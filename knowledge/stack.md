# Stack

Two surfaces, two teams, two hostnames. GitHub only. This page is Café Fausse as used so far, plus an intended restaurant to-be. It is **not** florist Path B, not 14 hats, not Kafka/BFF, not 3DX Lab.

**Probe date:** 2026-09-05 Europe/Berlin (this session) for hostname rows. Journey / NFR evidence stays the 2026-09-02 records on [Coverage](coverage.md).

## Two hostnames

| Hostname | Job | This session |
|---|---|---|
| `knowledge.cafe.artof.link` | This knowledge map | HTTPS GET **200**. HTTP **301** to HTTPS. TLS VERIFY_OK. CN/SAN match. Let’s Encrypt, expires 2026-11-30. Pages `cname` matches. **`https_enforced=true`**. Cert **approved**. |
| `cafe.artof.link` | Prefer live share this session (Lightsail staging) | HTTPS GET **200** (SPA + `/operator` + `/api/health`). TLS CN/SAN `cafe.artof.link`. DNS A `54.165.102.60`. [#57](https://github.com/artofdream/aea-interactive-design/issues/57) weekend window — **not** production forever. Longer-term hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22). |

They do not share a load balancer. This site is not the shop.

## Knowledge surface — Café Fausse Knowledge

Allowlisted markdown under `knowledge/` is built to static HTML (`knowledge/build.py`) and published as **GitHub Pages** (workflow `.github/workflows/knowledge-site.yml`). There is no CMS. No GitLab Pages.

## Implementation surface — Café Fausse App

- **Runtime in-repo on `main` (PRs #9 + timezone #12):** React + JSX (`frontend/`), Flask (`backend/cafe_fausse/`), PostgreSQL (`backend/schema.sql`).
- **MVP:** official SRS only (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9; PDF SoT).
- **Local path (cts-ai; this VM did not reach it):** Vite `http://127.0.0.1:5173`, Flask `:5000`, Docker `cafe-pg`. App this session: Journey **J1–J8 PASS** (DB up); **J9 PASS** (Vite-only viewports + theme; not Flask+Postgres). After the J1–J8 handoff, App reported `cafe-pg` unreachable. See [Coverage](coverage.md).
- **Hosting of `cafe.artof.link`:** Lightsail `cafe-fausse-staging` this weekend ([#57](https://github.com/artofdream/aea-interactive-design/issues/57)): Route53 A, Caddy + Let’s Encrypt, Flask + built SPA, PostgreSQL **on the instance**. AEA RDS untouched. Not a permanent claim. Longer-term hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22). AWS is not in the restaurant MVP PR.
- Extra features after the SRS belong in [Future](future.md). AWS RDS column dump vs local schema: [map + rationale](future/aws-schema-map.md) (no cts-ai required).

## AWS staging facts (this weekend)

Owner-probed implementation, not a second product. This session this agent also GET **200** on `https://cafe.artof.link/` (~0.04s), `/operator` **200**, `/api/health` **200** `{"ok":true}`; DNS A `54.165.102.60`; TLS CN/SAN `cafe.artof.link`, Let’s Encrypt `notAfter=2026-12-04`.

| Fact | Status |
|---|---|
| Lightsail | `cafe-fausse-staging`, us-east-1, `small_3_0` (~$12/mo), IP `54.165.102.60` |
| DNS | Route53 `cafe.artof.link` **A** → that IP, TTL 60. Overrides the `*.artof.link` ELB wildcard. That wildcard is **not** Café Fausse. |
| Edge | Caddy + Let’s Encrypt HTTPS |
| App | Flask + built React SPA on the instance |
| Database | PostgreSQL **on the Lightsail instance**. AEA RDS `aea-pilot-postgres` **untouched**. |
| Prefer share | `https://cafe.artof.link/` (+ `/operator`, `/api/health`) |
| Interim backup | `https://54-165-102-60.sslip.io/` (same IP; not the primary paste) |
| Stale tunnels | `shaky-deer-drive.loca.lt`, `happy-glasses-film`, `real-goats-shop` |
| IAM | `cts` account `737290977112` |
| Window | Weekend / Sunday recording. Tear-down after Sunday unless the owner extends ([#57](https://github.com/artofdream/aea-interactive-design/issues/57)). |
| `/operator` | Read-only recording helper. **Not FR-19.** Not an admin console. |
| Newsletter | Store/register **FR-15** / **FR-16** only. No outbound mailer in the SRS MVP. |
| Permanent hosting | Still [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22). #57 does not close it. |

Static HLD for this cut: [AWS staging SVG](assets/hld-aws-staging.svg).

![Café Fausse AWS staging: Knowledge Pages, Route53 A to Lightsail, Caddy, Flask+SPA, on-box Postgres; AEA RDS and ELB wildcard out of cut](assets/hld-aws-staging.svg)

## As-is HLD

What is true now: knowledge Pages is live; prefer `https://cafe.artof.link/` as the weekend Lightsail staging share (#57) — not production forever; the restaurant code still lives on `main` (local Vite / Flask / `cafe-pg`).

```mermaid
flowchart TB
  subgraph K["Café Fausse Knowledge — live this session"]
    MD["knowledge/*.md"] --> PY["knowledge/build.py"]
    PY --> GHA["GitHub Actions → GitHub Pages"]
    GHA --> KH["knowledge.cafe.artof.link"]
  end
  KH -.-> P["HTTPS GET 200 · HTTP 301 to HTTPS"]
  subgraph N["Staging share this session — not production forever"]
    CAFE["cafe.artof.link"] --> R53["Route53 A TTL 60 → 54.165.102.60"]
    R53 --> CADDY["Caddy + Let's Encrypt"]
    CADDY --> APP["Flask + built React SPA"]
    APP --> BOXPG["PostgreSQL on the instance"]
  end
  subgraph L["Local MVP on main"]
    VITE["Vite :5173"] --> FLASK["Flask :5000"]
    FLASK --> PG["cafe-pg PostgreSQL"]
  end
```

Static copy (renders if Mermaid JS is blocked): [as-is SVG](assets/hld-as-is.svg). Same facts in more detail: [AWS staging SVG](assets/hld-aws-staging.svg).

![Café Fausse as-is: knowledge Pages live, cafe.artof.link is weekend Lightsail staging, local Vite/Flask/Postgres still on main](assets/hld-as-is.svg)

## To-be HLD (permanent vs tear-down)

Knowledge stays GitHub Pages. Weekend staging is **live this session** and may be torn down after Sunday. Permanent restaurant hosting remains [Future #22](https://github.com/artofdream/aea-interactive-design/issues/22) and stays dashed.

```mermaid
flowchart LR
  subgraph K2["Knowledge — already published"]
    PAGES["GitHub Pages"] --> KH2["knowledge.cafe.artof.link"]
  end
  subgraph S["Weekend staging — live now, tear-down unless extended"]
    B["Browser"] --> HOST["cafe.artof.link Lightsail #57"]
    HOST --> RE["React SPA"]
    RE --> API["Flask"]
    API --> DB["Postgres on the instance"]
  end
  subgraph R["Permanent hosting — still Future #22"]
    HOST -.-> FUT["Dashed on purpose · not production forever"]
  end
```

Static copy: [to-be SVG](assets/hld-to-be.svg).

![Café Fausse to-be: knowledge Pages plus weekend staging vs dashed permanent hosting](assets/hld-to-be.svg)

## CI/CD (this repo)

- GitHub Actions only. No GitLab CI, no `.gitlab-ci.yml`, no AWS pipelines here.
- Knowledge: build on pull requests; deploy Pages from `main`.
- App CI (`.github/workflows/ci.yml`): fail closed if `docs/srs.md` / official PDF SHA256 missing; Flask tests against PostgreSQL; frontend test + build.
- Public repository. Assignment collaborator `quantic-grader` is required; **the owner must add that person** — agents must not.
- **Author does not merge their own PR.** MRC **COMMENT** is the role-approve signal (see PR #14 / issue #13). For `artofdream`-authored PRs, `cursor[bot]` may merge after this-run green checks and Bugbot resolve-or-decline.

## Honesty

- `knowledge.cafe.artof.link` was HTTPS GET 200 this session. HTTP GET returned 301 to HTTPS. Pages `https_enforced=true`.
- Prefer `https://cafe.artof.link/` as the weekend Lightsail staging share (#57). Route53 A overrides the `*.artof.link` ELB wildcard; that wildcard is **not** Café Fausse. Postgres is on the instance. AEA RDS untouched. Not production forever. Longer-term hosting stays #22.
- Journey **J1–J8 PASS** (cts-ai, DB up); **J9 PASS** (Vite-only viewports + theme). This VM did not reach Vite.
- **NFR-1** / **NFR-2** local Vite notes (56 ms / 32 ms) are **not** an SRS-budget “met.” **NFR-7** is **partial** (Edge all routes + Firefox home; Chrome/Safari Unknown).
- Mentioned tunnel `https://nine-teams-try.loca.lt/` — GET **timed out** this session.
- Do not claim this system is antifragile.
