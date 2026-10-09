# Instructor Guide — The Impossible Recovery

**Classification:** Instructor planning document (public-safe edition)  
**Training level:** Advanced / expert DFIR  
**Scenario:** Fictional eight-server enterprise facing a severe atmospheric event

> **Publication warning:** This repository is currently public. Never commit answer keys, flags, hidden timelines, private scoring rubrics, or full walkthroughs here. Keep restricted instructor materials in a separate private repository or secured distribution channel.

## Instructional purpose

Teach investigators to assess evidence reliability under simultaneous infrastructure failures, rather than simply match suspicious strings.

## Competency areas

- Multi-host timeline reconstruction and clock-drift analysis
- Windows, Linux, network, and backup artifact correlation
- Audit completeness and chain-of-custody documentation
- Recovery point integrity and continuity-policy assessment
- Hypothesis testing, falsification, and reporting uncertainty

## Suggested delivery sequence

1. **Briefing:** Define infrastructure, operating constraints, and audit requirements.
2. **Acquisition review:** Confirm provenance, file hashes, and evidence inventory.
3. **Independent analysis:** Build timelines and document alternative explanations.
4. **Cross-system correlation:** Reconcile conflicting observations.
5. **Recovery assessment:** Test backup claims and identify evidentiary gaps.
6. **Debrief:** Require students to defend conclusions with artifacts.

## Evaluation principles

- Award credit for accurate, reproducible reasoning.
- Require specific evidence references for conclusions.
- Penalize unsupported attribution and fabricated indicators.
- Distinguish unknowns from verified negatives.
- Validate every challenge question against the generated dataset before release.

## Restricted instructor package (NOT in this public repository)

The eventual private package should include a verified answer key, full walkthrough, canonical incident timeline, artifact-generation scripts, validation results, scoring rubric, and troubleshooting notes.

## Readiness gate

Do not label this challenge production-ready until all eight server roles, atmospheric-event chronology, synthetic artifacts, questions, answers, and independent solution tests are complete.
