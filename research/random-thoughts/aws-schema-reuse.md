# AWS schema reuse (portable)

Failure class: copying a teammate RDS dump onto local `backend/schema.sql` and calling it an optimization.

Rule: local MVP stays fail-closed (FR-8 / FR-9 / NFR-5). Map columns on **import**. Do not rename local Flask columns. Do not import `menu_*` until Future #36. Naive `time_slot` → America/New_York timestamptz. Skip null `table_number`.

IAM: `cafe_fausse_developer` uses temporary RDS tokens. Do not mint a permanent password. No cts-ai required to apply this note.

Canonical write-up (knowledge site source): `knowledge/future/aws-schema-map.md`. Live handoff: `research/daily-briefs/YYYY-MM-DD.md` only.
