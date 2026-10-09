# Advanced Instructor Assessment Framework (Public-Safe)

This document contains **no hidden solutions or answer key**.

## Assessment criteria (100 points)
| Dimension | Points |
| --- | ---: |
| Evidence acquisition and integrity verification | 15 |
| Timestamp normalization and chronology | 20 |
| Eight-server dependency reasoning | 15 |
| Audit-policy compliance analysis | 15 |
| Backup and recovery integrity reasoning | 15 |
| Competing hypotheses and uncertainty | 10 |
| Executive communication and defensible recommendations | 10 |

## Teaching notes
Ask learners to cite the record identifier and artifact path supporting each factual assertion. Reward explicit uncertainty when the evidence is insufficient. Do not reward unsupported attacker attribution.

## Advanced oral examination prompts
- What additional independent data would falsify your primary hypothesis?
- Which timestamps are observation times versus event occurrence times?
- Why can a successful job status coexist with unusable recovery data?
- Which audit gaps limit your ability to establish negative findings?
- What evidence should be acquired before any additional restoration?

## Instructor release gate
1. All questions have unique and reproducible answers or clearly expect an uncertainty assessment.
2. A second analyst completes the exercise without access to the author's notes.
3. All timestamps, offsets, and event dependencies are consistent.
4. Generated evidence and SHA-256 manifests validate.
5. The confidential instructor walkthrough is stored separately from this public repository.
