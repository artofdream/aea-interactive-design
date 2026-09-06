---
title: Part 3 present — diagrams only
nav: hide
---

# Part 3 — Present (diagrams only)

**Claude · Architecture · supporting deck**  
Script: [NATURAL](part3-variant-b-script-natural.html) · Live: [cafe.artof.link](https://cafe.artof.link/)  
Use this page while speaking — one beat per section. No FR/NFR IDs on camera. Say **MSAIE staging** for cafe.artof.link.

---

## Beat 1 — Why these boundaries (~0:00–0:25)

Product surface: Reservations on MSAIE staging (or still).

![Reservations still](assets/still-reservation-720.png)

---

## Beat 2 — How the request flows (~0:25–0:55)

React → Flask → Postgres (what Meghna clicks vs what hits the API).

![FE ↔ BE flow](assets/flow-meghna-fe-be-720.png)

![Stack](assets/fit-02-stack.png)

---

## Beat 3 — Why two deploy targets (~0:55–1:35)

Same design · local vs MSAIE staging · on-box Postgres on staging.

![Local HLD](assets/hld-local-720.png)

![MSAIE staging HLD](assets/hld-aws-msaie-720.png)

---

## Beat 4 — How quality is encoded (~1:35–2:10)

Fail-closed · unique slot+table · freeze/CI.

![Boxes](assets/card-p3-boxes.png)

![Sensors](assets/card-p3-sensors.png)

---

## Beat 5 — Why these tradeoffs (~2:10–2:45)

Two targets · Knowledge ≠ App · newsletter store-only · staging temporary.

![Staging card](assets/card-p3-staging.png)

---

## Beat 6 — Handoff → Coding (~2:45–3:00)

![Handoff](assets/card-p3-handoff.png)
