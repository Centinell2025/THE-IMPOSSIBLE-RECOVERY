# Advanced Investigation Missions — The Impossible Recovery

**Target:** Expert-level DFIR training. All records are fictional and synthetic.  
**Prerequisite:** Read CASE_BRIEF.md and generate the base evidence package.

## Mission 01 — Eight-Server Dependency Cascade
Map all eight server dependencies from topology/SERVER_INVENTORY.csv. Determine which downstream services would be affected by a DNS outage. Distinguish a confirmed outage from a possible dependency effect. Submit a dependency graph and evidence citations.

## Mission 02 — Conflicting Clock Sources
Compare SRV-06's diagnostic clock offset with its alerts and independent audit records. Produce a two-column timeline (raw vs normalized UTC). Identify at least two investigative mistakes caused by failing to normalize timestamps.

## Mission 03 — Audit Continuity Under Severe Weather
Compare the central audit heartbeat against policy/CONTINUITY_AND_AUDIT.md. Identify all policy breaches, affected intervals, and what cannot be inferred from missing records. Draft a continuity exception report.

## Mission 04 — Recovery Integrity Challenge
Examine the recovery catalog and binary payloads. Calculate independent SHA-256 hashes. Identify recovery points whose recorded success state is unsupported by content integrity. Document the distinction between job completion and verifiable recovery.

## Mission 05 — Root Cause vs Coincidence
Build competing hypotheses: atmospheric power degradation, DNS/network dependency cascade, backup failure, or deliberate tampering. For each, state supporting evidence, contradictions, and missing data. Do not attribute malicious intent without evidence.

## Mission 06 — Evidence Preservation and Custody
Prepare a chain-of-custody form for the generated evidence set. Record source, collection method, time standard, SHA-256, analyst, and each working-copy transformation. State what the synthetic dataset cannot prove.

## Mission 07 — Crisis Decision Briefing
Act as incident commander. Decide whether to resume production from the newest backup, fall back to an earlier recovery point, or delay restoration. Present risk, policy impact, and evidence-based justification.

## Mission 08 — Adversarial Peer Review
Swap investigation reports with another analyst. Challenge every timestamp, assumption, and causal claim. Require one precise artifact citation per material assertion. Record unresolved disagreements.

## Required submissions
- Normalized event timeline in CSV
- Eight-server dependency diagram
- Backup integrity comparison worksheet
- Audit-policy exception report
- Evidence custody record
- Competing-hypotheses matrix
- Final incident report and executive decision memo

## Expert standard
A high-quality answer explicitly separates observed evidence, inference, and uncertainty. These missions are additional learning activities; they are not yet platform-graded HTB questions.
