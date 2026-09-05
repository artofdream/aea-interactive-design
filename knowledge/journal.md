# Journal

This page is a **process index** for Café Fausse Knowledge. It is not the restaurant and not a CMS. Meeting packs stay the source of detail. Home’s [top 5 lessons](index.md) cite this list.

Delivery-only ([#79](https://github.com/artofdream/aea-interactive-design/issues/79)): linked from [Quantic / MSAIE](quantic.md) and home. Not in the global top nav.

## Principles

- **Honesty.** A status word is a claim. Probe **this session** (command, HTTP GET, CI log, or committed file) or write **Unknown**. See [Honesty](honesty.md).
- **Grade-floor freeze.** Official SRS only: **FR-1..FR-18**, **NFR-1..NFR-9**. Do not invent **FR-19** / **NFR-10**. Extra product ideas go to [Future](future.md).
- **GitHub only.** Issues, PRs, and Actions. No GitLab, `glab`, or GitLab CI.
- **One finding → one issue → one branch → one PR.** The author does not merge their own PR.
- **Fail closed.** Missing PostgreSQL, a full 30-table slot (**FR-9**), a timeout, or a missing freeze file → honest **no**.
- **Ratchet, not a boast.** A failure adds a tighter guide or sensor. Do not claim this harness is antifragile.

## Lessons learned

Home shows the first five. Same five, with the why:

1. **Probe or Unknown.** Yesterday’s GET is not today’s evidence. Hostnames on slides are not live.
2. **SRS IDs are the grade floor.** Functional Spec extras (#34–#38) and permanent hosting (#22) are Future, not missing assignment rows.
3. **Two surfaces.** This map explains. The App takes bookings. Mixing them is a false claim.
4. **Split the PR.** Folding unrelated findings into one closer list blocks merge. Keep one issue on one branch.
5. **Honest no.** Guessing “yes” when the database is down, the slot is full, or CI is red is worse than a clear failure.

## Meeting MoM overview

Detail pages for Wed / Fri / Sat / Sun are on open [#89](https://github.com/artofdream/aea-interactive-design/pull/89) (`meeting-*.html`). Until that lands, live meeting URLs stay **404**. Use the existing delivery pages below. Journal does not replace them.

| Meeting | When | One-line MoM | Detail |
|---|---|---|---|
| Wednesday | 2026-09-02 19:00 Europe/Berlin | Owner locked agenda **1, 3, 4** (not 2). Start from the Brief. FS extras = Future. | [Brief](brief.md). Meeting pack on #89: `meeting-wednesday.html` |
| Friday | 2026-09-04 19:00 Europe/Berlin | Score 5 / tech access. P0/P1/P2. Live Knowledge vs App local vs Future hostname. | [Friday plan](friday-plan.md). Meeting pack on #89: `meeting-friday.html` |
| Saturday | 2026-09-05 ~13:00 America/New_York / 19:00 Europe/Berlin | Lock one ~10 min VIDEO (demo + architecture + rationale). Issues → Slack → Claude. | [Talk cuts](presentation.md), [video script](video-script.md). Meeting pack on #89: `meeting-saturday.html` |
| Sunday | 2026-09-06 | Ends with a recording. Supporting docs target **9:00 America/New_York**. Remaining gaps stay **Unknown**. | [Must-film shots](must-film-shots.md). Meeting pack on #89: `meeting-sunday.html` |

An older stub remains at [Future / journal](future/journal.md) so old links do not vanish.
