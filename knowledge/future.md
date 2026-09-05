# Future / not-MVP

This page is **not** required for the assignment MVP. The MVP is the official SRS freeze ([SRS freeze](srs.md)).

When the restaurant is implemented, implement **the SRS only** as the first app cut. Extra product ideas go here (or under `knowledge/future/`), not into that cut.

Meeting prep that **is** now on the thin map (once this ships): [Brief](brief.md) (Wed 2026-09-02 19:00 CET; owner locked 1, 3, 4), [Coverage](coverage.md) (FR-1..FR-18 / NFR-1..NFR-9), Friday **2026-09-04** working references — [Friday plan](friday-plan.md), [video script](video-script.md), [slides](presentation-sample.md) — and Saturday [talk cuts](presentation.md). Those delivery pages stay complete here and are also listed on the [Quantic / MSAIE](quantic.md) navigation hub (hub does not replace them). Those pages are knowledge, not extra restaurant features. **#22 / #34–#38 stay Future**; they are not grade gaps.

## Planned later (not the SRS cut)

- **Permanent** restaurant hosting on `cafe.artof.link` ([#22](https://github.com/artofdream/aea-interactive-design/issues/22)) — always-on productization, not the weekend window. AWS already exists as Lightsail `cafe-fausse-staging` ([#57](https://github.com/artofdream/aea-interactive-design/issues/57)): this session HTTPS GET **200** (2026-09-05) on `/`, `/api/health`, `/operator`. Postgres is **on the instance**; AEA RDS is untouched. Staging stays **up** until the owner explicitly requests tear-down. Monday **16:00 CET** is evaluate-only (not automatic tear-down). Quantic grader host need remains **Unknown** until their email. Future is **not** “AWS does not exist.” AWS is still **not** in the restaurant MVP *code* PR. Staging HLD lives on [Stack](stack.md), not as a new FR.
- Team Functional Spec v0.1 extras stay here (not new FR/NFR IDs) — see the [Brief compare](brief.md): reservation lifecycle [#34](https://github.com/artofdream/aea-interactive-design/issues/34), cancel/checkout/admin [#35](https://github.com/artofdream/aea-interactive-design/issues/35), menu CRUD [#36](https://github.com/artofdream/aea-interactive-design/issues/36), email identity [#37](https://github.com/artofdream/aea-interactive-design/issues/37), concurrency retry [#38](https://github.com/artofdream/aea-interactive-design/issues/38). Hosting remains [#22](https://github.com/artofdream/aea-interactive-design/issues/22).
- Knowledge-site depth beyond this thin map (more essays), owned by Café Fausse Knowledge.
- GitHub E2E beyond the assignment floor (issues, PR discipline, Actions sensors) used to prove, disprove, and **adjust** the outer harness.
- `docs/ai-tooling.md` kept current during implementation.

## Notes parked here (useful, not required)

- [Schema / outer harness layers](future/schema.md) — six layers scaled to this project
- [AWS `cafe_fausse_db` vs local schema](future/aws-schema-map.md) — teammate RDS dump map, rationale, diagrams; do not apply to MVP `schema.sql`
- [Glossary](future/glossary.md)
- [Journal stub](future/journal.md)

Do not read these as a second product. They are transfer notes for this repo. No florist Path B, 14 hats, or GitLab on this map.
