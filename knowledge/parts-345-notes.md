# Parts 3–5 — build notes (secondary)

Public index for teammates: [Parts 3–5 materials](parts-345-materials.md).  
This page is **build notes only**. Silent clips live under `knowledge/clips/`. **PROTOTYPE** / rehearsal — not Quantic submit.

**Built:** 2026-09-06 Europe/Berlin.

---

## Durations (ffprobe)

| File | Duration | Size (approx) |
| --- | --- | --- |
| [`clips/part3-variant-b-prototype-silent.mp4`](clips/part3-variant-b-prototype-silent.mp4) | **180.02 s** | ~1.8 MB |
| [`clips/part4-variant-c-prototype-silent.mp4`](clips/part4-variant-c-prototype-silent.mp4) | **180.02 s** | ~1.4 MB |
| [`clips/part5-shared-close-prototype-silent.mp4`](clips/part5-shared-close-prototype-silent.mp4) | **60.02 s** | ~0.5 MB |

Codec: H.264 `yuv420p` 1280×720 @ 30 fps + AAC stereo silent (anullsrc). Same concat pattern as the Meghna silent prototype.

---

## How video was built

1. HLD SVGs from `knowledge/assets/` (`hld-aws-staging.svg`, `hld-as-is.svg`, `hld-to-be.svg`).
2. SVG → PNG (cairosvg). Title / coverage / honesty cards (Pillow).
3. Reservation still from the existing happy-book clip; reused fitted slides with a **PROTOTYPE** badge.
4. `ffmpeg` still→segment (`libx264 -tune stillimage` + silent AAC) → concat → final mp4s.

Segment timeline (approx):

**Part 3:** title 8s → happy-book clip 12s → reservation still 8s → start card 8s → AWS staging SVG 40s → as-is SVG 35s → stack slide 15s → boxes 30s → sensors 14s → handoff 10s.

**Part 4:** title 15s → freeze 40s → forms slide 10s → table 40s → NFR-5/6 slide 12s → index slide 8s → timezone/modules 40s → handoff 15s.

**Part 5:** title 8s → shipped 10s → layers slide 8s → **updated honesty** 22s → future slide 7s → end 5s.

---

## Honesty (must match [Coverage](coverage.md) / scripts)

| Item | Status in this pack |
| --- | --- |
| **NFR-1** | **met** — A36 Brave broadband cold Home **466 ms** ([#124](https://github.com/artofdream/aea-interactive-design/pull/124)) |
| **NFR-2** | **met** — reservation submit **233 ms** ([#126](https://github.com/artofdream/aea-interactive-design/pull/126)) |
| **NFR-7** | **Partial** — do not claim four browsers |
| Host | `cafe.artof.link` = Lightsail staging **#57** — not forever |
| FR-19 | **None** — `/operator` read-only helper only |
| Future #22 / #34–#38 | **Parked** — not grade gaps |
| Recorded VO | **Unknown** |

Old Talk-cuts wording (“NFR-1 / NFR-2 not claimed met”) is **superseded** by the 2026-09-06 update.

---

## What this is / is not

- Spoken scripts + ready-to-record VO for Parts 3–5, plus silent **PROTOTYPE** samples for rehearsal / timing.
- **Not** the Quantic submission, not recorded teammate voice, not a live browser capture of `cafe.artof.link`, and not a Hiren B vs C pick.

---

*End notes · talk #97 · PROTOTYPE only.*
