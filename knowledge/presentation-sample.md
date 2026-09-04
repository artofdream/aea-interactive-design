# Presentation sample

Working slide outline for Friday **2026-09-04 19:00 Europe/Berlin**. Not official Quantic dashboard text. Not a claim that NFR-1 / NFR-2 timings or a four-browser NFR-7 matrix are met.

Use with [Coverage](coverage.md) (every freeze ID) and the [Friday plan](friday-plan.md) diagram. Spoken timing lives in the [video script](video-script.md). Saturday recording cuts (three ~10 min variants): [Presentation](presentation.md). This file stays the 8/12-slide outline.

**Default for the room:** the **8-slide cut**. The 12-slide outline is if someone asks for more FR walkthrough.

## 12-slide outline (8–12 range)

| # | Slide | Say / show | Honesty |
|---|---|---|---|
| 1 | **Title** | Café Fausse. Knowledge + App. Friday score-5 working reference. | This site is not the restaurant. |
| 2 | **Two surfaces** | Knowledge = `knowledge.cafe.artof.link` (HTTPS live). App = in-repo React / Flask / PostgreSQL. | `cafe.artof.link` is an AWS ELB, **not** our app. |
| 3 | **Scope / grade floor** | Official SRS only: **FR-1..FR-18**, **NFR-1..NFR-9**. | No FR-19 / NFR-10. Freeze data stays frozen. |
| 4 | **Architecture** | Mermaid from Friday plan: Live Knowledge HTTPS vs App local/tunnel vs Future hostname. | Future #22 is hosting, not a missing FR. |
| 5 | **FR map** | [Coverage](coverage.md) table. Code + CI for the functional rows. | Evidence class is on the table. |
| 6 | **Home + Menu** | FR-1..FR-5. Play `clips/01-home-menu.mp4`. | Clip = look, not a public-host probe. |
| 7 | **Reservations** | FR-6..FR-9, FR-17..FR-18. Play `clips/02-happy-book.mp4`. 30 tables. Full slot = FR-9 error. | Fail closed if DB is missing. |
| 8 | **Newsletter + About / Gallery** | FR-15..FR-16; FR-10..FR-14 (history, founders, awards, lightbox). | Awards and reviews are freeze quotes. |
| 9 | **Live or fallback** | HTTPS Knowledge. Local or tunnel App. Clips if the stack is down. | Never demo `cafe.artof.link` as Café Fausse. |
| 10 | **NFR honesty** | NFR-5 / NFR-6: code + CI + local J6/J8. J9 **PASS** Vite-only. NFR-7 **partial** (Edge + Firefox home; Chrome/Safari Unknown). NFR-1 / NFR-2: **Unknown** as SRS-budget claims ([#40](https://github.com/artofdream/aea-interactive-design/issues/40) / [#44](https://github.com/artofdream/aea-interactive-design/issues/44)). | Do not say “NFR-1/2 met” or “four browsers.” |
| 11 | **AI tooling** | `docs/ai-tooling.md`. Cursor + GitHub Actions. Author does not merge. | MRC **COMMENT** is role-approve; then `cursor[bot]` merge after green + Bugbot. |
| 12 | **Future close** | #22, #34–#38 = Future / hardening. **Not grade gaps.** Friday locked access + video/scenarios. | Questions. Stay on the freeze. |

## 8-slide cut (use this Friday)

| # | Slide | Merge from the long outline |
|---|---|---|
| 1 | **Title + two surfaces** | Slides 1–2. Knowledge HTTPS vs App local. `cafe.artof.link` is not Café Fausse. |
| 2 | **Scope** | Slide 3. FR-1..FR-18 / NFR-1..NFR-9 only. |
| 3 | **Architecture** | Slide 4. Live / local-or-tunnel / Future diagram. |
| 4 | **FR coverage + clips** | Slides 5–6. Coverage table + clip 01 (Home → Menu). |
| 5 | **Reservations + newsletter** | Slides 7–8. Clip 02. Mention About/Gallery IDs in one sentence. |
| 6 | **Live or fallback** | Slide 9. HTTPS / local / clips. |
| 7 | **NFR honesty** | Slide 10. J1–J8 local PASS; J9 PASS Vite-only; NFR-7 partial; NFR-1 / NFR-2 not-claimed-met. |
| 8 | **AI tooling + Future close** | Slides 11–12. Tooling log. #22 / #34–#38 ≠ missing SRS. |

## What not to put on a slide

- “Journey 1–9 passed” as a single stamp (J1–J8 is Flask+DB; J9 is Vite-only), or any NFR-1 / NFR-2 / four-browser NFR-7 **met** mark. Coverage / #40 / #44: J1–J8 local PASS; J9 PASS Vite-only; NFR-7 partial.
- “Live restaurant at `cafe.artof.link`.”
- FS extras (#34–#38) as if they were official requirements.
- A fifth team, GitLab, AWS in the MVP cut, or invented IDs.

## Speaker props

- Browser tab: `https://knowledge.cafe.artof.link/` (this map).
- Browser tab: local `http://127.0.0.1:5173` or a probed tunnel — or no App tab, only clips.
- This page + [video script](video-script.md) scenario A–F.
