# Investigation Requirements

Provide an evidence citation (relative file path and record identifier) for every answer. Times must be normalized to UTC where applicable. These are open-response prompts for advanced training; an official HTB grading format has **not** been established.

1. What is the earliest timestamped external atmospheric warning in the evidence package?
2. At what UTC time did the power monitoring feed report utility degradation?
3. Which infrastructure component is explicitly associated with the UPS transfer in the environmental record, and at what UTC time was the transfer recorded? Distinguish this observation from the separate UPS rack telemetry.
4. Which server's local clock is offset from UTC, by how many minutes, and in which direction?
5. After normalizing the offset, when did the monitoring system actually record the backup-success alert?
6. What is the earliest recorded network-degradation event across the available server and switch evidence, and which source recorded it? If events have different time precision, explain how you resolved their order.
7. Which two server roles show a dependency failure after the network event?
8. What policy-defined maximum audit gap applies during an emergency?
9. Did the audit collector meet the required cadence during the disturbance? Cite the relevant gap.
10. Which backup recovery-point identifier is the most recent one with a verified matching payload hash?
11. Which recovery-point identifier has a recorded success status but fails content-integrity verification?
12. Which source provides the recovery job's claimed status, and which independent source contradicts it?
13. Was there evidence of unauthorized privileged login in the supplied identity log? Distinguish absence of evidence from proof of absence.
14. What was the UTC order of: atmospheric warning, utility degradation, network loss, backup completion claim, and integrity audit?
15. What is the latest defensible recovery point and what limitation should accompany that recommendation?
16. Which artifacts would you prioritize preserving before attempting a second recovery?
17. Explain one way a time-normalization error could create a false incident narrative.
18. Draft a short executive finding separating confirmed facts, unresolved questions, and operational recommendations.

**Submission quality bar:** Every factual claim should be traceable to a specific synthetic artifact; unsupported attribution earns no credit.
