# Parts 3–5 — materials pack (Quantic VIDEO Architecture / Coding / Close)

Everything for the locked five-part talk ([#97](https://github.com/artofdream/aea-interactive-design/issues/97)) after Meghna’s cafe demo.

| Clock (room) | Part | Who | This pack |
| --- | --- | --- | --- |
| ~3:30–6:30 | **3 Architecture** (Variant B) | Claude or Hiren | [script](part3-variant-b-script.md) + [VO](part3-variant-b-voiceover.md) + silent ~180s + [PROTOTYPE TTS](clips/part3-variant-b-prototype-vo.mp4) |
| ~6:30–9:30 | **4 Coding** (Variant C) | the other | [script](part4-variant-c-script.md) + [VO](part4-variant-c-voiceover.md) + silent ~180s + [PROTOTYPE TTS](clips/part4-variant-c-prototype-vo.mp4) |
| ~9:30–10:00 | **5 Shared close** | Shared | [script](part5-shared-close-script.md) + [VO](part5-shared-close-voiceover.md) + silent ~60s + [PROTOTYPE TTS](clips/part5-shared-close-prototype-vo.mp4) |

**Label:** silent videos are **PROTOTYPE** / samples / rehearsal. VO-integrated clips are **PROTOTYPE TTS** (`en-US-GuyNeural`) — **not** teammate VO · **not** Quantic submission.  
**Owner rule:** technical spoken scripts **may use FR/NFR IDs**; plain-English VO twins included.  
**Hiren B vs C pick:** **Unknown** — do not invent it.

---

## Honesty (must match [Coverage](coverage.md))

| Item | Status | Probe / cite |
| --- | --- | --- |
| **NFR-1** | **met** | A36 Brave broadband cold Home **466 ms** ([#123](https://github.com/artofdream/aea-interactive-design/issues/123) / [PR #124](https://github.com/artofdream/aea-interactive-design/pull/124)) |
| **NFR-2** | **met** | Reservation submit **233 ms** ([#125](https://github.com/artofdream/aea-interactive-design/issues/125) / [PR #126](https://github.com/artofdream/aea-interactive-design/pull/126)) |
| **NFR-7** | **Partial** | Do **not** claim four browsers |
| Host | Lightsail staging **#57** | `https://cafe.artof.link/` — **not forever** |
| FR-19 | **None** | `/operator` is a read-only helper |
| Future #22 / #34–#38 | **Parked** | Not grade gaps |
| Recorded teammate VO | **Unknown** | Until Claude / Hiren / shared records |

Do **not** use the old “NFR-1 / NFR-2 Unknown / not claimed met” line.

---

## 1. Script + talking points

| File | What |
| --- | --- |
| [Part 3 — Variant B script](part3-variant-b-script.md) | Timed ~3 min Architecture beats, diagram callouts, ID map |
| [Part 4 — Variant C script](part4-variant-c-script.md) | Timed ~3 min Coding beats (freeze/CI, table/fail-closed, TZ/modules) |
| [Part 5 — Shared close script](part5-shared-close-script.md) | Timed ~30–60s close with **updated** honesty |
| Knowledge (this site) | [Talk cuts](presentation.md) · [Quantic hub](quantic.md) · [Meghna materials](meghna-materials.md) (Part 2) |

Live site to rehearse after the cafe demo: **https://cafe.artof.link/**

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

## 2b. Prototype videos (VO-integrated — PROTOTYPE TTS)

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

## 3. Voice-over

| Asset | Path | Status |
| --- | --- | --- |
| Part 3 VO | [Part 3 Variant B VO](part3-variant-b-voiceover.md) | Ready to record (technical + plain twin) |
| Part 4 VO | [Part 4 Variant C VO](part4-variant-c-voiceover.md) | Ready to record (technical + plain twin) |
| Part 5 VO | [Part 5 Shared close VO](part5-shared-close-voiceover.md) | Ready to record (updated honesty) |
| Recorded teammate VO | — | **Unknown** until Claude / Hiren / shared records |

---

## 4. Supporting docs (IDs OK here)

| What | Link |
| --- | --- |
| Coverage (grade map) | https://knowledge.cafe.artof.link/coverage.html · [Coverage](coverage.md) |
| Talk cuts (Architecture after Meghna handoff) | https://knowledge.cafe.artof.link/presentation.html · [Talk cuts](presentation.md) |
| Stack / HLD | https://knowledge.cafe.artof.link/stack.html · [Stack](stack.md) |
| Quantic hub | https://knowledge.cafe.artof.link/quantic.html · [Quantic](quantic.md) |
| Meghna materials (Part 2) | [Meghna materials](meghna-materials.md) |
| Build notes (secondary) | [Parts 3–5 notes](parts-345-notes.md) |
| VO mux notes (**PROTOTYPE TTS**) | [Parts 3–5 VO notes](parts-345-vo-notes.md) |

---

## 5. App / staging

- Host: https://cafe.artof.link/ (Lightsail staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) — not forever)
- Health: https://cafe.artof.link/api/health
- Operator (optional after a live book only): https://cafe.artof.link/operator — read-only helper, not an admin console, **not FR-19**
- Backup: https://54-165-102-60.sslip.io/
- Permanent hosting stays [#22](https://github.com/artofdream/aea-interactive-design/issues/22)

---

## 6. Still open (not pack-blocking)

- Hiren Architecture vs Coding pick (B vs C) — **Unknown**; do not invent it
- Final Quantic submit video = live must-film + voice (dry-run / silent prototype / **PROTOTYPE TTS** ≠ submit)
- Recorded teammate VO takes stay **Unknown** (**PROTOTYPE TTS** is not that)
- Live Pages GET of these Parts 3–5 URLs stays **Unknown** until merge + Pages deploy

---

*Packed 2026-09-06 Europe/Berlin · talk #97 · PROTOTYPE / samples / rehearsal only.*
