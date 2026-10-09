#!/usr/bin/env python3
"""Check synthetic evidence package completeness and SHA-256 integrity."""
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "evidence"
manifest_path = root / "evidence_manifest.json"
if not manifest_path.is_file():
    sys.exit("FAIL: no manifest; first run python3 tools/generate_evidence.py")
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
if manifest.get("case_id") != "NB-IR-026" or manifest.get("synthetic") is not True:
    sys.exit("FAIL: unexpected case manifest")
expected = {e["file"] for e in manifest["files"]}
actual = {p.name for p in root.iterdir() if p.is_file()} - {"evidence_manifest.json"}
errors = []
for item in manifest["files"]:
    p = root / item["file"]
    if not p.is_file():
        errors.append(f"missing: {p.name}")
        continue
    data = p.read_bytes()
    if len(data) != item["size_bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
        errors.append(f"hash or size mismatch: {p.name}")
for extra in sorted(actual - expected):
    errors.append(f"unmanifested file: {extra}")
if errors:
    for e in errors:
        print("FAIL:", e)
    sys.exit(1)
print(f"PASS: {len(expected)} synthetic evidence artifacts match the SHA-256 manifest.")
print("Note: manifest integrity does not validate the backup catalog's recovery claims.")
