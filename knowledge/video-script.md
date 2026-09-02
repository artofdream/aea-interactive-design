# Video script (~10 minutes)

Working reference for Friday **2026-09-04 19:00 Europe/Berlin**. Not official Quantic dashboard text. Times are beats, not a stopwatch claim.

Play or talk over the committed clips when the local stack is down. The clips are a **look**. They are not a probe that reservations work on a public host, and they are not Café Fausse at `cafe.artof.link`.

**Clips on this site**

- Home → Menu: `knowledge/clips/01-home-menu.mp4`
- Happy reservation: `knowledge/clips/02-happy-book.mp4`

<video controls src="clips/01-home-menu.mp4"></video>

<video controls src="clips/02-happy-book.mp4"></video>

Lock scenarios with the menu at the bottom (A–F). Journey 1–9 pass/fail stays **Unknown** until [issue #40](https://github.com/artofdream/aea-interactive-design/issues/40).

## Timed beats

| Clock | Beat | What to show / say |
|---|---|---|
| 0:00–0:45 | **Title** | Café Fausse — Quantic MSAIE. Two teams: Knowledge (`knowledge.cafe.artof.link`) and App (in-repo). This video is the assignment floor, not a second product. |
| 0:45–1:30 | **Scope** | Grade of 5 = official SRS only (**FR-1..FR-18**, **NFR-1..NFR-9**). PDF is source of truth. Do not invent FR-19 / NFR-10. Freeze prices, address, hours, owners, awards, reviews. Extra ideas = Future. |
| 1:30–2:45 | **Architecture** | Three boxes from the [Friday plan](friday-plan.md) diagram: **Live Knowledge HTTPS** (this site, GET 200 this session). **App local or tunnel** (Vite / Flask / PostgreSQL on `main`). **Future** `cafe.artof.link` (AWS ELB today — **not** our restaurant; hosting [#22](https://github.com/artofdream/aea-interactive-design/issues/22)). |
| 2:45–5:00 | **FR coverage + clips** | Open [Coverage](coverage.md). Walk Home / Menu / nav (**FR-1..FR-5**). Play **clip 01** (Home → Menu). Point at About / Gallery rows (**FR-10..FR-14**) on the table if time is tight. |
| 5:00–6:30 | **Reservations + newsletter** | Form fields **FR-6**; slot check **FR-7**; random table 1–30 **FR-8**; success or full-book **FR-9**. Flask + Customers / Reservations **FR-17..FR-18**. Newsletter **FR-15..FR-16**. Play **clip 02** (happy book). Say: missing database → honest no, not a fake yes. |
| 6:30–7:30 | **Live or fallback** | **Live:** Knowledge HTTPS. **Local/tunnel:** App if the room can reach it. **Fallback:** these two clips. Never call `cafe.artof.link` a live Café Fausse demo. |
| 7:30–8:30 | **NFR honesty** | **NFR-5** / **NFR-6**: unique slot+table index, 30-table cap, fail-closed tests — **code + CI**. **NFR-3** / **NFR-4** / **NFR-8** / **NFR-9**: in-repo structure; Journey / device-lab pass-fail **Unknown**. **NFR-1** / **NFR-2** / **NFR-7**: **Unknown** until #40. Do not say they are met. |
| 8:30–9:15 | **AI tooling** | Point at `docs/ai-tooling.md`: Cursor cloud agent, GitHub issues/PRs/Actions, pytest, Vite/React JSX, Flask, PostgreSQL. AI drafted from the freeze. Student app repos were not copied. Author does not merge their own PR. |
| 9:15–10:00 | **Future close** | [#22](https://github.com/artofdream/aea-interactive-design/issues/22) and [#34](https://github.com/artofdream/aea-interactive-design/issues/34)–[#38](https://github.com/artofdream/aea-interactive-design/issues/38) are **Future**, not missing grade rows. Friday locked tech access + this script. Questions. |

If you run long, cut About/Gallery talk (they stay on Coverage) and keep reservations, clips, and the NFR honesty line.

## Scenario menu A–F

Working menu for Friday. These are **demo scenes**, not a claim that Journey 1–9 passed.

| ID | Scene | Freeze IDs | How to show |
|---|---|---|---|
| **A** | Home name, contact, hours, nav | FR-1..FR-4 | Live local/tunnel, or **clip 01** start |
| **B** | Menu categories and freeze prices | FR-5 | Live Menu page, or **clip 01** |
| **C** | Happy reservation (table 1–30) | FR-6..FR-9 success, FR-17..FR-18 | Live form, or **clip 02** |
| **D** | Newsletter signup stored | FR-15, FR-16 | Live footer form. If DB is down, show the honest error (NFR-6). |
| **E** | About history + Gallery awards / lightbox | FR-10..FR-14 | Live pages. No clip yet — do not invent one. |
| **F** | Full slot or fail-closed | FR-9, NFR-5, NFR-6 | Fill 30 tables on demo data, **or** stop PostgreSQL and show the error. Do not invent a success. |

**Do not film as “passed”:** Journey 1–9, **NFR-1**, **NFR-2**, **NFR-7**, or “live at `cafe.artof.link`.”

## If the stack is down

1. Knowledge site (HTTPS) + this script + Coverage.
2. Play clip 01 and clip 02.
3. Say out loud: fallback look; App not probed on a public host this session.

## Review note

MRC **COMMENT** is the role-approve signal on the PR that publishes these pages. The author does not merge. `cursor[bot]` may merge after this-run green checks and Bugbot resolve-or-decline.
