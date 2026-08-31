# Glossary (Future)

**Future / not-MVP.** Short terms used in this repo. Not a florist glossary.

- **MVP** — the reconstructed SRS (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9). First restaurant cut implements only this.
- **Freeze** — do not invent or rename requirement IDs; official PDF wins if it arrives.
- **Knowledge site** — this GitHub Pages surface. Intended hostname `knowledge.cafe.artof.link`. Not the restaurant.
- **Implementation site** — later restaurant. Intended hostname `cafe.artof.link`.
- **Unknown** — honest status when no probe has been run.
- **Probe** — command, HTTP GET, CI log, or file on disk, now.
- **DATE_RE** — `^[0-9]{4}-[0-9]{2}-[0-9]{2}$`; live handoff is `research/daily-briefs/YYYY-MM-DD.md` only.
- **Ratchet** — failures add guards; deleting a guard to go green is a regression.
- **Fail closed** — missing DB / full book / timeout / missing SRS → honest no.
- **Outer harness** — guides, sensors, loop, memory, permissions, observability around the freeze and (later) domain services.

Keep this glossary local to Café Fausse / this GitHub harness. Do not import another project’s product terms.
