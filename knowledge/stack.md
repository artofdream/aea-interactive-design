# Stack

Two surfaces, two teams, two hostnames. GitHub only. This page is Café Fausse as used so far, plus an intended restaurant to-be. It is **not** florist Path B, not 14 hats, not Kafka/BFF, not 3DX Lab.

**Probe date:** 2026-09-02 Europe/Berlin (this session).

## Two hostnames

| Hostname | Job | This session |
|---|---|---|
| `knowledge.cafe.artof.link` | This knowledge map | HTTPS GET **200**. HTTP **301** to HTTPS. TLS VERIFY_OK. CN/SAN match. Let’s Encrypt, expires 2026-11-30. Pages `cname` matches. **`https_enforced=true`**. Cert **approved**. |
| `cafe.artof.link` | Intended restaurant | DNS CNAME → AWS ELB `eu-north-1`. **Not our restaurant.** Do not claim Café Fausse App is live there. |

They do not share a load balancer. This site is not the shop.

## Knowledge surface — Café Fausse Knowledge

Allowlisted markdown under `knowledge/` is built to static HTML (`knowledge/build.py`) and published as **GitHub Pages** (workflow `.github/workflows/knowledge-site.yml`). There is no CMS. No GitLab Pages.

## Implementation surface — Café Fausse App

- **Runtime in-repo on `main` (PRs #9 + timezone #12):** React + JSX (`frontend/`), Flask (`backend/cafe_fausse/`), PostgreSQL (`backend/schema.sql`).
- **MVP:** official SRS only (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9; PDF SoT).
- **Local path (cts-ai; this VM did not reach it):** Vite `http://127.0.0.1:5173`, Flask `:5000`, Docker `cafe-pg`. App this session: Journey **J1–J8 PASS** (DB up); **J9 PASS** (Vite-only viewports + theme; not Flask+Postgres). After the J1–J8 handoff, App reported `cafe-pg` unreachable. See [Coverage](coverage.md).
- **Hosting of `cafe.artof.link`:** future. Not AWS in the restaurant MVP PR.
- Extra features after the SRS belong in [Future](future.md).

## As-is HLD

What is true now: knowledge Pages is live; the restaurant runs locally from `main`; `cafe.artof.link` points at someone else’s ELB.

```mermaid
flowchart TB
  subgraph K["Café Fausse Knowledge — live this session"]
    MD["knowledge/*.md"] --> PY["knowledge/build.py"]
    PY --> GHA["GitHub Actions → GitHub Pages"]
    GHA --> KH["knowledge.cafe.artof.link"]
  end
  KH -.-> P["HTTPS GET 200 · HTTP 301 to HTTPS · TLS VERIFY_OK · CN/SAN match · Let’s Encrypt exp 2026-11-30 · https_enforced=true"]
  subgraph N["Not our restaurant"]
    CAFE["cafe.artof.link"] --> ELB["CNAME → AWS ELB eu-north-1"]
  end
  subgraph L["Local MVP on main — not a public host"]
    VITE["Vite :5173"] --> FLASK["Flask :5000"]
    FLASK --> PG["cafe-pg PostgreSQL"]
  end
```

Static copy (renders if Mermaid JS is blocked): [as-is SVG](assets/hld-as-is.svg).

![Café Fausse as-is: knowledge Pages live, cafe.artof.link is an AWS ELB not our app, local Vite/Flask/Postgres](assets/hld-as-is.svg)

## Intended to-be HLD

Intended, not a live restaurant probe. Knowledge stays GitHub Pages. The restaurant hostname would terminate TLS, then serve React + JSX talking to Flask talking to PostgreSQL. Dashed = not live this session.

```mermaid
flowchart LR
  subgraph K2["Knowledge — already published"]
    PAGES["GitHub Pages"] --> KH2["knowledge.cafe.artof.link"]
  end
  subgraph R["Restaurant — intended, not live"]
    B["Browser"] -.-> HOST["cafe.artof.link hosting future"]
    HOST -.-> RE["React + JSX"]
    RE -.-> API["Flask API"]
    API -.-> DB["PostgreSQL"]
  end
```

Static copy: [to-be SVG](assets/hld-to-be.svg).

![Café Fausse intended to-be: knowledge Pages plus dashed restaurant React Flask Postgres](assets/hld-to-be.svg)

## CI/CD (this repo)

- GitHub Actions only. No GitLab CI, no `.gitlab-ci.yml`, no AWS pipelines here.
- Knowledge: build on pull requests; deploy Pages from `main`.
- App CI (`.github/workflows/ci.yml`): fail closed if `docs/srs.md` / official PDF SHA256 missing; Flask tests against PostgreSQL; frontend test + build.
- Public repository. Assignment collaborator `quantic-grader` is required; **the owner must add that person** — agents must not.
- **Author does not merge their own PR.** MRC **COMMENT** is the role-approve signal (see PR #14 / issue #13). For `artofdream`-authored PRs, `cursor[bot]` may merge after this-run green checks and Bugbot resolve-or-decline.

## Honesty

- `knowledge.cafe.artof.link` was HTTPS GET 200 this session. HTTP GET returned 301 to HTTPS. Pages `https_enforced=true`.
- `cafe.artof.link` is not Café Fausse App.
- Journey **J1–J8 PASS** (cts-ai, DB up); **J9 PASS** (Vite-only viewports + theme). This VM did not reach Vite.
- **NFR-1** / **NFR-2** local Vite notes (56 ms / 32 ms) are **not** an SRS-budget “met.” **NFR-7** is **partial** (Edge all routes + Firefox home; Chrome/Safari Unknown).
- Mentioned tunnel `https://nine-teams-try.loca.lt/` — GET **timed out** this session.
- Do not claim this system is antifragile.
