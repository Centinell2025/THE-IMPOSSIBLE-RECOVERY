# Instructor Guide — Professional Competency Assessment

**Purpose:** Assess job-relevant reasoning, not just whether learners guessed an answer.

## Observable performance

An instructor should ask the learner to:
- explain why an artifact is reliable or unreliable;
- normalize an unsynchronized clock and defend the adjustment;
- reconcile conflicting monitoring and recovery claims;
- identify the limits of the available synthetic evidence;
- present a recovery decision under time pressure;
- deliver a report suitable for both technical staff and management.

## Suggested feedback rubric

| Dimension | Meets expectations when |
| --- | --- |
| Evidence handling | Original files remain unchanged and hashes are recorded |
| Technical analysis | Assertions cite specific artifacts and records |
| Incident judgment | Competing explanations are evaluated rather than assumed |
| Recovery decision | Recommendation considers integrity, availability, and uncertainty |
| Communication | Findings distinguish fact, inference, and unknowns |
| Ethics | No invented indicators, unsupported blame, or misleading certainty |

## Instructor simulation

Conduct a 15-minute incident command briefing. Assign one participant the role of investigator and another the role of continuity manager. The manager asks whether the latest backup is safe to restore. The investigator must answer with evidence, uncertainty, and an actionable next step.

## Important limits

The available synthetic dataset is intentionally compact. Instructors must not describe it as equivalent to full production DFIR experience. Expand artifact realism and conduct independent blind testing before describing the challenge as Insane-level or production-ready.
