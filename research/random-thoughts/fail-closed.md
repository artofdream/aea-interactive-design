# Fail closed

Failure class: missing dependency (no DB, no SRS file, timeout) treated as success or as a guessed booking.

Rule: missing `docs/srs.md` fails CI. Later restaurant MVP: missing PostgreSQL, a full slot (30 tables), or a timeout is an honest **no** (see FR-9), not a cached **yes**.
