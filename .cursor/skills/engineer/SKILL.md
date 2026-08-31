---
name: engineer
description: Guard later React/Flask/PostgreSQL and GitHub Actions. Use when planning or implementing the restaurant, CI, or hosting — not to build the app in the foundation cut.
---

# Engineer

Café Fausse App implements the restaurant **later**: React + JSX, Flask, PostgreSQL. MVP = SRS only. Cite FR/NFR; do not invent IDs.

- This foundation PR does **not** implement reservation/newsletter Flask or React pages.
- Knowledge publish path: GitHub Actions → GitHub Pages. No GitLab CI. No AWS in this PR.
- `cafe.artof.link` hosting is future. Do not treat a hostname as a live deploy.
- Fail closed when the app exists: missing DB, full book (30 tables, FR-9), timeout = honest no.
- Course images: official zip is four webps; extras in `assets/images/` are not SoT.
