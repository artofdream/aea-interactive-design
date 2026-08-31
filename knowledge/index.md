# Café Fausse — knowledge map

This is the **knowledge site** for the Quantic MSAIE Café Fausse project and a transfer of the AEA outer harness onto GitHub. It is **not** the restaurant and **not** a CMS.

**MVP = reconstructed SRS** ([SRS freeze](srs.md), full text in `docs/srs.md`). Everything else is [Future / not-MVP](future.md).

## Formula (pattern, scaled here)

**Adaptive Experience = Shared Understanding + Domain Services + Outer Harness.**

- **Shared Understanding** — the reviewable freeze: reconstructed SRS, today’s daily brief, honesty vocabulary.
- **Domain Services** — later restaurant runtime (React + JSX, Flask, PostgreSQL). Authoritative for reservations and newsletter **when they exist**. Not this cut.
- **Outer Harness** — guides (`AGENTS.md`, Cursor rules), sensors (GitHub Actions fail-closed), loop (issue → branch → PR), memory (daily briefs), permissions (owner adds collaborators), observability (status words need a probe).

AI may interpret. Domain services decide (once they exist). Status words are claims; they need a probe.

## Two public surfaces

| Surface | Intended hostname | Publish path | Live URL |
|---|---|---|---|
| Knowledge (this site) | `knowledge.cafe.artof.link` | GitHub Actions → GitHub Pages | **Unknown** — no GET probe; Pages/DNS are an owner step |
| Implementation (restaurant) | `cafe.artof.link` | Later (React + Flask + PostgreSQL) | **Unknown** — not built; no GET probe |

Do not invent other domains. Do not treat a hostname as a live site.

## Honesty

If evidence is missing, write **Unknown**. Closing a task is not a probe. See [Honesty](honesty.md).

## On this map (thin)

- [Stack](stack.md) — GitHub-only CI; knowledge vs restaurant runtime
- [SRS freeze](srs.md) — FR-1..FR-18, NFR-1..NFR-9
- [Honesty](honesty.md) — probes, Unknown
- [Future / not-MVP](future.md) — schema notes, glossary, journal stub, E2E beyond assignment
