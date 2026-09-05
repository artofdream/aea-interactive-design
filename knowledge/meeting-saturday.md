# Saturday meeting

**In plain English:** Owner notes from **2026-09-05** locked one ~10 minute VIDEO. It is **not** “pick Variant A or B or C.” It is a five-part cut: team IDs, Meghna’s live site demo, then Variant B and Variant C as **3-minute** segments. Full talk tracks stay on [Talk cuts](presentation.md). Clips stay on the [Video script](video-script.md). This page does not replace them.

**When:** Saturday **2026-09-05 ~13:00 America/New_York** (**19:00 Europe/Berlin**). The America/New_York clock is the scheduled recording slot; Europe/Berlin is the repo’s “today” zone.

**Source:** team meeting notes 2026-09-05 (owner paste) → GitHub [#97](https://github.com/artofdream/aea-interactive-design/issues/97).

**Grade floor:** official SRS only — **FR-1..FR-18**, **NFR-1..NFR-9**. Do not invent **FR-19**. Do not say **NFR-1** / **NFR-2** are met. **NFR-7** is **partial**. `/operator` is a read-only recording helper — **not FR-19**. `https://cafe.artof.link/` is Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) — **not** forever production. Zoom dry-run on the video-script page is **PROTOTYPE**, not the Quantic submission.

## Locked VIDEO structure (~10 min)

| # | Part | Clock | Who | What |
|---|---|---|---|---|
| 1 | Team + ID verification | ~30s | Shared | Names / student IDs. |
| 2 | Website demo | ~3 min | **Meghna** | Live `https://cafe.artof.link/` — Home, Gallery, Menu, Reservations. Navigate to show FR/NFR. |
| 3 | Architecture + Diagram (**Variant B**) | ~3 min | **Claude or Hiren** | Take over from reservation → architecture. |
| 4 | Coding rationale (**Variant C**) | ~3 min | **Claude or Hiren** | Frameworks + implementation. |
| 5 | Shared close | remainder | Shared | Honesty close on [Talk cuts](presentation.md). |

**Hiren** chooses Architecture (B) or Coding (C). **Claude** takes the other. That choice is **Unknown** until the owner decides. Do not invent the lock.

## Per-part pack (mandatory)

Every part needs: **script / presentation / talking points** + a **prototype video**. **Voice-over is TBD** on every part.

