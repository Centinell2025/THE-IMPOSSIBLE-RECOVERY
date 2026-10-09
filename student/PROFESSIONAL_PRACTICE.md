# Professional Practice — From Sherlock Challenge to Real-World DFIR Skills

**Developer:** Beacon of the Eagle LLC — Centinell Forensics Enterprise

## Why this case matters

This fictional exercise simulates the decisions an incident responder, forensic examiner, SOC analyst, infrastructure engineer, or continuity manager may face when severe weather disrupts critical services.

The objective is not merely to solve questions. The objective is to demonstrate **repeatable professional judgment**: preserve evidence, distinguish facts from assumptions, validate recovery claims, and communicate operational risk.

## Professional competencies and deliverables

| Workplace responsibility | Practical task | Evidence of competence |
| --- | --- | --- |
| Initial incident response | Establish scope, impacted services, and immediate preservation priorities | Incident intake and triage note |
| Forensic acquisition | Inventory files, compute SHA-256, maintain working copies | Evidence register and custody record |
| Timeline analysis | Reconcile eight server logs, switch records, UPS events, and clock drift | Normalized UTC timeline with citations |
| Service dependency analysis | Map identity, DNS, database, application, and backup relationships | Dependency map and outage analysis |
| Audit and compliance | Evaluate audit heartbeat gaps against company policy | Audit exception report |
| Backup validation | Independently verify recovery-point content rather than trusting SUCCESS | Recovery integrity worksheet |
| Root-cause reasoning | Test weather, infrastructure, process, and malicious-action hypotheses | Evidence-based hypothesis matrix |
| Executive communication | Explain verified findings, limitations, and recovery choices | Executive incident brief |

## Rules of professional conduct

- Do not claim an intrusion without supporting evidence.
- Never modify source artifacts during analysis.
- Do not equate a passing SHA-256 manifest check with proof that a recovery is usable.
- Identify where telemetry is incomplete or clocks are not synchronized.
- Distinguish operational restoration from forensic verification.
- Document every important decision and its evidence.
- State uncertainty explicitly; do not invent missing facts.

## Final capstone

The learner acts as the lead incident responder and submits:

1. A concise executive briefing.
2. A normalized event timeline and evidence index.
3. A policy compliance assessment.
4. A backup/recovery decision with alternatives and residual risk.
5. A technical appendix that allows another analyst to reproduce the conclusions.

## Career relevance

These deliverables resemble work products used in incident response, SOC escalation, digital forensics, business continuity, and technical audit teams. Completing this simulated case is **not** a professional certification or proof of real-world field experience; it is an opportunity to practice and demonstrate specific analytical skills.

## Reflection questions

What would you do differently if the organization needed to restore service within 30 minutes? Which additional data sources would you request? What could you responsibly tell a customer before the investigation is complete?
