# Café Fausse — knowledge map

This is the **knowledge site** for the Quantic MSAIE Café Fausse project and a transfer of the AEA outer harness onto GitHub. It is **not** the restaurant and **not** a CMS.

**MVP = official SRS** ([SRS freeze](srs.md), working copy `docs/srs.md`; SoT = official PDF). Everything else is [Future / not-MVP](future.md).

## Teams

| Team | Owns | Intended hostname | Live URL |
|---|---|---|---|
| Café Fausse Knowledge | This knowledge site (GitHub Pages) | `knowledge.cafe.artof.link` | **HTTPS GET 200** this session at `https://knowledge.cafe.artof.link/` (TLS CN / SAN match). Pages `https_enforced`: **false** (HTTP also 200). |
| Café Fausse App | Restaurant MVP on `main` (merged PRs #9, #12). Local: Vite `127.0.0.1:5173`, Flask `:5000`, `cafe-pg` | `cafe.artof.link` | **Not our live app.** This session: CNAME to an AWS ELB hostname that did not resolve (GET failed). Hosting future. Local GET `:5173` / `:5000`: failed here (not running). |

AWS is not in the restaurant MVP. Do not invent other domains.

## Formula (pattern, scaled here)

**Adaptive Experience = Shared Understanding + Domain Services + Outer Harness.**

- **Shared Understanding** — the reviewable freeze: official SRS (PDF SoT), today’s daily brief, honesty vocabulary.
- **Domain Services** — in-repo restaurant runtime (React + JSX, Flask, PostgreSQL) for reservations and newsletter. Authoritative when PostgreSQL accepts the write. Public hosting of `cafe.artof.link` is Future.
- **Outer Harness** — guides (`AGENTS.md`, Cursor rules), sensors (GitHub Actions fail-closed), loop (issue → branch → PR), memory (daily briefs), permissions (owner adds collaborators), observability (status words need a probe).

AI may interpret. Domain services decide. Status words are claims; they need a probe.

## Two public surfaces

| Surface | Team | Intended hostname | Publish path | Live URL |
|---|---|---|---|---|
| Knowledge (this site) | Café Fausse Knowledge | `knowledge.cafe.artof.link` | GitHub Actions → GitHub Pages | **HTTPS GET 200** this session; TLS CN match. `https_enforced` still **false** (owner can tick Enforce HTTPS). |
| Implementation (restaurant) | Café Fausse App | `cafe.artof.link` | In-repo React + Flask + PostgreSQL. Hosting future; not AWS in the MVP PR. | **Not our live app** (dangling ELB CNAME; GET did not resolve). Local run: README; this session local GET **Unknown**/failed. |

Do not invent other domains. Do not treat a hostname as a live site without a GET this session.

## Honesty

If evidence is missing, write **Unknown**. Closing a task is not a probe. See [Honesty](honesty.md).

## On this map (thin)

- [Stack](stack.md) — GitHub-only CI; knowledge vs restaurant runtime
- [SRS freeze](srs.md) — FR-1..FR-18, NFR-1..NFR-9
- [FR/NFR coverage](coverage.md) — presentation matrix (paths, evidence class, why for the course)
- [Teammate brief](teammate-brief.md) — Wed 2026-09-02 19:00 CET meeting
- [Honesty](honesty.md) — probes, Unknown
- [Future / not-MVP](future.md) — schema notes, glossary, journal stub, E2E beyond assignment
