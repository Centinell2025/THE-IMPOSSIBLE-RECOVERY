# Case Brief — Atmospheric Emergency

**Case ID:** NB-IR-026  
**Classification:** Fictional / Controlled DFIR Exercise  
**Time standard:** UTC for synchronized sources. SRV-06 records use unsynchronized local wall-clock timestamps **without a timezone suffix**; its observed clock offset is documented in the evidence. Never interpret an unsuffixed SRV-06 timestamp as UTC.

## Organization

Northbridge Operations Center (NOC) is a fictional enterprise continuing the EchoTrace training universe. Its eight servers deliver identity, application, database, file, backup, security monitoring, DNS, and audit functions.

## The event

A severe atmospheric disturbance causes an unstable utility feed and intermittent network links. UPS transfer is recorded; monitoring and recovery records subsequently disagree. The continuity officer asks the forensic team to answer one operational question: **Can the claimed recovery be trusted?**

## Constraints

- Continuous auditing is mandatory, including during degraded operations.
- No system is automatically trusted because it reports `SUCCESS`.
- Evidence must be compared across independent sources.
- Clock offsets must be documented before timeline conclusions.
- Business continuity and forensic integrity are separate requirements.

## Evidence package

Generate the case dataset using `python3 tools/generate_evidence.py`. The generator creates eight server logs, environmental telemetry, audit checks, backup catalog and payloads, and a manifest. This is synthetic training data, not a forensic image from a real incident.

## Deliverable

Provide a defensible UTC timeline, policy assessment, integrity analysis, recovery recommendation, and a concise explanation of remaining uncertainty.
