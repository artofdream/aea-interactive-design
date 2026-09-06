---
title: Part 3 present — diagrams only
nav: hide
---

# Part 3 — Present (diagrams only)

**Claude · Architecture · supporting deck**  
Script: [NATURAL](part3-variant-b-script-natural.html) · Live: [cafe.artof.link](https://cafe.artof.link/)  
Use this page while speaking — one beat per section. No FR/NFR IDs on camera. Say **MSAIE staging** for cafe.artof.link.

---

![Part 3 title](assets/slide-p3-00-title.svg "fit")

## Beat 1 — Why these boundaries (~0:00–0:25)

Product surface: Reservations on MSAIE staging (or still).

![Why these boundaries](assets/slide-p3-01-boundaries.svg "fit")

![Reservations still](assets/still-reservation.png)

---

## Beat 2 — How the request flows (~0:25–0:55)

React → Flask → Postgres (what Meghna clicks vs what hits the API).

![How the request flows](assets/slide-p3-02-flow.svg "fit")

![FE ↔ BE flow](assets/flow-meghna-fe-be.svg)

![Stack](assets/fit-02-stack.png)

---

## Beat 3 — Why two deploy targets (~0:55–1:35)

Same design · local vs MSAIE staging · on-box Postgres on staging.

![Why two deploy targets](assets/slide-p3-03-deploys.svg "fit")

![Local vs MSAIE staging rationale](assets/hld-local-vs-msaie-rationale.svg "fit")

![Local HLD](assets/hld-local.svg)

![MSAIE staging HLD](assets/hld-aws-msaie.svg)

---

## Beat 4 — How quality is encoded (~1:35–2:10)

Fail-closed · unique slot+table · freeze/CI.

![How quality is encoded](assets/slide-p3-04-quality.svg "fit")

![Boxes](assets/card-p3-boxes.png)

![Sensors](assets/card-p3-sensors.png)

---

## Beat 5 — Why these tradeoffs (~2:10–2:45)

Two targets · Knowledge ≠ App · newsletter store-only · staging temporary.

![Why these tradeoffs](assets/slide-p3-05-tradeoffs.svg "fit")

![Staging card](assets/card-p3-staging.png)

---

## Beat 6 — Handoff → Coding (~2:45–3:00)

![Handoff → Coding](assets/slide-p3-06-handoff.svg "fit")

![Handoff](assets/card-p3-handoff.png)

Hiren’s cut is teammate architecture — not ours. Ours is cafe.artof.link at MSAIE staging. Side page: [Teammate HLD (Hiren)](teammate-hld.md) — labeled teammate, never our MSAIE map.

![Teammate HLD next](assets/slide-p3-07-teammate.svg "fit")
