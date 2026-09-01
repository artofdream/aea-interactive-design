# Teammate brief — Wed 2026-09-02 19:00 CET

Thin handoff for the teammate meeting. Not the restaurant. Not a second product.

**Probe date for live claims on this page:** 2026-09-01 Europe/Berlin (this session).

## Demo clips

Silent ~30s demos of the restaurant MVP (Café Fausse App). The tunnel or local stack may be offline; these files are the shareable look. They are not a probe that reservations work on a public host, and they are not Café Fausse at `cafe.artof.link`.

**Home → Menu (~32s)**

<video controls src="clips/01-home-menu.mp4"></video>

**Happy reservation (~33s)**

<video controls src="clips/02-happy-book.mp4"></video>

## Course grade 5 — covered vs decide

1. **What a grade of 5 needs.** Official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). PDF in `docs/official/` is SoT; working freeze `docs/srs.md`. Do not invent FR-19 / NFR-10. Freeze data is not to be “improved.” Extra ideas are Future, not extra credit.

2. **Already covered.** Restaurant MVP **on `main`** (PRs #9 + #12). Knowledge live HTTPS: `GET https://knowledge.cafe.artof.link/` **200** this session (TLS VERIFY_OK; CN/SAN match). [Coverage](coverage.md) maps every freeze ID. Demo clips on this brief (shareable look, not a live restaurant host). [Stack](stack.md) HLD as-is vs intended-to-be.

3. **Still decide / focus.** GitHub Pages **Enforce HTTPS** still **`https_enforced=false`** (Pages API this session) — owner tick. Journey 1–9 pass/fail: **Unknown** until probed. `cafe.artof.link` hosting is **Future** (issue #22); that hostname is an AWS ELB, not our restaurant. Owner adds `quantic-grader` (agents must not). **NFR-1** / **NFR-2** timing claims stay **Unknown** without a measured probe this session.

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
