# Quantic deliverable handoff

**In plain English:** This is the one-page pack to paste or open when someone asks “where is the assignment?” It is **not** the restaurant and **not** the official Quantic dashboard. Sister pages stay complete. This page links out.

Grade floor = official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). Do not invent **FR-19**. **NFR-1** / **NFR-2** are **met** on the A36 Brave broadband probes (**466 ms** / **233 ms**, [#124](https://github.com/artofdream/aea-interactive-design/pull/124) / [#126](https://github.com/artofdream/aea-interactive-design/pull/126)). **NFR-7** stays **Partial**. Do not claim four browsers.

Every section below is filled with what is known **now**. Rows that are not done yet stay **Unknown** / to-be-filled. Do not invent a submit video, a Hiren B-vs-C lock, a voice-over, or an outbound mailer.

## 1. Links (known now)

| What | URL | Known now |
|---|---|---|
| GitHub repo | [artofdream/aea-interactive-design](https://github.com/artofdream/aea-interactive-design) | Tracker + CI are GitHub only. No GitLab. Public repo. Issues → Slack; Claude addresses. |
| Restaurant app | [https://cafe.artof.link/](https://cafe.artof.link/) | Prefer this share. Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) — **not** forever production. Health: `/api/health`. Operator: `/operator`. Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22). |
| Knowledge map | [https://knowledge.cafe.artof.link/](https://knowledge.cafe.artof.link/) | GitHub Pages. This session HTTPS **GET 200**. |
| Quantic hub | [https://knowledge.cafe.artof.link/quantic.html](https://knowledge.cafe.artof.link/quantic.html) | Delivery / MSAIE navigation only (#74 / #79). |
| To-be (beyond MVP) | [To-be](to-be.md) | **Not the grade floor.** Parked Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22) / [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38). Sister page [Future](future.md) stays complete. |

Interim App backup (same host, not the primary paste): `https://54-165-102-60.sslip.io/`. Old tunnels (`shaky-deer-drive`, `happy-glasses-film`, `real-goats-shop`) are **stale**.

Live Pages URLs for pages that land only after this PR merges (`/glossary.html`, `/meeting-*.html`, `/quantic-handoff.html`) stay **Unknown** until a GET after deploy.

## 2. Sources / PDF refs (known now)

- **Official SRS PDF (source of truth):** [`docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf`](https://github.com/artofdream/aea-interactive-design/blob/main/docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf) (SHA256 `6075e5964601aa3e3c7a3085c626eab820e3d733a396b00e20339cfdc77a9d82`). Fetched 2026-08-31 HTTP 200. CI fails closed if missing or the hash mismatches.
- **Working freeze:** [SRS freeze](srs.md) and full copy `docs/srs.md` ([srs-full.html](srs-full.html)). **FR-1..FR-18**, **NFR-1..NFR-9** only.
- **Evidence map:** [Coverage](coverage.md) — each freeze ID, where it lives in-repo, evidence class (code / CI / local UX / **Unknown**).
- **Honesty ledger:** [Honesty](honesty.md) — a status word needs a probe **this session** or stays **Unknown**.
- **Must-film page:** [Must-film shots](must-film-shots.md) — four camera beats. Committed on `main` via #83 / PR #84. Live `https://knowledge.cafe.artof.link/must-film-shots.html` was **Unknown** until a GET after that deploy; re-probe next session or write **Unknown**.
- **Short labels:** [Glossary](glossary.md).
- **UX compliance:** Café Fausse App mobile ≤767px — [#91](https://github.com/artofdream/aea-interactive-design/issues/91) / PR #93. Knowledge mobile ≤767px — [#92](https://github.com/artofdream/aea-interactive-design/issues/92) / PR #94. **NFR-1** / **NFR-2** **met** cites stay on [Coverage](coverage.md) (A36 Brave broadband **466 ms** / **233 ms**). Do **not** claim four-browser **NFR-7**.

## 3. Coverage vs the talk track (known now)

**Coverage** is the grade-floor map. Open it when a grader asks “where is FR-9?” or “is NFR-6 tested?” It is not a slide deck.

**Meghna first:** [Meghna materials](meghna-materials.md) (index + silent **PROTOTYPE**) · [Meghna cafe demo](meghna-cafe-demo.md) · [Meghna VO draft](meghna-voiceover.md). Spoken / VO = **plain English only**. FR/NFR IDs stay in supporting notes (and Coverage). Recorded teammate VO is **Unknown**. Supporting docs target **9:00 America/New_York** on 2026-09-06.

**Parts 3–5 rehearsal (after Meghna):** [Parts 3–5 materials](parts-345-materials.md) (index + silent **PROTOTYPEs** + **PROTOTYPE TTS** VO) · [VO notes](parts-345-vo-notes.md) · [Part 3 script](part3-variant-b-script.md) / [VO](part3-variant-b-voiceover.md) · [Part 4 script](part4-variant-c-script.md) / [VO](part4-variant-c-voiceover.md) · [Part 5 script](part5-shared-close-script.md) / [VO](part5-shared-close-voiceover.md). Technical scripts may use FR/NFR IDs. Silent and TTS mp4s are **PROTOTYPE** / rehearsal — not Quantic submit. **PROTOTYPE TTS** is machine voice (`en-US-GuyNeural`), not teammate VO. Recorded teammate VO **Unknown**. Do not invent the Hiren B vs C pick.

**Locked Saturday VIDEO (~10 min)** — owner notes 2026-09-05 / [#97](https://github.com/artofdream/aea-interactive-design/issues/97). Not “pick one of A / B / C.”

1. Team + ID verification — ~30s — shared
2. Website demo `https://cafe.artof.link/` — ~3 min — **Meghna** — Home, Gallery, Menu, Reservations — pack: [Meghna demo](meghna-cafe-demo.md)
3. Architecture + Diagram (**Variant B**) — ~3 min — **Claude or Hiren** — [Part 3 script](part3-variant-b-script.md)
4. Coding rationale (**Variant C**) — ~3 min — **Claude or Hiren** — [Part 4 script](part4-variant-c-script.md)
5. Shared close — shared — [Part 5 script](part5-shared-close-script.md)

Hiren chooses B vs C; Claude takes the other. That **speaker** lock is **Unknown** / to-be-filled. Voice-over is **TBD**. Meghna’s 3-minute pack: [Meghna demo](meghna-cafe-demo.md). Per-part pack (script + prototype video + VO TBD) lives on [Saturday](meeting-saturday.md). Supporting docs target **9:00 America/New_York** on 2026-09-06.

Sister talk-track pages (stay complete):

- [Meghna materials](meghna-materials.md) — index + silent **PROTOTYPE** clip.
- [Meghna demo](meghna-cafe-demo.md) — 3-min live walk (spoken = plain English).
- [Meghna VO draft](meghna-voiceover.md) — plain-English voice-over. Recorded take **Unknown**.
- [Parts 3–5 materials](parts-345-materials.md) — Architecture / Coding / shared-close index + silent **PROTOTYPEs** + **PROTOTYPE TTS** VO. [VO notes](parts-345-vo-notes.md). Recorded teammate VO **Unknown**.
- [Part 3 script](part3-variant-b-script.md) · [Part 3 VO](part3-variant-b-voiceover.md)
- [Part 4 script](part4-variant-c-script.md) · [Part 4 VO](part4-variant-c-voiceover.md)
- [Part 5 script](part5-shared-close-script.md) · [Part 5 VO](part5-shared-close-voiceover.md)
- [Talk cuts](presentation.md) — Variant B and Variant C as 3-min sources; Variant A remains a draft. Shared open / close stay here.
- [Slide outline](presentation-sample.md) — 12-slide outline + 8-slide cut. Friday deck, not a second talk track.
- [Video script](video-script.md) — timed beats + scenario menu A–F. Zoom dry-run v2 on that page is **PROTOTYPE**.
- [Must-film shots](must-film-shots.md) — four camera beats on `cafe.artof.link`: (1) happy book → `/operator`, (2) newsletter → newsletter-only, (3) full-book **HTTP 409**, (4) NFR-6 via Coverage/CI.

The Zoom dry-run is **not** the Quantic submission. Do not submit it until a **live** must-film pass **plus voice** exists. That final submit cut is **Unknown** / to-be-filled.

| Track | Job (known) | Not (honest) |
|---|---|---|
| [Coverage](coverage.md) | FR/NFR evidence map (grade floor) | A claim that every NFR is met |
| Talk / video / must-film | Locked five-part structure; must-film page exists; dry-run is **PROTOTYPE** | A finished Quantic upload; a Hiren B-vs-C lock; a voice-over |

## 4. Honesty (known now — say out loud)

- **`cafe.artof.link` is weekend Lightsail staging** (#57). Not production forever. Staging stays up until the owner asks to tear it down. Monday **2026-09-08 16:00 Europe/Berlin** is evaluate-only (not auto tear-down).
- **NFR-1** is **met** — A36 Brave broadband cold Home **466 ms** ([#124](https://github.com/artofdream/aea-interactive-design/pull/124)). **NFR-2** is **met** — reservation submit **233 ms** ([#126](https://github.com/artofdream/aea-interactive-design/pull/126)). Local Vite notes (56 ms / 32 ms) and the ROG Wi‑Fi note are **not** those **met** cites.
- **NFR-7** is **Partial**. Not a four-browser pass. Full matrix on [Coverage](coverage.md) / [Honesty](honesty.md).
- **`/operator` is not FR-19.** Read-only recording helper (PR #58 / issue #54). Prefer `https://cafe.artof.link/operator`. Not an admin console.
- **Newsletter** is **FR-15** / **FR-16** store/register only. Outbound mail is **not in the SRS MVP** — **Unknown** as a product feature because it is out of freeze, not because we forgot to look.
- Journey **J1–J8 PASS** was local cts-ai with the DB up (2026-09-02). **J9 PASS** is Vite-only. Neither is a public-host write probe.
- Whether Quantic graders need the host up for video evaluation remains **Unknown** until the owner shares correspondence.

## 5. Still Unknown / to-be-filled (sections kept on purpose)

Do not invent these. The section exists so a grader sees the gap instead of a guessed yes.

| Item | Status now |
|---|---|
| Final Quantic submission video (live must-film + voice) | **Unknown** / to-be-filled. Dry-run on the [Video script](video-script.md) is **PROTOTYPE** only. |
| Hiren: Variant B vs Variant C (Claude takes the other) | **Unknown** / to-be-filled. Structure is locked; **speaker** names for B/C are not. |
| Voice-over (teammate recorded) | **TBD** on every part. **PROTOTYPE TTS** on [materials](parts-345-materials.md) is not that. |
| Optional Claude advance recording for eval | **Unknown** until a file exists. Not the submit video. |
| Sunday meeting **start** clock | **Unknown** / to-be-filled. Known job: ends with a recording; docs target **9:00 America/New_York** on 2026-09-06. Page: [Sunday](meeting-sunday.md). |
| Outbound newsletter mail | **Not in the SRS MVP.** Do not claim a mailer. |
| Permanent `cafe.artof.link` hosting | Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22). Staging does not close it. |
| Collaborator `quantic-grader` | Owner step. An agent must not add that person. |
| Live GET of this handoff page on Pages | **Unknown** until after merge / deploy. |

## Meeting packs

- [Wednesday](meeting-wednesday.md) — 2026-09-02 19:00 Europe/Berlin; owner locked 1, 3, 4.
- [Friday](meeting-friday.md) — 2026-09-04 19:00 Europe/Berlin; score-5 / tech access.
- [Saturday](meeting-saturday.md) — 2026-09-05 19:00 Europe/Berlin / ~13:00 America/New_York; locked five-part VIDEO (#97).
- [Sunday](meeting-sunday.md) — 2026-09-06; ends with a recording; supporting docs target **9:00 America/New_York**; remaining gaps stay **Unknown** / to-be-filled.

Back to the [Quantic / MSAIE](quantic.md) hub.
