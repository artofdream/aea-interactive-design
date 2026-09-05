# Quantic deliverable handoff

**In plain English:** This is the one-page pack to paste or open when someone asks “where is the assignment?” It is **not** the restaurant and **not** the official Quantic dashboard. Sister pages stay complete. This page links out.

Grade floor = official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent **FR-19**. Do not say **NFR-1** / **NFR-2** are met.

Every section below is filled with what is known **now**. Rows that are not done yet stay **Unknown** / to-be-filled. Do not invent a submit video, a Sunday agenda, a speaker lock, or an outbound mailer.

## 1. Links (known now)

| What | URL | Known now |
|---|---|---|
| GitHub repo | [artofdream/aea-interactive-design](https://github.com/artofdream/aea-interactive-design) | Tracker + CI are GitHub only. No GitLab. Public repo. |
| Restaurant app | [https://cafe.artof.link/](https://cafe.artof.link/) | Prefer this share. Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) — **not** forever production. Health: `/api/health`. Operator: `/operator`. Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22). |
| Knowledge map | [https://knowledge.cafe.artof.link/](https://knowledge.cafe.artof.link/) | GitHub Pages. This session HTTPS **GET 200**. |
| Quantic hub | [https://knowledge.cafe.artof.link/quantic.html](https://knowledge.cafe.artof.link/quantic.html) | Delivery / MSAIE navigation only (#74 / #79). |

Interim App backup (same host, not the primary paste): `https://54-165-102-60.sslip.io/`. Old tunnels (`shaky-deer-drive`, `happy-glasses-film`, `real-goats-shop`) are **stale**.

Live Pages URLs for pages that land only after this PR merges (`/glossary.html`, `/meeting-*.html`, `/quantic-handoff.html`) stay **Unknown** until a GET after deploy.

## 2. Sources (known now)

- **Official SRS PDF (source of truth):** `docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf` (SHA256 `6075e5964601aa3e3c7a3085c626eab820e3d733a396b00e20339cfdc77a9d82`). Fetched 2026-08-31 HTTP 200. CI fails closed if missing or the hash mismatches.
- **Working freeze:** [SRS freeze](srs.md) and full copy `docs/srs.md` ([srs-full.html](srs-full.html)). **FR-1..FR-18**, **NFR-1..NFR-9** only.
- **Evidence map:** [Coverage](coverage.md) — each freeze ID, where it lives in-repo, evidence class (code / CI / local UX / **Unknown**).
- **Honesty ledger:** [Honesty](honesty.md) — a status word needs a probe **this session** or stays **Unknown**.
- **Must-film page (live on the map once built):** [Must-film shots](must-film-shots.md) — four camera beats. Committed on `main` via #83 / PR #84. Live `https://knowledge.cafe.artof.link/must-film-shots.html` was **Unknown** until a GET after that deploy; re-probe next session or write **Unknown**.
- **Short labels:** [Glossary](glossary.md).

## 3. Coverage vs the talk track (known now)

**Coverage** is the grade-floor map. Open it when a grader asks “where is FR-9?” or “is NFR-6 tested?” It is not a slide deck.

**Presentation / video-script / must-film** is the talk track (exists now as drafts):

- [Talk cuts](presentation.md) — three ~10 min variants (A layers, B architecture, C coding) plus a shared open and close. **Which cut is locked** is **Unknown** / to-be-filled.
- [Slide outline](presentation-sample.md) — 12-slide outline + 8-slide cut. Friday deck, not a second talk track.
- [Video script](video-script.md) — timed beats + scenario menu A–F. Zoom dry-run v2 on that page is **PROTOTYPE**.
- [Must-film shots](must-film-shots.md) — four camera beats on `cafe.artof.link`: (1) happy book → `/operator`, (2) newsletter → newsletter-only, (3) full-book **HTTP 409**, (4) NFR-6 via Coverage/CI.

The Zoom dry-run is **not** the Quantic submission. Do not submit it until a **live** must-film pass **plus voice** exists. That final submit cut is **Unknown** / to-be-filled.

| Track | Job (known) | Not (honest) |
|---|---|---|
| [Coverage](coverage.md) | FR/NFR evidence map (grade floor) | A claim that every NFR is met |
| Talk / video / must-film | What to say and film; must-film page exists; dry-run is **PROTOTYPE** | A finished Quantic upload |

## 4. Honesty (known now — say out loud)

- **`cafe.artof.link` is weekend Lightsail staging** (#57). Not production forever. Staging stays up until the owner asks to tear it down. Monday **2026-09-08 16:00 Europe/Berlin** is evaluate-only (not auto tear-down).
- **NFR-1** / **NFR-2** (3s page load / 2s form submit) stay **Unknown** as SRS-budget claims. Local Vite notes (56 ms / 32 ms) are not “met.”
- **NFR-7** is **partial** (Edge + Firefox home; Chrome / Safari **Unknown**). Not a four-browser pass.
- **`/operator` is not FR-19.** Read-only recording helper (PR #58 / issue #54). Prefer `https://cafe.artof.link/operator`. Not an admin console.
- **Newsletter** is **FR-15** / **FR-16** store/register only. Outbound mail is **not in the SRS MVP** — **Unknown** as a product feature because it is out of freeze, not because we forgot to look.
- Journey **J1–J8 PASS** was local cts-ai with the DB up (2026-09-02). **J9 PASS** is Vite-only. Neither is a public-host write probe.
- Whether Quantic graders need the host up for video evaluation remains **Unknown** until the owner shares correspondence.

## 5. Still Unknown / to-be-filled (sections kept on purpose)

Do not invent these. The section exists so a grader sees the gap instead of a guessed yes.

| Item | Status now |
|---|---|
| Final Quantic submission video (live must-film + voice) | **Unknown** / to-be-filled. Dry-run on the [Video script](video-script.md) is **PROTOTYPE** only. |
| Locked talk cut (A / B / C) | **Unknown** / to-be-filled. All three drafts live on [Talk cuts](presentation.md). |
| Speaker names / who records | **Unknown** / to-be-filled. |
| Sunday meeting notes and clock | **Unknown** / to-be-filled. Page exists: [Sunday](meeting-sunday.md). |
| Outbound newsletter mail | **Not in the SRS MVP.** Do not claim a mailer. |
| Permanent `cafe.artof.link` hosting | Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22). Staging does not close it. |
| Collaborator `quantic-grader` | Owner step. An agent must not add that person. |
| Live GET of this handoff page on Pages | **Unknown** until after merge / deploy. |

## Meeting packs (known dates + Sunday gap)

- [Wednesday](meeting-wednesday.md) — 2026-09-02 19:00 Europe/Berlin; owner locked 1, 3, 4.
- [Friday](meeting-friday.md) — 2026-09-04 19:00 Europe/Berlin; score-5 / tech access.
- [Saturday](meeting-saturday.md) — 2026-09-05 19:00 Europe/Berlin / ~13:00 America/New_York; recording.
- [Sunday](meeting-sunday.md) — **Unknown** / to-be-filled (no invented agenda).

Back to the [Quantic / MSAIE](quantic.md) hub.
