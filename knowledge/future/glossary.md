# Glossary (Future)

**Future / not-MVP.** Short terms used in this repo. Not a florist glossary.

- **MVP** — the official SRS freeze (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9; PDF SoT). First restaurant cut implements only this.
- **Freeze** — do not invent or rename requirement IDs; official PDF is source of truth.
- **Café Fausse Knowledge** — team that owns `knowledge.cafe.artof.link` (GitHub Pages knowledge map).
- **Café Fausse App** — team that owns `cafe.artof.link` restaurant MVP (later).
- **Knowledge site** — this GitHub Pages surface. Not the restaurant.
- **Implementation site** — later restaurant. Hosting future; not AWS in this PR.
- **Unknown** — honest status when no probe has been run **this session**.
- **Probe** — command, HTTP GET, CI log, or committed file on disk, this session.
- **DATE_RE** — `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`; live handoff is `research/daily-briefs/YYYY-MM-DD.md` only.
- **Shared memory** — committed git + today’s brief. Uncommitted files do not count.
- **Ratchet** — failures add guards; deleting a guard to go green is a regression.
- **Fail closed** — missing DB / full book / timeout / missing SRS or official PDF → honest no.
- **Outer harness** — guides, sensors, loop, memory, permissions, observability around the freeze and (later) domain services.

Keep this glossary local to Café Fausse / this GitHub harness. Do not import another project’s product terms.
