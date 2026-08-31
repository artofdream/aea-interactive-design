# Stack

Two surfaces, two teams. GitHub only. DNS and Pages enablement are **owner steps** — this page documents names; it does not configure them. **AWS is not in this PR.**

## Knowledge surface — Café Fausse Knowledge

- **Intended hostname:** `knowledge.cafe.artof.link`
- **Publish path:** GitHub Actions builds Markdown → HTML and deploys **GitHub Pages**
- **Live URL:** **Unknown** until a GET **this session** after the owner enables Pages (source: GitHub Actions) and DNS
- **What it is:** formula, stack, SRS freeze, honesty, plus a labeled Future section
- **What it is not:** the restaurant, a CMS, GitLab Pages, AWS

## Implementation surface — Café Fausse App (later)

- **Intended hostname:** `cafe.artof.link`
- **Runtime (intended, not live):** React + JSX front-end, Flask back-end, PostgreSQL
- **MVP:** official SRS only (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9; PDF SoT)
- **Hosting:** future. Not AWS in this foundation PR. Owner skipped AWS re-auth.
- **Live URL:** **Unknown** — restaurant app is not in this cut; no GET this session
- Extra features after the SRS belong in [Future](future.md), not in the first app cut

## CI/CD (this repo)

- GitHub Actions only. No GitLab CI, no `.gitlab-ci.yml`, no AWS pipelines here.
- Knowledge-site workflow: build on pull requests; deploy Pages from `main` once Pages is enabled.
- Placeholder CI: **fail closed** if `docs/srs.md` is missing or official PDF/zip SHA256 does not match the freeze.
- Private repository. Assignment collaborator `quantic-grader` is required; **the owner must add that person** — agents must not.
- **Author does not merge their own PR.**

## Unknown until probed this session

`knowledge.cafe.artof.link` and `cafe.artof.link` are names on this map. They are not evidence that either site is live.
