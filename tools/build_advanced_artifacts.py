#!/usr/bin/env python3
"""Create deterministic supplemental synthetic forensic artifacts.
Run after generate_evidence.py. No external services or packages required.
"""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
if not (OUT / "evidence_manifest.json").is_file():
    raise SystemExit("First run: python3 tools/generate_evidence.py")

def csvfile(name, columns, rows):
    with (OUT / name).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

csvfile("ups_power_telemetry.csv",
        ["id","timestamp_utc","rack","utility_voltage","ups_load_percent","battery_percent","state"],
        [
            ["UPS-01","2026-09-18T02:00:00Z","RACK-NET",121,58,100,"UTILITY"],
            ["UPS-02","2026-09-18T02:04:00Z","RACK-NET",87,60,100,"UNDERVOLTAGE"],
            ["UPS-03","2026-09-18T02:05:00Z","RACK-NET",0,61,98,"BATTERY"],
            ["UPS-04","2026-09-18T02:12:00Z","RACK-NET",0,64,75,"BATTERY"],
            ["UPS-05","2026-09-18T02:22:00Z","RACK-NET",119,62,59,"UTILITY_RESTORED"],
        ])
csvfile("network_switch_events.csv",
        ["id","timestamp_utc","device","port","event","detail"],
        [
            ["NET-01","2026-09-18T02:05:42Z","sw-core-01","Gi1/0/24","FLAP","CRC errors increasing"],
            ["NET-02","2026-09-18T02:06:00Z","sw-core-01","Gi1/0/24","DOWN","Uplink to nb-net01 unavailable"],
            ["NET-03","2026-09-18T02:06:12Z","sw-core-01","Gi1/0/8","DNS_TIMEOUT","Identity resolver requests timed out"],
            ["NET-04","2026-09-18T02:23:00Z","sw-core-01","Gi1/0/24","UP","Uplink restored"],
        ])
csvfile("storage_integrity_events.csv",
        ["id","timestamp_utc","device","volume","event","detail"],
        [
            ["STO-01","2026-09-18T02:10:00Z","nb-backup01","/backup","WRITE_BEGIN","Recovery point RP-0210"],
            ["STO-02","2026-09-18T02:15:00Z","nb-backup01","/backup","IO_RETRY","Transient storage retry"],
            ["STO-03","2026-09-18T02:17:40Z","nb-backup01","/backup","WRITE_INCOMPLETE","Final segment not committed"],
            ["STO-04","2026-09-18T02:18:00Z","nb-backup01","/backup","JOB_STATUS","Scheduler reports SUCCESS"],
        ])
csvfile("change_control.csv",
        ["id","timestamp_utc","requester","change_id","action","authorization"],
        [
            ["CHG-01","2026-09-18T01:40:00Z","continuity-officer","NOC-CHG-118","Emergency recovery access approved","APPROVED"],
            ["CHG-02","2026-09-18T02:19:00Z","svc-recovery","NOC-CHG-118","Privileged recovery session","WITHIN_WINDOW"],
        ])
csvfile("audit_forwarder_queue.csv",
        ["id","timestamp_utc","device","queue_depth","status","detail"],
        [
            ["AUD-01","2026-09-18T02:05:00Z","nb-audit01",0,"HEALTHY","Heartbeat sent"],
            ["AUD-02","2026-09-18T02:07:00Z","nb-audit01",31,"QUEUED","Collector path unavailable"],
            ["AUD-03","2026-09-18T02:12:00Z","nb-audit01",68,"QUEUED","Audit events buffered locally"],
            ["AUD-04","2026-09-18T02:17:00Z","nb-audit01",12,"DRAINING","Collector reachable"],
            ["AUD-05","2026-09-18T02:20:00Z","nb-audit01",0,"HEALTHY","Forwarder queue drained"],
        ])
csvfile("ntp_observations.csv",
        ["id","timestamp_utc","device","observed_offset_seconds","source"],
        [
            ["NTP-01","2026-09-18T02:00:00Z","nb-siem01",420,"local diagnostic"],
            ["NTP-02","2026-09-18T02:29:00Z","nb-siem01",420,"post-event diagnostic"],
            ["NTP-03","2026-09-18T02:29:00Z","nb-audit01",0,"trusted reference"],
        ])
manifest_path = OUT / "evidence_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["files"] = [
    {"file": p.name, "size_bytes": p.stat().st_size,
     "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
    for p in sorted(OUT.iterdir())
    if p.is_file() and p.name != manifest_path.name
]
manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print("Added six supplemental evidence sources; updated SHA-256 manifest.")
