#!/usr/bin/env python3
"""Validate forensic case consistency without publishing a solution key."""
import csv
import hashlib
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
subprocess.run([sys.executable, str(ROOT / "tools/test_advanced.py")], check=True)

def rows(name):
    with (OUT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def utc(raw):
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))

servers = {f"SRV-{i:02}": rows(f"SRV-{i:02}.csv") for i in range(1, 9)}
assert len(servers) == 8
ids = [record["record_id"] for events in servers.values() for record in events]
assert len(ids) == len(set(ids)), "Duplicate server record identifiers"

offset = 420
siem = servers["SRV-06"]
assert all(not r["timestamp"].endswith("Z") for r in siem), "Unsynchronized clock falsely marked UTC"
assert any("local_clock_offset_seconds=+420" in r["detail"] for r in siem)
success_alert = next(r for r in siem if "BK-92" in r["detail"])
normalized = datetime.fromisoformat(success_alert["timestamp"]).replace(tzinfo=timezone.utc) - timedelta(seconds=offset)
backup_success = next(r for r in servers["SRV-05"] if "BK-92" in r["detail"] and r["event"] == "BACKUP_COMPLETE")
assert normalized == utc(backup_success["timestamp"]), "SIEM normalization disagrees with backup completion"

catalog = rows("backup_catalog.csv")
assert len(catalog) == 2
assert sum(r["catalog_sha256"] != r["observed_sha256"] for r in catalog) == 1
for r in catalog:
    digest = hashlib.sha256((OUT / r["payload_file"]).read_bytes()).hexdigest()
    assert digest == r["observed_sha256"], "Payload does not match observed digest"

audit = [utc(r["timestamp"]) for r in servers["SRV-08"] if r["event"] == "AUDIT_HEARTBEAT"]
assert audit == sorted(audit)
assert any((b-a).total_seconds() > 300 for a, b in zip(audit, audit[1:])), "Expected audit cadence gap not present"

for name in ("ups_power_telemetry.csv", "network_switch_events.csv", "storage_integrity_events.csv", "change_control.csv", "audit_forwarder_queue.csv", "ntp_observations.csv"):
    items = rows(name)
    assert items and all("id" in r and "timestamp_utc" in r for r in items), f"Malformed {name}"
    assert all(utc(r["timestamp_utc"]).tzinfo is not None for r in items), f"Invalid UTC timestamp in {name}"

print("PASS: case consistency, clock normalization, audit gap, unique IDs, backup integrity, supplemental evidence.")
