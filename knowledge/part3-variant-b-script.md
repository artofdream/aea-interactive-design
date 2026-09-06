# Part 3 — Architecture / Variant B (~3 min)

**Who:** **Claude** (owner lock 2026-09-06) — Architecture Part 3.  
**Job:** Take over from Meghna’s reservation screen → diagrams → Coverage boxes → sensors → hand off to Coding.  
**Picture:** live Reservations (or clip/still) → Stack + AWS staging SVG → coverage cards → CI sensors.  
**Label:** **PROTOTYPE** — not Quantic submit.  
**Talk lock:** #97 five-part VIDEO. Room clock ≈ **3:30–6:30**.

Spoken scripts for this technical part **may use FR/NFR IDs**. A plain-English VO twin is in [Part 3 VO](part3-variant-b-voiceover.md). Pack index: [Parts 3–5 materials](parts-345-materials.md). Talk cuts: [Presentation](presentation.md).

---

## 1. Timed beat sheet (~180s)

| Clock | Dur | Beat | Show | Say |
| ---: | ---: | --- | --- | --- |
| **0:00–0:20** | 20s | Takeover | Reservations still / live form on `cafe.artof.link` | “Taking Architecture from Reservations. Two hostnames: Knowledge on GitHub Pages, App on Lightsail staging #57 — not one shop, not production forever.” |
| **0:20–1:00** | 40s | HLD staging | `hld-aws-staging` SVG (+ Stack slide) | “As-is: Route53 A to Lightsail `cafe-fausse-staging`, Caddy + Let’s Encrypt, Flask + built SPA, Postgres on the instance. AEA RDS untouched. The `*.artof.link` ELB wildcard is not Café Fausse. Longer-term hosting stays Future #22.” |
| **1:00–1:50** | 50s | As-is picture | `hld-as-is` SVG | “Knowledge markdown builds to Pages. App code on `main` is React + Flask + Postgres. This weekend’s share is `cafe.artof.link` GET 200 — weekend window, owner tear-down, not forever.” |
| **1:50–2:40** | 50s | Boxes → IDs | Coverage / boxes card | “React pages map to FR-1..FR-5 and FR-10..FR-14, plus NFR-3, NFR-4, NFR-8. Flask APIs: FR-6..FR-9 and FR-15..FR-18 with NFR-5 and NFR-6. Postgres is FR-17 — unique `(time_slot, table_number)`. Grade floor only: FR-1..18 / NFR-1..9. `/operator` is a read-only helper — not FR-19.” |
| **2:40–3:00** | 20s | Sensors + handoff | Sensors / CI card | “Outer harness: Actions require freeze file + PDF SHA256; `test_freeze.py` locks copy; `test_fail_closed.py` locks missing-DB and the 31st table. Author does not merge. Over to Coding — why freeze, tables, timezone.” |

**Room tip:** If late at 2:30, skip as-is deep dive; keep staging SVG + boxes + handoff.

---

## 2. Diagram callouts (what to point at)

| Visual | Point at | One line |
| --- | --- | --- |
| Reservations start | Form fields / Reserve | “Product surface we just walked — now the boxes behind it.” |
| AWS staging SVG | Route53 → Lightsail → Caddy → Flask/SPA → PG | “Weekend #57 path; AEA RDS untouched.” |
| As-is SVG | Knowledge Pages vs App staging vs local MVP | “Two hostnames, two jobs.” |
| Boxes card | Three FR/NFR clusters | “Coverage is the grade map — not a second product.” |
| Sensors card | freeze / fail-closed / no self-merge | “Harness proves the freeze; not new FR rows.” |

Live visuals for the real take: [AWS staging SVG](assets/hld-aws-staging.svg), [as-is SVG](assets/hld-as-is.svg), [Stack](stack.md), [Coverage](coverage.md). Silent rehearsal clip: [`clips/part3-variant-b-prototype-silent.mp4`](clips/part3-variant-b-prototype-silent.mp4) (**PROTOTYPE**).

---

## 3. Supporting ID map

| Beat | Freeze IDs / notes |
| --- | --- |
| Takeover / staging | Hosting honesty #57; Future #22 parked |
| React / UX boxes | FR-1..5, FR-10..14, NFR-3, NFR-4, NFR-8 |
| Flask / forms boxes | FR-6..9, FR-15..18, NFR-5, NFR-6 |
| Data | FR-17, NFR-5 (unique index), NFR-6 (fail-closed) |
| Sensors | CI only — not grade rows |
| Explicit non-claims | No FR-19; NFR-7 Partial (Coding/close); Future #34–#38 parked |

---

## 4. Honesty (Architecture segment)

- Prefer `https://cafe.artof.link/` as **Lightsail staging #57** — not production forever.
- Knowledge ≠ App (no shared LB).
- Do **not** invent FR-19 for `/operator`.
- Leave full NFR-1 / NFR-2 / NFR-7 honesty lines for **Shared close** (updated 2026-09-06: NFR-1/2 **met** with probes; NFR-7 still Partial). One breath here is enough: “speed and browser honesty are in the close.”

---

## 5. Handoff line (Coding)

> “That’s the as-is picture and the Coverage map. Coding next: freeze file and CI, random table plus fail-closed, timezone and the NFR-9 cut. Over to you.”

---

*Packed 2026-09-06 Europe/Berlin · PROTOTYPE sample · talk #97.*
