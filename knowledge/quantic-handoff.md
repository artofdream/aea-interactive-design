# Quantic deliverable handoff

**In plain English:** This is the one-page pack to paste or open when someone asks “where is the assignment?” It is **not** the restaurant and **not** the official Quantic dashboard. Sister pages stay complete. This page links out.

Grade floor = official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent **FR-19**. Do not say **NFR-1** / **NFR-2** are met.

## 1. Links

| What | URL | This session |
|---|---|---|
| GitHub repo | [artofdream/aea-interactive-design](https://github.com/artofdream/aea-interactive-design) | Tracker + CI are GitHub only. No GitLab. |
| Restaurant app | [https://cafe.artof.link/](https://cafe.artof.link/) | Prefer this share. Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) — **not** forever production. Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22). |
| Knowledge map | [https://knowledge.cafe.artof.link/](https://knowledge.cafe.artof.link/) | GitHub Pages. This session HTTPS **GET 200**. |
| Quantic hub | [https://knowledge.cafe.artof.link/quantic.html](https://knowledge.cafe.artof.link/quantic.html) | Delivery / MSAIE navigation only. |

Interim App backup (same host, not the primary paste): `https://54-165-102-60.sslip.io/`. Old tunnels (`shaky-deer-drive`, `happy-glasses-film`, `real-goats-shop`) are **stale**.

## 2. Sources

- **Official SRS PDF (source of truth):** `docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf` (SHA256 `6075e5964601aa3e3c7a3085c626eab820e3d733a396b00e20339cfdc77a9d82`).
- **Working freeze:** [SRS freeze](srs.md) and full copy `docs/srs.md` ([srs-full.html](srs-full.html)). **FR-1..FR-18**, **NFR-1..NFR-9** only.
- **Evidence map:** [Coverage](coverage.md) — each freeze ID, where it lives in-repo, evidence class.
- **Honesty ledger:** [Honesty](honesty.md) — a status word needs a probe **this session** or stays **Unknown**.
- **Short labels:** [Glossary](glossary.md).

## 3. Coverage vs the talk track

**Coverage** is the grade-floor map. Open it when a grader asks “where is FR-9?” or “is NFR-6 tested?” It is not a slide deck.

**Presentation / video-script / must-film** is the talk track:

- [Talk cuts](presentation.md) — three ~10 min variants + shared open/close.
- [Slide outline](presentation-sample.md) — 12-slide outline + 8-slide cut.
- [Video script](video-script.md) — timed beats + scenario menu A–F. Zoom dry-run v2 is **PROTOTYPE**.
- [Must-film shots](must-film-shots.md) — four camera beats on `cafe.artof.link`.

The Zoom dry-run is **not** the Quantic submission. Do not submit it until a **live** must-film pass **plus voice** exists. That final submit cut is **Unknown** / to-be-filled.

| Track | Job | Not |
|---|---|---|
| [Coverage](coverage.md) | FR/NFR evidence map (grade floor) | A claim that every NFR is met |
| Talk / video / must-film | What to say and film | A finished Quantic upload |

## 4. Honesty (say out loud)

- **`cafe.artof.link` is weekend Lightsail staging** (#57). Not production forever. Staging stays up until the owner asks to tear it down. Monday **2026-09-08 16:00 Europe/Berlin** is evaluate-only (not auto tear-down).
- **NFR-1** / **NFR-2** (3s page load / 2s form submit) stay **Unknown** as SRS-budget claims. Local Vite notes are not “met.”
- **NFR-7** is **partial** (Edge + Firefox home; Chrome / Safari **Unknown**). Not a four-browser pass.
- **`/operator` is not FR-19.** Read-only recording helper (PR #58 / issue #54). Not an admin console.
- **Newsletter** is **FR-15** / **FR-16** store/register only. No outbound mailer in this MVP.
- Journey **J1–J8 PASS** was local cts-ai with the DB up. **J9 PASS** is Vite-only. Neither is a public-host write probe.
- Whether Quantic graders need the host up for video evaluation remains **Unknown** until the owner shares correspondence.

## 5. Still Unknown / to-be-filled

Do not invent these. Fill the row when evidence exists.

| Item | Status now |
|---|---|
| Final Quantic submission video (live must-film + voice) | **Unknown** / to-be-filled. Dry-run is **PROTOTYPE** only. |
| Locked talk cut (A / B / C) and speaker names | **Unknown** / to-be-filled. Variants live on [Talk cuts](presentation.md). |
| Sunday meeting notes and clock | **Unknown** / to-be-filled. See [Sunday](meeting-sunday.md). |
| Outbound newsletter mail | **Not in the SRS MVP.** Do not claim a mailer. |
| Permanent `cafe.artof.link` hosting | Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22). Staging does not close it. |
| Collaborator `quantic-grader` | Owner step. An agent must not add that person. |

## Meeting packs

- [Wednesday](meeting-wednesday.md) — 2026-09-02 19:00 Europe/Berlin
- [Friday](meeting-friday.md) — 2026-09-04 19:00 Europe/Berlin
- [Saturday](meeting-saturday.md) — 2026-09-05 19:00 Europe/Berlin / ~13:00 America/New_York
- [Sunday](meeting-sunday.md) — placeholder

Back to the [Quantic / MSAIE](quantic.md) hub.
