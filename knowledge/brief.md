# Teammate brief — Wed 2026-09-02 19:00 CET

Thin handoff for the teammate meeting. Not the restaurant. Not a second product.

**Probe date for live claims on this page:** 2026-09-01 Europe/Berlin (this session).

## Demo clips

Silent ~30s demos of the restaurant MVP (Café Fausse App). The tunnel or local stack may be offline; these files are the shareable look. They are not a probe that reservations work on a public host, and they are not Café Fausse at `cafe.artof.link`.

**Home → Menu (~32s)**

<video controls src="clips/01-home-menu.mp4"></video>

**Happy reservation (~33s)**

<video controls src="clips/02-happy-book.mp4"></video>

## Where we are

- Public GitHub repo `artofdream/aea-interactive-design`. Tracker and CI are **GitHub only**. No GitLab.
- **MVP = official SRS only.** PDF is SoT (`docs/official/…SRS.pdf`). Working freeze `docs/srs.md` (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent FR-19 / NFR-10. Freeze data (menu prices, address, hours, owners, awards, reviews) is not to be “improved.”
- Restaurant MVP code is **on `main`** (PRs #9 + timezone #12): React + JSX, Flask, PostgreSQL. Extra ideas stay in [Future](future.md).
- Knowledge site (this map) publishes via GitHub Actions → GitHub Pages.

## Two surfaces

| Surface | Hostname | This session |
|---|---|---|
| Café Fausse Knowledge | `knowledge.cafe.artof.link` | GET **200**; TLS VERIFY_OK; CN/SAN match; Let’s Encrypt, expires 2026-11-30. Pages API: `cname=knowledge.cafe.artof.link`, **`https_enforced=false`** — owner still needs to tick Enforce HTTPS. |
| Café Fausse App | `cafe.artof.link` | DNS CNAME → `aaafeaf0606ec43f5ad23cfe94d6273e-1de430975830beed.elb.eu-north-1.amazonaws.com.` **Not our restaurant.** Do not claim this hostname is live Café Fausse. Hosting is future. |

Local validate on cts-ai (not this agent VM): Vite `http://127.0.0.1:5173`, Flask `:5000`, `cafe-pg` Postgres. A Journey 1–9 UX checklist is described for that machine. **Pass/fail = Unknown** unless someone probes those journeys this session. This agent did not.

## Freeze vs Future

- **In MVP:** the official SRS pages and APIs (Home, Menu, Reservations, About, Gallery, newsletter, 30 tables, fail-closed DB). See [Coverage](coverage.md).
- **Not in MVP:** AWS / `cafe.artof.link` hosting, florist Path B, 14 hats, Kafka/BFF, 3DX Lab, GitLab, invented requirement IDs, claiming the system is antifragile.

## Grade of 5 (Quantic)

A top mark maps to the **official SRS freeze only** (**FR-1..FR-18**, **NFR-1..NFR-9**). No invented IDs. No florist Path B, extra pages, or AWS as “extra credit.” Row-by-row map: [Coverage](coverage.md).

**What the assignment requires**

- Product: Home (**FR-1..FR-4**), Menu (**FR-5**), Reservations (**FR-6..FR-9**), About (**FR-10..FR-11**), Gallery (**FR-12..FR-14**), newsletter (**FR-15..FR-16**), PostgreSQL Customers/Reservations + Flask book/confirm (**FR-17..FR-18**). Freeze data (prices, address, hours, owners, awards, reviews) is SoT.
- Quality: 3s load (**NFR-1**), 2s submits (**NFR-2**), navigable UX (**NFR-3**), brand (**NFR-4**), no double-book (**NFR-5**), honest failures (**NFR-6**), Chrome/Firefox/Safari/Edge (**NFR-7**), responsive (**NFR-8**), modular + documented (**NFR-9**). Stack: React + JSX, Flask, PostgreSQL, Flexbox/Grid. README deploy. `docs/ai-tooling.md`. Public repo. Owner adds `quantic-grader`.

**Already covered**

- Café Fausse App **on `main`** (PRs #9 + timezone #12): every FR row in [Coverage](coverage.md) is `code` / `CI`. **NFR-5**, **NFR-6**, **NFR-8**, **NFR-9** same. Local path (cts-ai, not this VM): Vite `:5173`, Flask `:5000`, `cafe-pg`.
- Café Fausse Knowledge: `GET https://knowledge.cafe.artof.link/` **200** this session; TLS VERIFY_OK; CN/SAN match. This brief and Coverage are the presentation surfaces.
- Clips on this page: silent ~30s shareable look of the local MVP. Not a live restaurant host.

**Still decide / honest Unknowns**

- Journey 1–9 pass/fail: **Unknown** (this VM did not reach cts-ai).
- **NFR-1** / **NFR-2** timings and **NFR-7** browser matrix: **Unknown** (no stopwatch / no four-browser probe this session).
- GitHub Pages **Enforce HTTPS:** Pages API this session still **`https_enforced=false`**. Owner tick.
- `cafe.artof.link` hosting is **Future** (issue #22). That hostname is an AWS ELB, not Café Fausse App.
- `quantic-grader`: collaborator check **404** this session. Owner must add; agents must not.
- PORT / `__main__.py`: **no GitHub issue filed**. Do not invent one in this PR.
- Clips above are the shareable demo, not evidence that a public restaurant host works.

## GitHub loop (do not skip)

One finding → one issue → one branch → one PR against `main`. **The author does not merge their own PR.** Lesson: PR #14 / issue #13.

MRC: a COMMENT is role-approve until a distinct GitHub App identity. Merge gate is GitHub review **`APPROVE` from a login that is not the PR author**. Bugbot comments are a signal, not the gate. `cursor[bot]` may `APPROVE` `artofdream`-authored PRs after a this-run CI probe; `artofdream` may `APPROVE` `cursor[bot]`-authored PRs. Same login cannot self-APPROVE.

Assignment collaborator `quantic-grader` must be added by the **owner**. Agents must not.

## What to decide tomorrow

1. **Owner:** tick Enforce HTTPS (`https_enforced=false` this session).
2. **Owner:** add `quantic-grader` (collaborator GET 404 this session).
3. **Presentation:** [Coverage](coverage.md). Journey 1–9, **NFR-1** / **NFR-2**, **NFR-7** stay **Unknown** until probed. Do not say `cafe.artof.link` is the restaurant (Future, issue #22).
4. **Demo:** the clips on this page, or local Vite/Flask/`cafe-pg` — not the AWS ELB. Clips are shareable look, not a live host.
5. **Scope:** extra ideas go to Future, not a new FR. PORT is not filed; do not batch it here.

## Read next

- [Stack](stack.md) — as-is vs intended HLD
- [Coverage](coverage.md) — every FR/NFR
- [Honesty](honesty.md) — what we will not claim
