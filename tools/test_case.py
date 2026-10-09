#!/usr/bin/env python3
"""Public consistency tests; deliberately does not disclose a complete answer key."""
import csv
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(ROOT / "tools/generate_evidence.py")], check=True)
subprocess.run([sys.executable, str(ROOT / "tools/verify_evidence.py")], check=True)
evidence = ROOT / "evidence"

def rows(name):
    with (evidence / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

assert len([p for p in evidence.glob("SRV-*.csv")]) == 8, "Must include eight servers"
assert len(rows("environment.csv")) >= 4
catalog = rows("backup_catalog.csv")
assert len(catalog) == 2
for item in catalog:
    actual = hashlib.sha256((evidence / item["payload_file"]).read_bytes()).hexdigest()
    assert actual == item["observed_sha256"], "Observed digest inconsistent"
assert sum(row["catalog_sha256"] != row["observed_sha256"] for row in catalog) == 1, "Expected one integrity discrepancy"
assert any("local_clock_offset_seconds=" in r["detail"] for r in rows("SRV-06.csv"))
print("PASS: eight-server dataset, environmental events, clock-offset clue, and recovery-integrity discrepancy.")
