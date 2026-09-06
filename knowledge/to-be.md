# To-be (beyond the Quantic MVP)

**In plain English:** This page is the Quantic-facing **to-be** map. It is not the grade floor. The assignment grade is **as-is**: official SRS only — **FR-1..FR-18**, **NFR-1..NFR-9**. Everything here is planned Future. Do not invent **FR-19** or **NFR-10**. Do not say these rows are missing official requirements.

The long Future notes stay on [Future / not-MVP](future.md). The HLD picture stays on [Stack](stack.md). This page does not replace them.

## As-is vs to-be

| | As-is (grade floor) | To-be (planned Future) |
|---|---|---|
| What it is | The official SRS MVP | Extra product ideas after the first cut |
| IDs | **FR-1..FR-18**, **NFR-1..NFR-9** only | No new FR / NFR IDs |
| Restaurant | In-repo React + JSX, Flask, PostgreSQL | Permanent hosting, admin, extras — parked |
| Live share now | `https://cafe.artof.link/` — Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57), **not** forever | Always-on `cafe.artof.link` stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22) |
| Knowledge | This thin map on GitHub Pages | More essays — still not the restaurant |

**Honesty:** **NFR-1** / **NFR-2** stay **Unknown** as SRS-budget claims (do not say they are met). **NFR-7** is **partial**. `/operator` is a read-only recording helper — **not FR-19**. Weekend staging is not production forever.

## Parked Future (not missing grade rows)

These GitHub issues are **Future**. Missing them is **not** a missing FR/NFR.

| Issue | What it is (plain English) |
|---|---|
| [#22](https://github.com/artofdream/aea-interactive-design/issues/22) | Permanent restaurant hosting on `cafe.artof.link` — always-on productization. Weekend Lightsail [#57](https://github.com/artofdream/aea-interactive-design/issues/57) does **not** close this. |
| [#34](https://github.com/artofdream/aea-interactive-design/issues/34) | Reservation lifecycle extras (beyond book / full-slot) |
| [#35](https://github.com/artofdream/aea-interactive-design/issues/35) | Cancel / checkout / admin console |
| [#36](https://github.com/artofdream/aea-interactive-design/issues/36) | Menu CRUD (edit the freeze from a console) |
| [#37](https://github.com/artofdream/aea-interactive-design/issues/37) | Email identity / verbatim-case extras |
| [#38](https://github.com/artofdream/aea-interactive-design/issues/38) | Concurrency retry beyond fail-closed |
| [#135](https://github.com/artofdream/aea-interactive-design/issues/135) | Newsletter outbound via Amazon SES — after **FR-15** / **FR-16** store. Grade floor stays store-only until send is live and probed. Not **FR-19**. |

Team Functional Spec v0.1 extras vs the official SRS compare stay on the [Brief](brief.md). Do not promote those extras into the first restaurant cut.

## HLD to-be (picture)

Static copy: [to-be SVG](assets/hld-to-be.svg). Same story in words on [Stack](stack.md): Knowledge Pages stay; weekend staging is live now; permanent hosting stays dashed (#22).

![Café Fausse to-be: knowledge Pages plus weekend staging vs dashed permanent hosting](assets/hld-to-be.svg)

## Open these (sister pages stay complete)

- [Future / not-MVP](future.md) — full parked list, schema notes, journal stub
- [Stack](stack.md) — as-is / staging / to-be HLD
- [SRS freeze](srs.md) — grade floor IDs
- [Coverage](coverage.md) — evidence map for **FR-1..FR-18** / **NFR-1..NFR-9**
- [Honesty](honesty.md) — probe / **Unknown**
- [Quantic / MSAIE](quantic.md) — Delivery hub

Back to the [Quantic / MSAIE](quantic.md) hub.
