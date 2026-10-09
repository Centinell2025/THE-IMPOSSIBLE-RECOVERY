#!/usr/bin/env python3
"""Generate a deterministic, fully fictional eight-server DFIR exercise."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
OUT.mkdir(exist_ok=True)

def write_csv(name, fields, rows):
    path = OUT / name
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def events(server, rows):
    write_csv(f"{server}.csv", ["record_id", "timestamp", "event", "detail"], [
        dict(record_id=f"{server}-{i:03}", timestamp=t, event=e, detail=d)
        for i, (t, e, d) in enumerate(rows, 1)
    ])

events("SRV-01", [
    ("2026-09-18T01:55:00Z", "AUTH_OK", "User nora.hale; privileged=false; source=10.44.0.18"),
    ("2026-09-18T02:08:00Z", "DNS_TIMEOUT", "Directory resolver unreachable"),
    ("2026-09-18T02:19:00Z", "AUTH_OK", "User svc-recovery; privileged=true; approved change NOC-CHG-118"),
])
events("SRV-02", [
    ("2026-09-18T02:09:00Z", "APP_DEGRADED", "Directory dependency unavailable"),
    ("2026-09-18T02:16:00Z", "APP_RETRY", "Database connection retries ongoing"),
])
events("SRV-03", [
    ("2026-09-18T02:11:00Z", "DB_TIMEOUT", "DNS resolution and connection pool failures"),
    ("2026-09-18T02:26:00Z", "DB_RECOVERED", "Connection pool healthy"),
])
events("SRV-04", [
    ("2026-09-18T02:07:00Z", "SMB_DEGRADED", "Authentication path intermittent"),
    ("2026-09-18T02:25:00Z", "SMB_RESTORED", "File shares reachable"),
])
events("SRV-05", [
    ("2026-09-18T01:30:00Z", "BACKUP_COMPLETE", "RP-0130; status=SUCCESS"),
    ("2026-09-18T02:10:00Z", "BACKUP_START", "RP-0210; job=BK-92"),
    ("2026-09-18T02:18:00Z", "BACKUP_COMPLETE", "RP-0210; job=BK-92; status=SUCCESS"),
])
# SRV-06 clock is deliberately seven minutes ahead; do not normalize these raw records.
events("SRV-06", [
    ("2026-09-18T02:06:00Z", "CLOCK_DIAGNOSTIC", "local_clock_offset_seconds=+420"),
    ("2026-09-18T02:25:00Z", "ALERT", "Backup job BK-92 reported SUCCESS by SRV-05"),
    ("2026-09-18T02:34:00Z", "ALERT", "Integrity mismatch RP-0210 reported by SRV-08"),
])
events("SRV-07", [
    ("2026-09-18T02:06:00Z", "LINK_DOWN", "Core uplink port eth1 unavailable"),
    ("2026-09-18T02:23:00Z", "LINK_UP", "Core uplink port eth1 restored"),
])
events("SRV-08", [
    ("2026-09-18T02:00:00Z", "AUDIT_HEARTBEAT", "collector healthy"),
    ("2026-09-18T02:05:00Z", "AUDIT_HEARTBEAT", "collector healthy"),
    ("2026-09-18T02:17:00Z", "AUDIT_HEARTBEAT", "collector delayed after link loss"),
    ("2026-09-18T02:27:00Z", "INTEGRITY_CHECK", "RP-0210 digest mismatch; RP-0130 verified"),
    ("2026-09-18T02:30:00Z", "AUDIT_HEARTBEAT", "collector healthy"),
])
write_csv("environment.csv", ["record_id", "timestamp_utc", "sensor", "event", "detail"], [
    dict(record_id="ENV-001", timestamp_utc="2026-09-18T01:48:00Z", sensor="weather-feed", event="SEVERE_STORM_WARNING", detail="Simulated severe thunderstorm warning"),
    dict(record_id="ENV-002", timestamp_utc="2026-09-18T02:04:00Z", sensor="power-meter", event="UTILITY_DEGRADED", detail="Voltage below configured threshold"),
    dict(record_id="ENV-003", timestamp_utc="2026-09-18T02:05:00Z", sensor="ups-controller", event="UPS_TRANSFER", detail="SRV-07 rack power switched to battery"),
    dict(record_id="ENV-004", timestamp_utc="2026-09-18T02:22:00Z", sensor="power-meter", event="UTILITY_RESTORED", detail="Voltage returned to nominal"),
])
# Payloads and reference digests intentionally disagree for one recovery point.
payloads = {
    "RP-0130": b"NORTHBRIDGE|DATABASE|SNAPSHOT|2026-09-18T01:30:00Z|REV=41\n",
    "RP-0210": b"NORTHBRIDGE|DATABASE|SNAPSHOT|2026-09-18T02:10:00Z|REV=43|INCOMPLETE\n",
}
expected_0210 = b"NORTHBRIDGE|DATABASE|SNAPSHOT|2026-09-18T02:10:00Z|REV=43|COMPLETE\n"
catalog = []
for rp, payload in payloads.items():
    path = OUT / f"{rp}.bin"
    path.write_bytes(payload)
    expected = payload if rp == "RP-0130" else expected_0210
    catalog.append(dict(
        recovery_point=rp, source_server="SRV-05",
        scheduler_status="SUCCESS",
        payload_file=path.name,
        catalog_sha256=hashlib.sha256(expected).hexdigest(),
        observed_sha256=hashlib.sha256(payload).hexdigest(),
    ))
write_csv("backup_catalog.csv", list(catalog[0]), catalog)

manifest = []
for p in sorted(OUT.iterdir()):
    if p.is_file() and p.name != "evidence_manifest.json":
        manifest.append({"file": p.name, "size_bytes": p.stat().st_size,
                         "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
(OUT / "evidence_manifest.json").write_text(
    json.dumps({"case_id": "NB-IR-026", "synthetic": True, "files": manifest},
               indent=2) + "\n", encoding="utf-8"
)
print(f"Generated {len(manifest)} synthetic artifacts in {OUT}")
print("Run: python3 tools/verify_evidence.py")
