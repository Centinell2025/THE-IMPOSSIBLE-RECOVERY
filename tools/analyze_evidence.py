#!/usr/bin/env python3
"""Student-friendly evidence inventory and integrity report. No hidden answers."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
manifest_path = EVIDENCE / "evidence_manifest.json"
if not manifest_path.exists():
    raise SystemExit("Generate evidence first: python3 tools/generate_evidence.py")

manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
print("CASE:", manifest["case_id"], "| Synthetic:", manifest["synthetic"])
print("FILE INVENTORY")
for item in manifest["files"]:
    p = EVIDENCE / item["file"]
    digest = hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "MISSING"
    print(f'{item["file"]:24} {item["size_bytes"]:>7} bytes  verified={digest == item["sha256"]}')

print("\nTIMESTAMP SOURCES (raw timestamps; do not assume clocks are synchronized)")
for p in sorted(EVIDENCE.glob("SRV-*.csv")):
    with p.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    print(f"{p.name:18} records={len(rows):>2} first={rows[0]['timestamp'] if rows else 'none'}")
print("\nNext: independently reconcile sources; this utility does not decide incident cause.")
