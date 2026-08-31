# Stack

Two surfaces. GitHub only. DNS and Pages enablement are **owner steps** — this page documents names; it does not configure them.

## Knowledge surface (this site)

- **Intended hostname:** `knowledge.cafe.artof.link`
- **Publish path:** GitHub Actions builds Markdown → HTML and deploys **GitHub Pages**
- **Live URL:** **Unknown** until a GET probe after the owner enables Pages (source: GitHub Actions) and DNS
- **What it is:** formula, stack, SRS freeze, honesty, plus a labeled Future section
- **What it is not:** the restaurant, a CMS, GitLab Pages

## Implementation surface (later)

- **Intended hostname:** `cafe.artof.link`
- **Runtime (intended, not live):** React + JSX front-end, Flask back-end, PostgreSQL
- **MVP:** reconstructed SRS only (`docs/srs.md`, FR-1..FR-18, NFR-1..NFR-9)
- **Live URL:** **Unknown** — restaurant app is not in this cut; no GET probe
- Extra features after the SRS belong in [Future](future.md), not in the first app cut

## CI/CD (this repo)

- GitHub Actions only. No GitLab CI, no `.gitlab-ci.yml`.
- Knowledge-site workflow: build on pull requests; deploy Pages from `main` once Pages is enabled.
- Placeholder CI: **fail closed** if `docs/srs.md` is missing.
- Private repository. Assignment collaborator `quantic-grader` is required; **the owner must add that person** — agents must not.

## Unknown until probed

`knowledge.cafe.artof.link` and `cafe.artof.link` are names on this map. They are not evidence that either site is live.
