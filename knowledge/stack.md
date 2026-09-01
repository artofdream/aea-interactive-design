# Stack

Two surfaces, two teams. GitHub only. DNS and Pages enablement are **owner steps** — this page documents names; it does not configure them. **AWS is not in the restaurant MVP.**

## Knowledge surface — Café Fausse Knowledge

- **Intended hostname:** `knowledge.cafe.artof.link`
- **Publish path:** GitHub Actions builds Markdown → HTML and deploys **GitHub Pages**
- **Live URL this session:** **HTTPS GET 200** at `https://knowledge.cafe.artof.link/` (TLS CN / SAN match). Pages API: `https_enforced` **false**, certificate `approved` (expires 2026-11-30).
- **What it is:** formula, stack, SRS freeze, [coverage](coverage.md), [teammate brief](teammate-brief.md), honesty, plus a labeled Future section
- **What it is not:** the restaurant, a CMS, GitLab Pages, AWS

## Implementation surface — Café Fausse App

- **Intended hostname:** `cafe.artof.link`
- **Runtime (in-repo on `main`, merged PRs #9 and #12):** React + JSX front-end, Flask back-end, PostgreSQL
- **Local (README):** Vite `http://127.0.0.1:5173`, Flask `http://127.0.0.1:5000`, Postgres `cafe-pg`. **This session:** those ports were not listening here.
- **MVP:** official SRS only (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9; PDF SoT)
- **Hosting:** future. Not AWS in the restaurant MVP. This session `cafe.artof.link` CNAME targets an AWS ELB hostname that **did not resolve** — not our live app.
- Extra features after the SRS belong in [Future](future.md), not in the first app cut

## CI/CD (this repo)

- GitHub Actions only. No GitLab CI, no `.gitlab-ci.yml`, no AWS pipelines here.
- Knowledge-site workflow: build on pull requests; deploy Pages from `main`.
- App CI: fail closed if `docs/srs.md` is missing or official PDF/zip SHA256 does not match the freeze; Flask tests against PostgreSQL; frontend test + build.
- Public repository. Assignment collaborator `quantic-grader` is required; **the owner must add that person** — agents must not. This session collaborators listed `artofdream` only.
- **Author does not merge their own PR.**

## Unknown until probed this session

`cafe.artof.link` is a documented name plus a dangling ELB CNAME. It is not evidence that Café Fausse App is live. Local Vite/Flask/Postgres need a GET **this session** or stay Unknown.
