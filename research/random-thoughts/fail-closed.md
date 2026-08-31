# Fail closed

Failure class: missing dependency (no DB, no SRS file, timeout) treated as success or as a guessed booking.

Rule: missing `docs/srs.md` fails CI. ID freeze CI requires the actual `**FR-n:**` / `**NFR-n:**` entries (FR-1..FR-18, NFR-1..NFR-9), not a substring of the provenance range citation. Later restaurant MVP: missing PostgreSQL, a full slot (30 tables), or a timeout is an honest **no** (see FR-9), not a cached **yes**.
