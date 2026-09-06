# Parts 3–5 — deliverable handoff mapping

**Not spoken on camera.**

**Purpose:** Keep freeze / FR / NFR / probe IDs accurate for the deliverable pack while spoken scripts stay natural demo language.  
**Rule:** Do **not** read this file on camera. Spoken lines live only in the natural [script](part3-variant-b-script-natural.md) / [VO](part3-variant-b-voiceover-natural.md) Timed lines (and the Part 4 / Part 5 twins). Technical scripts stay for post-mortem compare.  
**Label:** PROTOTYPE · talk #97 · packed 2026-09-06 Europe/Berlin  
**Index:** [Parts 3–5 materials](parts-345-materials.md) · [Coverage](coverage.md) · [Talk cuts](presentation.md) · [Quantic handoff](quantic-handoff.md)

---

## Speaking rule (reminder)

| On camera (spoken) | Off camera (this file — **not spoken on camera**) |
| --- | --- |
| Plain product language | FR- / NFR- IDs |
| “weekend staging”, timings in ms | Issue #57, #124, #126, Future #22 / #34–#38 |
| “freeze file”, “CI checks” | `test_freeze.py`, `test_fail_closed.py`, PDF SHA256, job names |
| “read-only helper” | “not FR-19” |

---

## Part 3 — Architecture (Variant B)

Spoken pack: [natural script](part3-variant-b-script-natural.md) · [natural VO](part3-variant-b-voiceover-natural.md). Technical compare: [script](part3-variant-b-script.md) · [VO](part3-variant-b-voiceover.md).

| Beat | Spoken intent | Freeze / evidence IDs |
| --- | --- | --- |
| Takeover / hostnames | Knowledge = Pages; App = weekend Lightsail share; not one shop; not forever | Hosting honesty **#57**; Knowledge ≠ App |
| HLD staging | Route53 A → Lightsail `cafe-fausse-staging` → Caddy + LE → Flask + SPA → Postgres on instance; AEA RDS untouched; `*.artof.link` ELB wildcard ≠ Café Fausse; longer-term hosting parked | Staging **#57**; Future **#22** parked |
| As-is picture | Markdown → Pages; `main` = React + Flask + Postgres; `cafe.artof.link` GET 200 weekend window / owner tear-down | Staging **#57** |
| Coverage boxes | Front-end pages → public site UX; API → booking + newsletter; DB → customers + reservations + unique slot/table; grade floor = official SRS only; `/operator` = read-only helper | React: **FR-1..5, FR-10..14**, **NFR-3, NFR-4, NFR-8**. Flask: **FR-6..9, FR-15..18**, **NFR-5, NFR-6**. Data: **FR-17**, **NFR-5** unique `(time_slot, table_number)`. Grade floor: **FR-1..18 / NFR-1..9**. **No FR-19** |
| Sensors / CI | Actions require freeze file + PDF fingerprint; tests lock freeze copy + fail-closed (missing DB, 31st table); author does not merge | CI harness only — not grade rows; `test_freeze.py`; `test_fail_closed.py`; PDF SHA256 |
| Explicit non-claims | Speed + browser honesty deferred to Shared close | **NFR-7** Partial (close); Future **#34–#38** parked |

---

## Part 4 — Coding rationale (Variant C)

Spoken pack: [natural script](part4-variant-c-script-natural.md) · [natural VO](part4-variant-c-voiceover-natural.md). Technical compare: [script](part4-variant-c-script.md) · [VO](part4-variant-c-voiceover.md).

| Beat | Spoken intent | Freeze / evidence IDs |
| --- | --- | --- |
| Freeze + CI | Menu, address, hours, awards, reviews in one freeze file; pages + menu API display it; tests fail on drift; do not “improve” prices | `shared/freeze.json`; locks **FR-2, FR-5, FR-10, FR-11, FR-14**; `test_freeze.py` |
| Table + fail-closed | Random table 1–30; unique slot+table; full slot → honest error (no 31st table); fail closed if DB missing / unreachable / timeout; email validate + strip + lower before store; verbatim-case Future parked | **FR-8** (`ORDER BY random()`, 1–30); **NFR-5** index `reservations_slot_table`; **FR-9** full-slot error; **NFR-6** write only if Postgres accepts; **FR-15** email normalize note; Future **#37** parked; `test_fail_closed.py` |
| Timezone / modules / tooling | Hours = Washington, DC; slots use America/New_York so remote browser cannot invent Sunday hours; clear backend packages + page folders; tooling log Cursor / Actions / pytest; no student-app copy | **FR-2, FR-7**; **NFR-9** cut (`backend/cafe_fausse/`, `frontend/src/pages/`); `slots.py` / PR **#12**; `docs/ai-tooling.md` |
| Parked | Futures not grade gaps | Future **#22**, **#34–#38** |

---

## Part 5 — Shared close

Spoken pack: [natural script](part5-shared-close-script-natural.md) · [natural VO](part5-shared-close-voiceover-natural.md). Technical compare: [script](part5-shared-close-script.md) · [VO](part5-shared-close-voiceover.md).

| Claim | Spoken line (plain) | Evidence IDs |
| --- | --- | --- |
| Page-load speed | Met on phone broadband probe — cold Home **466 ms** | **NFR-1** met · probe **A36** Brave broadband · issue **#124** |
| Reservation submit | Met — submit **233 ms** | **NFR-2** met · issue **#126** |
| Browser support | Still **Partial** — not claiming all four browsers | **NFR-7** Partial |
| Staging | `cafe.artof.link` weekend Lightsail share — **not forever** | Staging **#57** |
| Operator | Read-only helper — not an admin console / not a graded admin feature | **No FR-19** |
| Futures | Parked — not missing grade rows | Future **#22**, **#34–#38** |
| Shipped floor | Official SRS on `main` (React + Flask + Postgres + CI); Knowledge live HTTPS; evidence on Coverage | **FR-1..18**, **NFR-1..9** |
| Journeys (optional breath) | Core journeys pass with DB up; prefer live share after healthy GET, or clips | J1–J8 (DB up); J9 Vite-only |

**Do not** use the old “NFR-1 / NFR-2 Unknown / not claimed met” wording anywhere in this pack.

---

## Cross-part honesty checklist (deliverable)

- [x] NFR-1 **met** (466 ms, #124) — speakable as “load timing met on phone broadband probe”
- [x] NFR-2 **met** (233 ms, #126) — speakable as “submit timing met”
- [x] NFR-7 **Partial** — speakable as “browser support still partial”
- [x] Staging #57 not forever — speakable as “weekend staging, not forever”
- [x] Futures parked — speakable as “future items parked”
- [x] No FR-19 — speakable as “operator is a read-only helper”
- [x] SES outbound / verbatim email case = Future — **not** in spoken grade story unless optional. Do **not** claim Coverage SES outbound send.

---

*End handoff mapping · **not spoken on camera** · keep IDs here · keep spoken lines natural.*
