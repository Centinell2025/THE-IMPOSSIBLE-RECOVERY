# Expert Casework — Supplemental Investigation

Generate base artifacts first, then supplemental sources:

```bash
python3 tools/generate_evidence.py
python3 tools/build_advanced_artifacts.py
python3 tools/verify_evidence.py
python3 tools/test_case.py
```

**Note:** Running test_case.py regenerates the base package and therefore removes the supplemental files from the manifest until build_advanced_artifacts.py is rerun. For the complete evidence set, run the three commands in order: generate, build, verify.

## Exercise A — Electrical Failure Reconstruction
Reconcile UPS transfer and rack battery telemetry with utility voltage. Identify what is directly observed and what is inferred about infrastructure power.

## Exercise B — Network Causality
Reconcile switch port flaps, the DNS server, and downstream application failures. Separate event timestamps from later service-health observations.

## Exercise C — Storage Write Reliability
Compare storage I/O events against scheduler status and backup-catalog digests. Explain how a recovery job can complete with a false-positive status.

## Exercise D — Audit Queue Versus Audit Receipt
Use the forwarder queue and audit collector heartbeats to distinguish local buffering from centrally received evidence. State whether queued events alone prove compliance with a central five-minute audit requirement.

## Exercise E — Authorization Review
Correlate privileged authentication records with change-control authorization. Explain why the presence of privileged access is not automatically an indicator of compromise.

## Exercise F — Clock Offset Validation
Compare NTP observations and SIEM event timestamps. Reconstruct alert times in UTC and identify uncertainty that remains after normalization.

## Final report requirements
Produce an evidence-based incident timeline, a causal dependency diagram, a backup-integrity decision, a policy exception table, and a concise recommendation with explicit uncertainty.

**Difficulty:** Advanced training extension, not independently validated as an HTB Insane challenge.
