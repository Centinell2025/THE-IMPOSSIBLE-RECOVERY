# Quality Assurance and Release Gate

**Current status:** DEVELOPMENT / NOT YET INDEPENDENTLY VALIDATED.

## Confirmed source-level corrections
- Advanced CSV generator now uses csv.writer for positional data rows.
- Unsynchronized SRV-06 timestamps omit the misleading UTC Z suffix.
- Baseline test regenerates both basic and advanced sources before manifest verification.
- Student advanced runbook references the full advanced test.

## Reproducible local validation

From a fresh clone with Python 3.10+:

```bash
python3 tools/test_case.py
python3 tools/test_advanced.py
python3 tools/verify_evidence.py
python3 tools/analyze_evidence.py
```

Expected: all commands exit 0. A successful test validates deterministic generation, structural checks, and SHA-256 file consistency. It does **not** independently validate the realism or grading uniqueness of the scenario.

## Release acceptance criteria
- [ ] GitHub Actions baseline and advanced workflows both green on current commit
- [ ] Fresh-clone reproducibility independently confirmed
- [ ] Every question independently solved from the provided artifacts
- [ ] No ambiguous question, incorrect timestamp, or unsupported causal assertion
- [ ] Realistic Windows/Linux forensic artifact depth beyond simplified CSV telemetry
- [ ] Instructor-only walkthrough and answer key stored privately
- [ ] Platform submission, rights, and public-disclosure conditions checked
- [ ] Original Beacon logo binary uploaded and displayed correctly
- [ ] Accessibility and readability checked
- [ ] Second analyst blind solve completed

## Reviewer findings requiring resolution
- [ ] Verify every question against the generated artifacts and eliminate multi-answer wording.
- [ ] Distinguish upstream event time from SIEM alert observation/ingestion time.
- [ ] Confirm whether environmental component identifiers and rack identifiers can be joined without assumptions.
- [ ] Perform a blind solve and verify answer uniqueness, evidence provenance, and expected grading.

## Known limitations
Current artifacts are **synthetic CSV logs and small sample binary payloads**, not raw EVTX, journal, packet capture, memory, or disk images. The exercise is useful for correlation practice but cannot yet be described as an independently validated Insane-level Sherlock.

## Data protection
Do not include credentials, real customer data, proprietary logs, private instructor answers, or unauthorized third-party intellectual property.