Every part must stay: plain English; supporting documents; PDF refs (GitHub + cafe + Knowledge); UX-compliant sites ([#91](https://github.com/artofdream/aea-interactive-design/issues/91) App / [#92](https://github.com/artofdream/aea-interactive-design/issues/92) Knowledge); issues → Slack, Claude addresses.

| Part | Script / talking points | Prototype video now | Voice-over |
|---|---|---|---|
| 1. Team + ID (~30s) | Shared open on [Talk cuts](presentation.md) (first 30s only — names / IDs). | **TBD** / none yet. | **TBD** |
| 2. Website demo (Meghna, ~3 min) | This page (demo beats below) + [Must-film shots](must-film-shots.md) + [Coverage](coverage.md). Pages: Home, Gallery, Menu, Reservations. | Live `https://cafe.artof.link/` preferred. Fallback look: clip **01** / **02** on the [Video script](video-script.md). Zoom dry-run v2 is **PROTOTYPE** (Variant A) — **not** this cut. | **TBD** |
| 3. Architecture / Variant B (~3 min) | [Talk cuts — Variant B](presentation.md) condensed to 3 min. Diagrams: [Stack](stack.md), [staging SVG](assets/hld-aws-staging.svg). Start from the reservation screen. | **Unknown** / to-be-filled. No dedicated B clip yet. HLD SVGs are the stills. | **TBD** |
| 4. Coding / Variant C (~3 min) | [Talk cuts — Variant C](presentation.md) condensed to 3 min. Frameworks + why this implementation. | **Unknown** / to-be-filled. No dedicated C clip yet. | **TBD** |
| 5. Shared close | [Shared close](presentation.md) on Talk cuts. | **TBD** / none yet. | **TBD** |

Optional: Claude may prepare an **advance recording** for evaluation. That file is **Unknown** until it exists. It is **not** the Quantic submit video.

## Meghna demo beats (~3 min)

Prefer live `https://cafe.artof.link/` (staging #57). Navigate; do not invent IDs. Point at [Coverage](coverage.md) if a grader asks “where is that FR?”

| Order | Page | Show (freeze IDs) | Do not say |
|---|---|---|---|
| 1 | **Home** | Name, contact, hours, nav — **FR-1..FR-4**. | Production-forever hosting. |
| 2 | **Gallery** | Images, awards, reviews — **FR-12..FR-14**. | Extra awards or invented quotes. |
| 3 | **Menu** | Freeze categories and prices — **FR-5**. | “Improved” prices. Bruschetta is an honest placeholder. |
| 4 | **Reservations** | Form fields **FR-6**; slot **FR-7**; table 1–30 **FR-8**; success or full-book **FR-9**; Flask + store **FR-17** / **FR-18**. Hand off here to architecture. | A guessed yes if the DB is down (**NFR-6**). **FR-19**. |

**NFR on the walk (honest):** theme / Flex-Grid / viewports **NFR-3** / **NFR-4** / **NFR-8**. App mobile pass [#91](https://github.com/artofdream/aea-interactive-design/issues/91) (PR #93). Knowledge mobile pass [#92](https://github.com/artofdream/aea-interactive-design/issues/92) (PR #94). Do **not** claim **NFR-1** / **NFR-2** met. **NFR-7** is **partial**. After a **live** happy book (must-film), `/operator` may show the row — **not FR-19**. Newsletter is **FR-15** / **FR-16** store only.

Exact click paths for the four must-film writes stay on [Must-film shots](must-film-shots.md). Do not move them here.

## Supporting docs / PDF refs

Paste or open these. They are the reference pack (GitHub + cafe + Knowledge + official PDF).

| What | Where |
|---|---|
| Official SRS PDF (source of truth) | [`docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf`](https://github.com/artofdream/aea-interactive-design/blob/main/docs/official/MSEE_Web_Application_and_Interface_Design_Cafe_Fausse_SRS.pdf) — SHA256 `6075e5964601aa3e3c7a3085c626eab820e3d733a396b00e20339cfdc77a9d82` |
| Working freeze | [SRS freeze](srs.md) · `docs/srs.md` — **FR-1..FR-18**, **NFR-1..NFR-9** only |
| GitHub repo | [artofdream/aea-interactive-design](https://github.com/artofdream/aea-interactive-design) |
| Restaurant app | [https://cafe.artof.link/](https://cafe.artof.link/) — staging #57, not forever |
| Knowledge map | [https://knowledge.cafe.artof.link/](https://knowledge.cafe.artof.link/) |
| Evidence / honesty | [Coverage](coverage.md) · [Honesty](honesty.md) · [Handoff](quantic-handoff.md) |
| UX compliance | App [#91](https://github.com/artofdream/aea-interactive-design/issues/91) / PR #93 · Knowledge [#92](https://github.com/artofdream/aea-interactive-design/issues/92) / PR #94 |
| Issues → Slack | File a GitHub issue; Slack the number; **Claude** addresses. Do not invent a close. |

## Open / Unknown (do not invent)

- **Hiren:** Architecture (B) vs Coding (C) — Claude takes the other — **Unknown** until the owner decides.
- **Voice-over** — **TBD** on every part.
- **Final Quantic submit video** — **Unknown** until a **live** must-film pass **plus voice**. Dry-run stays **PROTOTYPE**.
- Optional Claude advance recording for eval — **Unknown** until a file exists.
- Per-part prototype videos for B and C — **Unknown** / to-be-filled.

## Open these

- [Talk cuts](presentation.md) — Variant B and Variant C (3-min segments) plus shared open / close. Variant A remains a draft, not the locked Saturday cut.
- [Video script](video-script.md) — timed beats, scenario menu A–F, committed clips. Zoom dry-run v2 is **PROTOTYPE**, not the Quantic submission.
- [Must-film shots](must-film-shots.md) — four camera beats: happy book → `/operator`, newsletter → newsletter-only, full-book **HTTP 409**, NFR-6 via Coverage/CI.
- [Slide outline](presentation-sample.md) — 12-slide outline + 8-slide cut (Friday deck; not a second talk track).
- [Friday plan](friday-plan.md) — what Friday already locked.
- [Coverage](coverage.md) — every freeze ID.
- [Honesty](honesty.md) — probe / **Unknown**.
- [Glossary](glossary.md) — short labels.

## Other meetings

- [Wednesday](meeting-wednesday.md) — earlier teammate meeting
- [Friday](meeting-friday.md) — score-5 / tech access
- [Sunday](meeting-sunday.md) — ends with a recording; supporting docs target **9:00 America/New_York** on 2026-09-06; remaining gaps stay **Unknown**

[Quantic deliverable handoff](quantic-handoff.md) — links + Coverage vs talk track.

Back to the [Quantic / MSAIE](quantic.md) hub.
