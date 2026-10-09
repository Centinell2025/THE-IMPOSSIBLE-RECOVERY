#!/usr/bin/env python3
"""Reproducible structural and integrity tests for full synthetic exercise."""
import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for tool in ["generate_evidence.py", "build_advanced_artifacts.py", "verify_evidence.py"]:
    subprocess.run([sys.executable, str(ROOT / "tools" / tool)], check=True)

out = ROOT / "evidence"
files = ["ups_power_telemetry.csv", "network_switch_events.csv",
         "storage_integrity_events.csv", "change_control.csv",
         "audit_forwarder_queue.csv", "ntp_observations.csv"]
for filename in files:
    with (out / filename).open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) >= 2, f"Too few events in {filename}"
    assert all(row.get("id") for row in rows), f"Missing record IDs in {filename}"

assert len(list(out.glob("SRV-*.csv"))) == 8
assert len(list(out.glob("*.csv"))) >= 15
print("PASS: 8 server logs, 6 supplemental sources, complete evidence hashes.")
