# Future / not-MVP

This page is **not** required for the assignment MVP. The MVP is the official SRS freeze ([SRS freeze](srs.md)).

When the restaurant is implemented, implement **the SRS only** as the first app cut. Extra product ideas go here (or under `knowledge/future/`), not into that cut.

Meeting prep that **is** now on the thin map (once this ships): [Brief](brief.md) (Wed 2026-09-02 19:00 CET) and [Coverage](coverage.md) (FR-1..FR-18 / NFR-1..NFR-9). Those pages are knowledge, not extra restaurant features.

## Planned later (not the SRS cut)

- Public restaurant on intended hostname `cafe.artof.link` (React + JSX, Flask, PostgreSQL), owned by Café Fausse App. **That hostname is not Café Fausse today** (CNAME to an AWS ELB, probed 2026-09-02). Hosting is future. **AWS is not in the restaurant MVP PR.**
- Team Functional Spec v0.1 extras (reservation lifecycle, menu CRUD, and related hardening) stay here — see the [Brief compare](brief.md). Not new FR/NFR IDs.
- Knowledge-site depth beyond this thin map (more essays), owned by Café Fausse Knowledge.
- GitHub E2E beyond the assignment floor (issues, PR discipline, Actions sensors) used to prove, disprove, and **adjust** the outer harness.
- `docs/ai-tooling.md` kept current during implementation.

## Notes parked here (useful, not required)

- [Schema / outer harness layers](future/schema.md) — six layers scaled to this project
- [Glossary](future/glossary.md)
- [Journal stub](future/journal.md)

Do not read these as a second product. They are transfer notes for this repo. No florist Path B, 14 hats, or GitLab on this map.
