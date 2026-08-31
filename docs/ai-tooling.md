# AI tooling log

Required for the Quantic assignment. This file records tools and usage for the Café Fausse restaurant implementation (MVP = official SRS freeze in `docs/srs.md`, FR-1..FR-18 and NFR-1..NFR-9). Do not invent FR/NFR IDs in this log.

## Tools

| Tool | Use |
|---|---|
| Cursor Cloud Agent (Grok 4.6) | Implement the restaurant MVP on `artofdream/aea-interactive-design` from the official SRS |
| Official SRS PDF | Source of truth for pages, facts, menu prices, reservation rules, and NFRs |
| `docs/srs.md` | Working ID freeze (cite IDs from here only) |
| GitHub Actions | App CI (pytest + React build) plus existing SRS SHA256 and knowledge-site workflows |
| GitHub CLI (`gh`) | Read-only: issues, PR #1 history. PRs opened with the repo’s PR tool, not `gh pr create` |
| PostgreSQL 16 + Flask + React (JSX) / Vite | Assigned stack. Local run only in this PR |

## What was asked

Implement the restaurant app only: Home, Menu, Reservations, About Us, Gallery, plus contact and newsletter. Flask API + PostgreSQL for reservations (30 tables, random free table, fail closed) and newsletter storage. Official images first; supplemental labeled not-official. README and this file. GitHub Actions for the app. No GitLab. No AWS. Do not change the knowledge site. Do not work issues #2 / #3 / #4. Do not claim `cafe.artof.link` is live. Open one PR; do not merge.

## Usage notes

- Application code was written in this repository. Other students’ Café Fausse / florist / AEA / 3DX application code was not copied.
- Menu prices, address, hours, owners, awards, and reviews were taken from the SRS freeze, not “improved.”
- Status words stay probe-or-Unknown. Local tests are evidence for local behavior only. Public `cafe.artof.link` remains **Unknown**.
- AI suggestions that invented requirement IDs, added AWS, or treated a hostname as a live deploy were discarded.
