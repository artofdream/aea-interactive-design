# Video script (~10 minutes)

Working reference for Friday **2026-09-04 19:00 Europe/Berlin**. Not official Quantic dashboard text. Times are beats, not a stopwatch claim.

Play or talk over the committed clips when staging drops. The clips are a **look**. They are not a this-session write probe, and they are not a permanent hosting claim. Prefer live share `https://cafe.artof.link/` (Lightsail #57 — weekend window, not production forever).

## Zoom dry-run v2 — **PROTOTYPE**

> **PROTOTYPE** — Zoom dry-run visual. This is **not** the Quantic submission.

**Cut:** Variant A (~10 min) from live `https://cafe.artof.link/` + Knowledge. Clip 02 is fallback only for happy-book motion. Do not claim **NFR-1** / **NFR-2** met. Do not invent **FR-19**.

<video controls src="clips/zoom-dryrun-v2.mp4"></video>

**Short fallback clips on this site** (not the dry-run)

- Home → Menu: `knowledge/clips/01-home-menu.mp4`
- Happy reservation: `knowledge/clips/02-happy-book.mp4`

<video controls src="clips/01-home-menu.mp4"></video>

<video controls src="clips/02-happy-book.mp4"></video>

Lock scenarios with the menu at the bottom (A–F). Saturday recording variants (layers / architecture / coding): [Presentation](presentation.md). Coverage / [#40](https://github.com/artofdream/aea-interactive-design/issues/40) / [#44](https://github.com/artofdream/aea-interactive-design/issues/44): J1–J8 **PASS** (cts-ai, DB up); J9 **PASS** (Vite-only viewports + theme). Do not film **NFR-1** / **NFR-2** as met, or **NFR-7** as a four-browser pass.

## Timed beats

| Clock | Beat | What to show / say |
|---|---|---|
| 0:00–0:45 | **Title** | Café Fausse — Quantic MSAIE. Two teams: Knowledge (`knowledge.cafe.artof.link`) and App (in-repo). This video is the assignment floor, not a second product. |
| 0:45–1:30 | **Scope** | Grade of 5 = official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). PDF is source of truth. Do not invent FR-19 / NFR-10. Freeze prices, address, hours, owners, awards, reviews. Extra ideas = Future. |
| 1:30–2:45 | **Architecture** | Three boxes from the [Friday plan](friday-plan.md) diagram: **Live Knowledge HTTPS** (this site, GET 200 this session). **App staging share** — prefer `https://cafe.artof.link/` (Lightsail #57, GET 200 this session; not production forever). **Future** longer-term hosting [#22](https://github.com/artofdream/aea-interactive-design/issues/22). |
| 2:45–5:00 | **FR coverage + clips** | Open [Coverage](coverage.md). Walk Home / Menu / nav (**FR-1..FR-5**). Play **clip 01** (Home → Menu). Point at About / Gallery rows (**FR-10..FR-14**) on the table if time is tight. |
| 5:00–6:30 | **Reservations + newsletter** | Form fields **FR-6**; slot check **FR-7**; random table 1–30 **FR-8**; success or full-book **FR-9**. Flask + Customers / Reservations **FR-17..FR-18**. Newsletter **FR-15..FR-16**. Play **clip 02** (happy book). Say: missing database → honest no, not a fake yes. |
| 6:30–7:30 | **Live or fallback** | **Live:** Knowledge HTTPS. **Prefer App share:** `https://cafe.artof.link/` (Lightsail #57). **Backup:** `https://54-165-102-60.sslip.io/`. **Fallback:** these two clips. Do not call the hostname production forever. |
| 7:30–8:30 | **NFR honesty** | **NFR-5** / **NFR-6**: unique slot+table index, 30-table cap, fail-closed tests — **code + CI**; local J6/J8 PASS. **NFR-3** / **NFR-8**: J1–J8 local UX PASS + J9 **PASS** Vite-only viewports/theme. **NFR-7** **partial** (Edge all routes + Firefox home; Chrome/Safari Unknown). **NFR-1** / **NFR-2**: **Unknown** as SRS-budget claims (local Vite 56 ms / 32 ms are notes only). Do not say they are met. |
| 8:30–9:15 | **AI tooling** | Point at `docs/ai-tooling.md`: Cursor cloud agent, GitHub issues/PRs/Actions, pytest, Vite/React JSX, Flask, PostgreSQL. AI drafted from the freeze. Student app repos were not copied. Author does not merge their own PR. |
| 9:15–10:00 | **Future close** | [#22](https://github.com/artofdream/aea-interactive-design/issues/22) and [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38) are **Future**, not missing grade rows. Friday locked tech access + this script. Questions. |

If you run long, cut About/Gallery talk (they stay on Coverage) and keep reservations, clips, and the NFR honesty line.

## Scenario menu A–F

Working menu for Friday. These are **demo scenes**. J1–J8 PASS is local cts-ai UX while the DB was up. J9 **PASS** is Vite-only. Neither is a public-host probe.

| ID | Scene | Freeze IDs | How to show |
|---|---|---|---|
| **A** | Home name, contact, hours, nav | FR-1..FR-4 | Live local/tunnel, or **clip 01** start |
| **B** | Menu categories and freeze prices | FR-5 | Live Menu page, or **clip 01** |
| **C** | Happy reservation (table 1–30) | FR-6..FR-9 success, FR-17..FR-18 | Live form, or **clip 02** |
| **D** | Newsletter signup stored | FR-15, FR-16 | Live footer form. If DB is down, show the honest error (NFR-6). |
| **E** | About history + Gallery awards / lightbox | FR-10..FR-14 | Live pages. No clip yet — do not invent one. |
| **F** | Full slot or fail-closed | FR-9, NFR-5, NFR-6 | Fill 30 tables on demo data, **or** stop PostgreSQL and show the error. Do not invent a success. |

**Do not film as “passed”:** **NFR-1**, **NFR-2**, a full **NFR-7** four-browser matrix, or “production-forever at `cafe.artof.link`.” Prefer the hostname as the weekend staging share (#57). J9 **PASS** is Vite-only viewports + theme. J1–J8 was local cts-ai while the DB was up; after that, App reported `cafe-pg` down.

## If the stack is down

1. Knowledge site (HTTPS) + this script + Coverage.
2. Play clip 01 and clip 02.
3. Say out loud: fallback look; App not probed on a public host this session.

## Review note

MRC **COMMENT** is the role-approve signal on the PR that publishes these pages. The author does not merge. `cursor[bot]` may merge after this-run green checks and Bugbot resolve-or-decline.
