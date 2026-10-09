# Student Introduction — The Impossible Recovery

**Training track:** Advanced Digital Forensics and Incident Response (DFIR)  
**Target difficulty:** Insane (proposed; not assigned by Hack The Box)  
**Scenario type:** Fully fictional, synthetic enterprise incident

## Mission briefing

A fictional enterprise maintains eight critical servers and operates under a policy of continuous infrastructure monitoring, recurring audits, evidence preservation, and documented disaster recovery.

During a severe atmospheric event, power stability and network connectivity are disrupted. Several systems report successful recovery, but subsequent audit evidence is inconsistent. Your task is to reconstruct the incident, test competing explanations, and determine which conclusions the evidence actually supports.

The atmospheric event, sequence of failures, and underlying cause are still being designed; this introduction does **not** assert that an attacker was involved.

## Environment

| ID | Proposed role |
| --- | --- |
| SRV-01 | Identity and access management |
| SRV-02 | Application services |
| SRV-03 | Database |
| SRV-04 | File storage |
| SRV-05 | Backup and recovery |
| SRV-06 | Security monitoring |
| SRV-07 | Network and DNS |
| SRV-08 | Audit and evidence repository |

Server roles are provisional until the case design is finalized.

## Learning objectives

1. Build an evidence-backed, normalized timeline across heterogeneous systems.
2. Separate weather-related operational failures from security hypotheses.
3. Evaluate audit-log completeness and potential clock drift.
4. Validate integrity claims using independent evidence.
5. Assess whether recovery procedures complied with documented policy.
6. Identify the last demonstrably trustworthy recovery state.
7. Communicate uncertainty and distinguish observations from inferences.

## Investigation rules

- Treat every artifact as evidence to be verified, not as a guaranteed fact.
- Preserve original files; analyze working copies.
- Record filenames, hashes, timestamps, tools, and transformations.
- Support every answer with specific artifacts and reproducible reasoning.
- Do not assume malicious activity solely because systems disagree.
- No production systems or third-party targets are involved.

## Student materials status

**Design in progress.** Synthetic forensic datasets, challenge questions, and validated answers have not yet been released. This document is an orientation, not a completed or solvable Sherlock.
