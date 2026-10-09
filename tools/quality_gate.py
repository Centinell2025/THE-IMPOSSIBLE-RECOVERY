#!/usr/bin/env python3
"""Non-destructive source quality checks; execute full tests separately."""
import ast
from pathlib import Path

root = Path(__file__).resolve().parents[1]
scripts = sorted((root / "tools").glob("*.py"))
assert scripts, "No Python tooling found"
for path in scripts:
    ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
print(f"PASS: syntax parsed for {len(scripts)} Python tools")
required = [
    "README.md", "DISCLAIMER.md", "BRANDING_AND_ATTRIBUTION.md",
    "student/README.md", "student/CASE_BRIEF.md", "student/QUESTIONS.md",
    "student/ADVANCED_MISSIONS.md", "student/EXPERT_CASEWORK.md",
    "instructor/README.md", "instructor/ADVANCED_ASSESSMENT.md",
    "policy/CONTINUITY_AND_AUDIT.md", "topology/SERVER_INVENTORY.csv",
]
missing = [p for p in required if not (root / p).is_file()]
assert not missing, f"Missing required project files: {missing}"
print(f"PASS: {len(required)} required project documents present")
