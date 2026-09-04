# Café Fausse — knowledge map

This is the **knowledge site** for the Quantic MSAIE Café Fausse project and a transfer of the AEA outer harness onto GitHub. It is **not** the restaurant and **not** a CMS.

**MVP = official SRS** ([SRS freeze](srs.md), working copy `docs/srs.md`; SoT = official PDF). Everything else is [Future / not-MVP](future.md).

Teammate meeting **Wed 2026-09-02 19:00 CET** (owner locked **1, 3, 4** — not 2): start with the [Brief](brief.md) (clips; FS v0.1 vs SRS MVP compare). Course presentation map: [FR/NFR coverage](coverage.md).

Friday **2026-09-04 19:00 Europe/Berlin** (score 5): [Friday plan](friday-plan.md) (P0/P1/P2; live vs local vs Future). App tunnel this session: `https://real-goats-shop.loca.lt/` GET **200** (SPA + `/api/health`; **slow (~10–20s)**; **interstitial-possible** in browsers — not snappy, not always-on) — temporary localtunnel to Flask on cts-ai, **not** `cafe.artof.link`. Knowledge HTTPS + [clips on the Brief](brief.md) stay fallback. Working drafts: [video script](video-script.md), [slides](presentation-sample.md), Saturday [talk cuts](presentation.md). [Issue #40](https://github.com/artofdream/aea-interactive-design/issues/40) / [#44](https://github.com/artofdream/aea-interactive-design/issues/44) recorded on [Coverage](coverage.md): J1–J8 **PASS** (cts-ai, DB up); J9 **PASS** (Vite-only viewports + theme); **NFR-7** **partial** (Edge + Firefox home; Chrome/Safari Unknown); **NFR-1** / **NFR-2** stay not-claimed-met.

## Teams

| Team | Owns | Intended hostname | Live URL (probe 2026-09-02 Europe/Berlin) |
|---|---|---|---|
| Café Fausse Knowledge | This knowledge site (GitHub Pages) | `knowledge.cafe.artof.link` | HTTPS **GET 200** this session (2026-09-04); HTTP **301** to HTTPS; TLS VERIFY_OK; CN/SAN `knowledge.cafe.artof.link`. |
| Café Fausse App | Restaurant MVP (React + JSX, Flask, PostgreSQL) | `cafe.artof.link` | **Not Café Fausse.** DNS CNAME → AWS ELB `eu-north-1`. Do not claim this hostname is the restaurant. App is **in-repo on `main`** (PRs #9 + timezone #12). Public hosting remains future. |

AWS is not in the restaurant MVP cut. App on cts-ai (not this VM): Vite `http://127.0.0.1:5173`, Flask `:5000`, `cafe-pg`. Tunnel this session: `https://real-goats-shop.loca.lt/` GET **200** (SPA HTML); `/api/health` GET **200** `{"ok":true}`. Knowledge GET: root **200** ~15s; `/api/health` **200** ~15s. **Slow (~10–20s)**; **interstitial-possible** in browsers. Short timeouts can look like failure. Not snappy. Not always-on. Temporary localtunnel to Flask. **Not** `cafe.artof.link`. Journey **J1–J8 PASS** (2026-09-02, DB up); **J9 PASS** Vite-only (viewports + theme). This VM did not reach Vite on `:5173`. Old `https://tender-rings-kick.loca.lt/` is stale — do not keep as the live share URL.

## Formula (pattern, scaled here)

**Adaptive Experience = Shared Understanding + Domain Services + Outer Harness.**

- **Shared Understanding** — the reviewable freeze: official SRS (PDF SoT), today’s daily brief, honesty vocabulary.
- **Domain Services** — restaurant runtime in-repo (React + JSX, Flask, PostgreSQL). Authoritative for reservations and newsletter when PostgreSQL accepts the write. Not this knowledge site.
- **Outer Harness** — guides (`AGENTS.md`, Cursor rules), sensors (GitHub Actions fail-closed), loop (issue → branch → PR), memory (daily briefs), permissions (owner adds collaborators), observability (status words need a probe).

AI may interpret. Domain services decide. Status words are claims; they need a probe.

## Two public surfaces

| Surface | Team | Hostname | Publish path | This session |
|---|---|---|---|---|
| Knowledge (this site) | Café Fausse Knowledge | `knowledge.cafe.artof.link` | GitHub Actions → GitHub Pages | HTTPS GET 200 this session (2026-09-04); HTTP 301 to HTTPS; CNAME `artofdream.github.io`; Let’s Encrypt, expires 2026-11-30 |
| Implementation (restaurant) | Café Fausse App | `cafe.artof.link` | Local React + Flask + PostgreSQL. Hosting future. | CNAME is an AWS ELB, **not** our app. No claim that the restaurant is live there. |

Do not invent other domains. Do not treat a hostname as a live Café Fausse restaurant.

## Honesty

If evidence is missing, write **Unknown**. Closing a task is not a probe. See [Honesty](honesty.md). Do not claim this harness is antifragile.

## On this map (thin)

- [Brief](brief.md) — teammate meeting 2026-09-02 19:00 CET; owner locked 1/3/4; silent demo clips; FS v0.1 vs SRS MVP compare; Friday score-5 section
- [Friday plan](friday-plan.md) — 2026-09-04 19:00 Europe/Berlin; P0/P1/P2; live Knowledge HTTPS vs App local/tunnel vs Future hostname
- [Video script](video-script.md) — ~10 minute beats; clips; scenario menu A–F
- [Talk cuts](presentation.md) — Saturday recording: three ~10 min variants + shared close
- [Slide outline](presentation-sample.md) — 12-slide outline + 8-slide cut
- [Stack](stack.md) — HLD as-is / intended-to-be; GitHub-only CI
- [SRS freeze](srs.md) — FR-1..FR-18, NFR-1..NFR-9
- [Coverage](coverage.md) — each freeze ID: where in-repo, evidence class, why it matters
- [Honesty](honesty.md) — probes, Unknown; live vs local vs Future
- [Future / not-MVP](future.md) — schema notes (including [AWS `cafe_fausse_db` map](future/aws-schema-map.md)), glossary, journal stub, E2E beyond assignment
