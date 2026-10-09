# Northbridge Operations Center — Continuity & Audit Policy

**Policy ID:** NOC-BCP-07 | **Revision:** 1.0 | **Fictional training document**

## Required controls

- Maintain a monitored inventory of all eight production servers.
- Preserve local security and operational logs during severe weather.
- Collect a central audit heartbeat at least once every **5 minutes**.
- Record UTC or document measured offsets for non-UTC sources.
- Retain evidence copies before recovery actions change source state.
- Verify recovery-point content hashes independently of job success codes.
- Never mark a recovery point `trusted` based only on a scheduler status.
- Escalate utility power, network loss, backup integrity failures, and missed audit cadence to the continuity officer.

## Decision standard

A recoverable system is not automatically a forensically verified system. A recovery point is **verified** only when its available payload matches its recorded SHA-256 digest and its provenance is documented.

## Evidence handling

For each collected file, record original name, size, SHA-256, collection timestamp, custodian, and transformations. Preserve immutable originals and use copies for analysis.

## Training note

This policy is deliberately specific to the fictional case; it is not a substitute for a regulatory or industry standard.
