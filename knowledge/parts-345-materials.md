# Parts 3–5 — materials pack (Quantic VIDEO Architecture / Coding / Close)

Everything for the locked five-part talk ([#97](https://github.com/artofdream/aea-interactive-design/issues/97)) after Meghna’s cafe demo.

**Talk spine:** Part 2 UX/business (Meghna) · **Part 3 architecture why/how** · **Part 4 coding why/how** · **Part 5 honesty/close**.

| Clock (room) | Part | Who | This pack |
| --- | --- | --- | --- |
| ~3:30–6:30 | **3 Architecture** (Variant B) | Claude or Hiren | **Camera:** [natural script](part3-variant-b-script-natural.md) + [natural VO](part3-variant-b-voiceover-natural.md) + [natural TTS](clips/part3-variant-b-prototype-vo-natural.mp4) · **Compare:** [technical script](part3-variant-b-script.md) + [technical VO](part3-variant-b-voiceover.md) + silent + [technical TTS](clips/part3-variant-b-prototype-vo.mp4) |
| ~6:30–9:30 | **4 Coding** (Variant C) | the other | **Camera:** [natural script](part4-variant-c-script-natural.md) + [natural VO](part4-variant-c-voiceover-natural.md) + [natural TTS](clips/part4-variant-c-prototype-vo-natural.mp4) · **Compare:** [technical script](part4-variant-c-script.md) + [technical VO](part4-variant-c-voiceover.md) + silent + [technical TTS](clips/part4-variant-c-prototype-vo.mp4) |
| ~9:30–10:00 | **5 Shared close** | Shared | **Camera:** [natural script](part5-shared-close-script-natural.md) + [natural VO](part5-shared-close-voiceover-natural.md) + [natural TTS](clips/part5-shared-close-prototype-vo-natural.mp4) · **Compare:** [technical script](part5-shared-close-script.md) + [technical VO](part5-shared-close-voiceover.md) + silent + [technical TTS](clips/part5-shared-close-prototype-vo.mp4) |

**Prefer natural for camera.** Keep technical silent + technical VO for post-mortem compare.  
**Label:** silent videos are **PROTOTYPE** / samples / rehearsal. VO-integrated clips are **PROTOTYPE TTS** (`en-US-GuyNeural`) — **not** teammate VO · **not** Quantic submit. Natural VO = **PROTOTYPE TTS** natural.  
**Owner rule:** camera spoken lines stay plain (no FR/NFR on camera). Technical spoken scripts **may use FR/NFR IDs** for compare. ID map: [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md) — **not spoken on camera**.  
**Demo focus:** **cafe.artof.link** = **staging environment for the MSAIE project** (temporary — not production forever). Avoid “weekend Lightsail staging” on camera.  
**Architect deploy table (off-camera ops OK):** [Local vs AWS MSAIE staging](part3-local-vs-aws.md) — same React+JSX→Flask→Postgres; Vite/local Postgres vs Caddy→on-box Postgres (tip `73d202d`, not AEA RDS); newsletter store-only. Also folded into [Stack](stack.md).  
**Architect visuals (PROTOTYPE):** [HLD + Meghna FE/BE](part3-hld-flow-notes.md) · [Part 4 coding overview](part4-coding-overview.md) — prefer **hld-local** + **hld-aws-msaie**; freeze for static pages; booking `GET /api/slots` + `POST /api/reservations`; newsletter `POST /api/newsletter` store-only. Older `hld-as-is` / `hld-aws-staging` stay as history.  
**Hiren B vs C pick:** **Unknown** — do not invent it.

---

## Honesty (must match [Coverage](coverage.md))

| Item | Status | Probe / cite |
| --- | --- | --- |
| **NFR-1** | **met** | A36 Brave broadband cold Home **466 ms** ([#123](https://github.com/artofdream/aea-interactive-design/issues/123) / [PR #124](https://github.com/artofdream/aea-interactive-design/pull/124)) |
| **NFR-2** | **met** | Reservation submit **233 ms** ([#125](https://github.com/artofdream/aea-interactive-design/issues/125) / [PR #126](https://github.com/artofdream/aea-interactive-design/pull/126)) |
| **NFR-7** | **Partial** | Do **not** claim four browsers |
| Host | MSAIE staging at `cafe.artof.link` | Temporary — **not forever**. Tracker [#57](https://github.com/artofdream/aea-interactive-design/issues/57) is off-camera. |
| FR-19 | **None** | `/operator` is a read-only helper |
| Future #22 / #34–#38 | **Parked** | Not grade gaps |
| Newsletter | Store-only | Do **not** claim Coverage SES outbound send |
| Recorded teammate VO | **Unknown** | Until Claude / Hiren / shared records |

Do **not** use the old “NFR-1 / NFR-2 Unknown / not claimed met” line.

---

## 1. Script + talking points

**Prefer natural for camera.** Technical scripts stay for post-mortem compare.

| File | What |
| --- | --- |
| [Part 3 — natural script](part3-variant-b-script-natural.md) | Timed ~3 min Architecture why/how — camera spoken (plain) |
| [Part 4 — natural script](part4-variant-c-script-natural.md) | Timed ~3 min Coding why/how — camera spoken (plain) |
| [Part 5 — natural script](part5-shared-close-script-natural.md) | Timed ~30–60s close — camera spoken (plain + updated honesty) |
| [Part 3 — technical script](part3-variant-b-script.md) | Compare / post-mortem (FR/NFR IDs OK) |
| [Part 4 — technical script](part4-variant-c-script.md) | Compare / post-mortem (FR/NFR IDs OK) |
| [Part 5 — technical script](part5-shared-close-script.md) | Compare / post-mortem (FR/NFR IDs OK) |
| [Handoff mapping](parts-345-handoff-mapping.md) | FR/NFR / probe map — **not spoken on camera** |
| [Local vs AWS](part3-local-vs-aws.md) | Architect deploy table (what used · explanation · rationale · implementation) |
| [Part 3 HLD + Meghna FE/BE](part3-hld-flow-notes.md) | Local + MSAIE staging HLDs + Meghna FE↔BE flow (**PROTOTYPE**) |
| [Part 4 coding overview](part4-coding-overview.md) | Forms → API → modules → Postgres (**PROTOTYPE**) |
| Knowledge (this site) | [Talk cuts](presentation.md) · [Quantic hub](quantic.md) · [Stack](stack.md) · [Meghna materials](meghna-materials.md) (Part 2 UX/business) |

Live site to rehearse after the cafe demo: **https://cafe.artof.link/** (MSAIE staging — temporary, not forever)

---

## 2. Prototype videos (silent)

| Asset | Path / URL | Note |
| --- | --- | --- |
| **Part 3 Architecture** | [`clips/part3-variant-b-prototype-silent.mp4`](clips/part3-variant-b-prototype-silent.mp4) (~180s) | Silent Variant B rehearsal. Reservations → staging HLD → Coverage boxes → sensors. **PROTOTYPE**, not Quantic submit. |
| **Part 4 Coding** | [`clips/part4-variant-c-prototype-silent.mp4`](clips/part4-variant-c-prototype-silent.mp4) (~180s) | Silent Variant C rehearsal. Freeze/CI → table/fail-closed → timezone/modules. **PROTOTYPE**. |
| **Part 5 Shared close** | [`clips/part5-shared-close-prototype-silent.mp4`](clips/part5-shared-close-prototype-silent.mp4) (~60s) | Silent shared-close rehearsal with updated honesty card. **PROTOTYPE**. |

Prefer **live diagrams / Coverage** for the real recording; use the silent prototypes only for rehearsal / VO timing.

> **PROTOTYPE** — silent Parts 3–5 samples. Not the Quantic submission. Voice-over recorded take **Unknown**.

<video controls src="clips/part3-variant-b-prototype-silent.mp4"></video>

<video controls src="clips/part4-variant-c-prototype-silent.mp4"></video>

<video controls src="clips/part5-shared-close-prototype-silent.mp4"></video>

**Recorded teammate VO:** **Unknown** until Claude, Hiren, or a shared speaker records.

---

## 2b. Prototype videos (technical VO — PROTOTYPE TTS)

**Label:** **PROTOTYPE TTS** (`en-US-GuyNeural`) — **not** teammate recorded VO · **not** Quantic submit.

Mux / duration notes: [Parts 3–5 VO notes](parts-345-vo-notes.md). Silent `*-silent.mp4` files stay in §2 and were **not** overwritten.

| Asset | Path / URL | Note |
| --- | --- | --- |
| **Part 3 Architecture** | [`clips/part3-variant-b-prototype-vo.mp4`](clips/part3-variant-b-prototype-vo.mp4) (~180s) | Technical timed lines + silence pad to the silent cut. **PROTOTYPE TTS**. |
| **Part 4 Coding** | [`clips/part4-variant-c-prototype-vo.mp4`](clips/part4-variant-c-prototype-vo.mp4) (~180s) | Technical timed lines + silence pad. **PROTOTYPE TTS**. |
| **Part 5 Shared close** | [`clips/part5-shared-close-prototype-vo.mp4`](clips/part5-shared-close-prototype-vo.mp4) (~64.5s) | Technical close + last-frame pad to match VO. **PROTOTYPE TTS**. |

> **PROTOTYPE TTS** — machine voice `en-US-GuyNeural`. Not teammate VO. Not the Quantic submission.

<video controls src="clips/part3-variant-b-prototype-vo.mp4"></video>

<video controls src="clips/part4-variant-c-prototype-vo.mp4"></video>

<video controls src="clips/part5-shared-close-prototype-vo.mp4"></video>

**Recorded teammate VO:** **Unknown** until Claude, Hiren, or a shared speaker records. These TTS clips do not change that.

---

## 2c. Prototype videos (natural VO — PROTOTYPE TTS natural)

**Prefer this pack for camera.** Technical silent (§2) and technical VO (§2b) stay beside it for post-mortem compare.

**Label:** **PROTOTYPE TTS** natural (`en-US-GuyNeural`) — **not** teammate VO · **not** Quantic submit.

| Asset | Path / URL | Note |
| --- | --- | --- |
| **Part 3 Architecture** | [`clips/part3-variant-b-prototype-vo-natural.mp4`](clips/part3-variant-b-prototype-vo-natural.mp4) (~180s) | Architect why/how timed lines + silence pad. **PROTOTYPE TTS** natural. |
| **Part 4 Coding** | [`clips/part4-variant-c-prototype-vo-natural.mp4`](clips/part4-variant-c-prototype-vo-natural.mp4) (~180s) | Coding why/how timed lines + silence pad. **PROTOTYPE TTS** natural. |
| **Part 5 Shared close** | [`clips/part5-shared-close-prototype-vo-natural.mp4`](clips/part5-shared-close-prototype-vo-natural.mp4) (~60s) | Natural close + pad. **PROTOTYPE TTS** natural. |

> **PROTOTYPE TTS** natural — machine voice `en-US-GuyNeural`. Not teammate VO. Not the Quantic submission. Does not replace technical silent or technical VO.

<video controls src="clips/part3-variant-b-prototype-vo-natural.mp4"></video>

<video controls src="clips/part4-variant-c-prototype-vo-natural.mp4"></video>

<video controls src="clips/part5-shared-close-prototype-vo-natural.mp4"></video>

**Recorded teammate VO:** **Unknown** until Claude, Hiren, or a shared speaker records. These TTS clips do not change that.

---

## 3. Voice-over

| Asset | Path | Status |
| --- | --- | --- |
| Part 3 natural VO (camera) | [Part 3 Variant B VO natural](part3-variant-b-voiceover-natural.md) | Ready to record — architecture why/how, no FR/NFR on camera |
| Part 4 natural VO (camera) | [Part 4 Variant C VO natural](part4-variant-c-voiceover-natural.md) | Ready to record — coding why/how, no FR/NFR on camera |
| Part 5 natural VO (camera) | [Part 5 Shared close VO natural](part5-shared-close-voiceover-natural.md) | Ready to record — updated honesty, plain |
| Part 3 technical VO (compare) | [Part 3 Variant B VO](part3-variant-b-voiceover.md) | Post-mortem (technical + plain twin) |
| Part 4 technical VO (compare) | [Part 4 Variant C VO](part4-variant-c-voiceover.md) | Post-mortem (technical + plain twin) |
| Part 5 technical VO (compare) | [Part 5 Shared close VO](part5-shared-close-voiceover.md) | Post-mortem (updated honesty) |
| Recorded teammate VO | — | **Unknown** until Claude / Hiren / shared records |

---

## 4. Supporting docs (IDs OK here)

| What | Link |
| --- | --- |
| Coverage (grade map) | https://knowledge.cafe.artof.link/coverage.html · [Coverage](coverage.md) |
| Talk cuts (Architecture after Meghna handoff) | https://knowledge.cafe.artof.link/presentation.html · [Talk cuts](presentation.md) |
| Stack / HLD | https://knowledge.cafe.artof.link/stack.html · [Stack](stack.md) |
| Local vs AWS (architect deploy table) | [Local vs AWS MSAIE staging](part3-local-vs-aws.md) |
| Part 3 HLD + Meghna FE/BE (**PROTOTYPE**) | [Part 3 HLD + flow](part3-hld-flow-notes.md) · also on [Stack](stack.md) |
| Part 4 coding overview (**PROTOTYPE**) | [Part 4 coding overview](part4-coding-overview.md) · also on [Stack](stack.md) |
| Quantic hub | https://knowledge.cafe.artof.link/quantic.html · [Quantic](quantic.md) |
| Meghna materials (Part 2 UX/business) | [Meghna materials](meghna-materials.md) |
| Handoff mapping (FR/NFR — **not spoken on camera**) | [Parts 3–5 handoff mapping](parts-345-handoff-mapping.md) |
| Build notes (secondary) | [Parts 3–5 notes](parts-345-notes.md) |
| VO mux notes (**PROTOTYPE TTS** technical) | [Parts 3–5 VO notes](parts-345-vo-notes.md) |

---

## 5. App / staging

- Host: https://cafe.artof.link/ — **staging environment for the MSAIE project** (temporary — not forever)
- Health: https://cafe.artof.link/api/health
- Operator (optional after a live book only): https://cafe.artof.link/operator — read-only helper, not an admin console, **not FR-19**
- Backup: https://54-165-102-60.sslip.io/
- Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22)
- Off-camera ops tracker: Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57)

---

## 6. Still open (not pack-blocking)

- Hiren Architecture vs Coding pick (B vs C) — **Unknown**; do not invent it
- Final Quantic submit video = live must-film + voice (dry-run / silent prototype / **PROTOTYPE TTS** ≠ submit)
- Recorded teammate VO takes stay **Unknown** (**PROTOTYPE TTS** is not that)
- Live Pages GET of these Parts 3–5 URLs stays **Unknown** until merge + Pages deploy

---

*Packed 2026-09-06 Europe/Berlin · talk #97 · PROTOTYPE / samples / rehearsal only · NATURAL architect/coding why-how beside technical originals.*
