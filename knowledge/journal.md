# Journal

**In plain English:** This page is the project notebook. It holds principles, lessons, and a minutes overview of the teammate meetings. It is **not** the live handoff and **not** the restaurant.

The live handoff file is still `research/daily-briefs/YYYY-MM-DD.md` (today: [2026-09-05](https://github.com/artofdream/aea-interactive-design/blob/main/research/daily-briefs/2026-09-05.md)). Uncommitted files do not count. Meeting **detail** stays on the meeting packs and sister pages; this Journal is the index.

Home surfaces the [top 5 lessons](index.md#top-5-lessons-learned). Short labels: [Glossary](glossary.md). Course hub: [Quantic / MSAIE](quantic.md).

**Honesty this session (2026-09-05):** live `https://knowledge.cafe.artof.link/journal.html` is **404** until this PR deploys. Meeting packs, handoff, Meghna pages, and [To-be](to-be.md) land with [PR #89](https://github.com/artofdream/aea-interactive-design/pull/89); live `/meeting-*.html` / `/quantic-handoff.html` / `/to-be.html` are **404** this session. Sister pages already on `main` stay complete: [Brief](brief.md), [Friday plan](friday-plan.md), [Talk cuts](presentation.md), [Video script](video-script.md).

## Principles

These are the rules we keep. They are ratchet, not a claim that the system is antifragile.

| Principle | In plain English | Where it lives |
|---|---|---|
| Honesty vocabulary | A status word needs a **probe this session** or it stays **Unknown**. | [Honesty](honesty.md) · [Glossary](glossary.md) |
| Grade-floor freeze | Official SRS only: **FR-1..FR-18**, **NFR-1..NFR-9**. Do not invent **FR-19**. | [SRS freeze](srs.md) · [Coverage](coverage.md) |
| GitHub only | Issues, PRs, Actions, Pages. No GitLab, no `glab`, no GitLab CI. | [Stack](stack.md) · repo [README](https://github.com/artofdream/aea-interactive-design) |
| Fail closed | Missing DB, full 30-table slot, timeout, missing freeze file → honest **no**. | [Honesty](honesty.md) · **FR-9** / **NFR-6** |
| Ratchet, not antifragile | A failure adds a tighter guide or sensor. Deleting a check to go green is a regression. | `AGENTS.md` · [Honesty](honesty.md) |
| Author does not merge | One finding → one issue → one branch → one PR. MRC **COMMENT**; no self-merge. | [PR coordinator skill](https://github.com/artofdream/aea-interactive-design/blob/main/.cursor/skills/pr-coordinator/SKILL.md) |
| Two surfaces | This map is not the restaurant. Staging is not forever. | [Stack](stack.md) · Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22) |
| Shared memory | Committed git + today’s DATE_RE brief. Chat is not the handoff. | [Daily briefs](https://github.com/artofdream/aea-interactive-design/tree/main/research/daily-briefs) |
| Knowledge before code | Do not implement restaurant features from a Knowledge-site task. | [Knowledge guardian](https://github.com/artofdream/aea-interactive-design/blob/main/.cursor/skills/knowledge-guardian/SKILL.md) |
| Delivery stays on the hub | Quantic packs are complete pages. They are not dumped into the global top nav ([#79](https://github.com/artofdream/aea-interactive-design/issues/79)). | [Quantic / MSAIE](quantic.md) |

## Lessons learned

Home cites the first five. The rest is the longer notebook.

### Top 5 (also on [Home](index.md#top-5-lessons-learned))

1. **A status word is a claim.** Probe this session or write **Unknown**. A previous session, a hostname on a slide, or a closed PR is not a probe.
2. **The grade floor is the official SRS only.** **FR-1..FR-18** / **NFR-1..NFR-9**. Extras are [Future](future.md) / [To-be](to-be.md), not missing FRs. Do not invent **FR-19**.
3. **Fail closed.** Missing PostgreSQL, a full book (**FR-9**), a timeout, or a missing freeze/PDF → honest **no**.
4. **Two surfaces.** Knowledge Pages ≠ restaurant. Lightsail [#57](https://github.com/artofdream/aea-interactive-design/issues/57) ≠ permanent hosting [#22](https://github.com/artofdream/aea-interactive-design/issues/22).
5. **Uncommitted files are not shared memory.** The author does not merge their own PR. Bugbot comments are a signal, not the merge gate.

### More we learned this week

- **Hub-only, not hollow.** [Quantic](quantic.md) is a navigation hub. Clips stay on Brief / Video; HLD stays on Stack ([#74](https://github.com/artofdream/aea-interactive-design/issues/74)).
- **A health GET is not a write probe.** `/api/health` **200** does not prove a reservation or newsletter write.
- **`/operator` is not admin and not FR-19.** Read-only recording helper ([#54](https://github.com/artofdream/aea-interactive-design/issues/54) / [PR #58](https://github.com/artofdream/aea-interactive-design/pull/58)).
- **Newsletter is store-only.** **FR-15** / **FR-16**. No outbound mailer in the MVP.
- **Do not say NFR-1 / NFR-2 met.** Local Vite timings are not an SRS broadband stopwatch. **NFR-7** is **partial**.
- **Autofix is a new branch.** Cursor Bugbot autofix must not squash into an unrelated finding PR.
- **Prefer `cafe.artof.link`.** Demote stale tunnels. sslip is the interim backup, not the primary paste ([#64](https://github.com/artofdream/aea-interactive-design/issues/64)).
- **Plain English for spoken / VO.** Meghna on-camera talk does not recite FR/NFR IDs. Coverage holds the ID map.
- **architecture.artof.link is a tone bar only.** Do not copy florist Path B, 14 hats, or that site’s case studies.

First foundation note: `research/daily-briefs/2026-08-31.md`. An older stub remains at [Future / journal](future/journal.md) so old links do not vanish.

## Meeting MoM overview

Meeting pages remain the source of detail once [PR #89](https://github.com/artofdream/aea-interactive-design/pull/89) lands. Until then, use the sister pages that already exist on `main`. Live Pages GET of the meeting HTML is **Unknown** / **404** this session.

| When | Room job (one line) | Minutes page | Sister pages (already on main) |
|---|---|---|---|
| Wed **2026-09-02** 19:00 Europe/Berlin | Start from the assignment map. Owner locked **1, 3, 4** — not 2. | [Wednesday](meeting-wednesday.md) | [Brief](brief.md) · [Coverage](coverage.md) · [SRS freeze](srs.md) |
| Fri **2026-09-04** 19:00 Europe/Berlin | Score-5 / tech access. Lock video and scenarios. Not Future extras. | [Friday](meeting-friday.md) | [Friday plan](friday-plan.md) · [Brief](brief.md) · [Video script](video-script.md) · [Slides](presentation-sample.md) |
| Sat **2026-09-05** 19:00 Europe/Berlin / ~13:00 America/New_York | Lock one ~10 min VIDEO (not “pick A or B or C”). Five parts. | [Saturday](meeting-saturday.md) | [Talk cuts](presentation.md) · [Must-film shots](must-film-shots.md) · [Meghna materials](meghna-materials.md) |
| Sun **2026-09-06** | Ends with a recording. Supporting docs target **9:00 America/New_York**. Start clock still **Unknown**. | [Sunday](meeting-sunday.md) | [Handoff](quantic-handoff.md) · [To-be](to-be.md) · Saturday pack |

One-page paste pack: [Quantic deliverable handoff](quantic-handoff.md).

### Wednesday — 2026-09-02

Owner locked items **1, 3, 4** (not 2). The room started with the assignment map, not a second product. Team Functional Spec v0.1 extras vs the official SRS stay on the [Brief](brief.md). Permanent hosting [#22](https://github.com/artofdream/aea-interactive-design/issues/22) and extras [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38) are Future, not missing grade rows.

### Friday — 2026-09-04

Score-5 / tech access. Show the freeze, prove what is live, lock the video and scenarios A–F. Say the Unknowns out loud: **NFR-1** / **NFR-2** not-claimed-met; **NFR-7** **partial**; `/operator` **not FR-19**. Full P0/P1/P2: [Friday plan](friday-plan.md).

### Saturday — 2026-09-05

Locked five-part VIDEO (~10 min) — [#97](https://github.com/artofdream/aea-interactive-design/issues/97):

1. Team + ID (~30s)
2. Website demo (~3 min) — **Meghna** on live `https://cafe.artof.link/` (Home → Gallery → Menu → Reservations)
3. Architecture + diagram (**Variant B**, ~3 min) — Claude or Hiren
4. Coding rationale (**Variant C**, ~3 min) — the other
5. Shared close

Hiren chooses B vs C. That speaker lock is **Unknown**. Voice-over is **TBD**. Zoom dry-run is **PROTOTYPE**, not the Quantic submission. Pack: [Saturday](meeting-saturday.md) · [Meghna demo](meghna-cafe-demo.md) · [Meghna VO](meghna-voiceover.md).

### Sunday — 2026-09-06

Ends with a recording of that locked VIDEO. Supporting docs target **9:00 America/New_York**. Room start clock, Hiren B-vs-C, recorded VO, and the final submit video stay **Unknown**. If someone asks about extras after the MVP, open [To-be](to-be.md) — not the grade floor.

## Handoff

| What | Where | What it is not |
|---|---|---|
| Live daily handoff | `research/daily-briefs/YYYY-MM-DD.md` (DATE_RE) | This Journal. Chat history. `research/random-thoughts/` |
| Quantic paste pack | [Handoff](quantic-handoff.md) | The official Quantic dashboard |
| Coverage vs talk | [Coverage](coverage.md) vs [Talk cuts](presentation.md) | A claim every NFR is met |
| Home top-5 | [Home — lessons](index.md#top-5-lessons-learned) | A substitute for this page |

Back to [Home](index.md) or the [Quantic hub](quantic.md).
