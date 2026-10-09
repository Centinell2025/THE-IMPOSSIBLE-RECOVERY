# THE IMPOSSIBLE RECOVERY
### EchoTrace Case Files | Advanced DFIR Sherlock Training

**Status:** Original training scenario / candidate submission — not endorsed, accepted, or difficulty-rated by Hack The Box.  
**Target difficulty:** Insane (requires independent validation)  
**Language:** English  
**Scope:** Fully fictional enterprise, eight servers, severe atmospheric event, continuous audits.

## Incident premise

At 02:04 UTC, a severe thunderstorm destabilizes power and connectivity at the fictional **Northbridge Operations Center**. The organization must keep eight critical servers operational under its continuous-audit and disaster-recovery policy. Monitoring says that an emergency backup completed successfully. Independent audit data raises a different possibility.

Investigators must determine which observations are reliable, reconstruct the actual sequence of failures, distinguish clock drift from activity order, and identify the latest demonstrably valid recovery point. **Do not assume an intrusion occurred.**

## Start here

1. Read [Student Introduction](student/README.md), [Case Brief](student/CASE_BRIEF.md), and [Audit Policy](policy/CONTINUITY_AND_AUDIT.md).
2. Install Python 3.10+ (standard library only).
3. Run `python3 tools/generate_evidence.py` from the repository root.
4. Review the generated `evidence/` folder without editing original files.
5. Work through [Investigation Questions](student/QUESTIONS.md).
6. Run `python3 tools/verify_evidence.py` to check artifact completeness and hashes. This does **not** reveal answers.

## Directory layout

```text
student/           Public student orientation and questions
instructor/        Public-safe teaching methodology (no answer key)
policy/            Enterprise continuity and audit requirements
topology/          Eight-server inventory and dependency map
tools/             Deterministic synthetic evidence generator and verifier
evidence/          Generated locally; excluded from git by default
```

## Boundaries

All domains, users, servers, and events are fictional. All telemetry is **synthetic**. No real enterprise has been attacked; no real weather observations are represented. No hidden answer key or walkthrough is published. This repository is currently public; instructor-only solutions must stay in a separate private location.

## Validation

The generator produces an evidence manifest with SHA-256 hashes. Run the verifier after generation and before analysis. A passing integrity check confirms file consistency, **not** the truth of claims made inside individual logs.

## Development readiness

This is a runnable advanced training **prototype**, not yet a verified HTB-ready Insane Sherlock. Independent solve testing, final question grading, accessibility checks, and official submission packaging remain necessary.
