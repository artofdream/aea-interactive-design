# Parts 3–5 — build notes

**Built:** 2026-09-06 Europe/Berlin (box UTC morning of Sep 6).  
**Output root:** `/workspace/cafe-fausse-prototype/parts-345/`  
**Do not push to GitHub.** **Not Quantic submit** — labeled PROTOTYPE throughout.

---

## Durations (ffprobe)

| File | Duration | Size (approx) |
| --- | --- | --- |
| `part3-variant-b-prototype-silent.mp4` | **180.02 s** | ~1.8 MB |
| `part4-variant-c-prototype-silent.mp4` | **180.02 s** | ~1.4 MB |
| `part5-shared-close-prototype-silent.mp4` | **60.02 s** | ~0.5 MB |

Codec: H.264 `yuv420p` 1280×720 @ 30 fps + AAC stereo silent (anullsrc). Concat demuxer (same pattern as `meghna-proto-tmp`).

---

## How video was built

1. Downloaded HLD SVGs from `artofdream/aea-interactive-design` `knowledge/assets/` via `gh api`.
2. Converted SVG → PNG with **cairosvg** in a local venv (`parts-345/.venv`).
3. Generated title/coverage/honesty cards with **Pillow**.
4. Extracted / letterboxed reservation still from `/workspace/cafe-fausse-prototype/assets/02-happy-book.mp4`; short 12s silent clip for Part 3 open.
5. Reused existing slides `02`, `08`, `11`, `13`, `15`, `17` fitted to 1280×720 with PROTOTYPE badge.
6. `ffmpeg` still→segment (`libx264 -tune stillimage` + silent AAC) → concat demuxer → final mp4s.

Segment timeline (approx):

**Part 3:** title 8s → happy-book clip 12s → reservation still 8s → start card 8s → AWS staging SVG 40s → as-is SVG 35s → stack slide 15s → boxes 30s → sensors 14s → handoff 10s.

**Part 4:** title 15s → freeze 40s → forms slide 10s → table 40s → NFR-5/6 slide 12s → index slide 8s → timezone/modules 40s → handoff 15s.

**Part 5:** title 8s → shipped 10s → layers slide 8s → **updated honesty** 22s → future slide 7s → end 5s.

---

## Honesty (must match scripts)

| Item | Status in this pack |
| --- | --- |
| **NFR-1** | **Met** — A36 Brave broadband cold Home **466 ms** (#124) |
| **NFR-2** | **Met** — reservation submit **233 ms** (#126) |
| **NFR-7** | **Partial** — do not claim four browsers |
| Host | `cafe.artof.link` = Lightsail staging **#57** — not forever |
| FR-19 | **None** — `/operator` read-only helper only |
| Future #22 / #34–#38 | **Parked** — not grade gaps |

Old presentation.html wording (“NFR-1 / NFR-2 not claimed met”) is **superseded for this pack** by the 2026-09-06 owner update. Scripts and Part 5 cards use the new line.

---

## What this is

- Spoken scripts + ready-to-record VO for Parts 3–5
- Silent **PROTOTYPE** sample videos for rehearsal / timing
- Materials index mirroring Meghna pack shape

## What this is not

- Not the Quantic submission video
- Not recorded teammate voice
- Not a live browser capture of `cafe.artof.link` (reservation open uses existing clip/still + cards)
- Not a GitHub push / Knowledge Pages publish
- Not a claim that Hiren has picked B vs C

---

## Sources used

- https://knowledge.cafe.artof.link/presentation.html (Variant B, C, Shared close)
- https://knowledge.cafe.artof.link/stack.html
- GitHub `knowledge/assets/hld-*.svg`
- `/workspace/cafe-fausse-prototype/slides/*.png`
- `/workspace/cafe-fausse-prototype/assets/02-happy-book.mp4`
- Meghna pack pattern: `MEGHNA-MATERIALS.md` / VO / concat tmp
- Owner honesty UPDATE 2026-09-06 (NFR-1/2 met)

---

## Blockers

None for pack delivery. Optional later: live reservation screenshot from staging if preferred over clip still; recorded VO; Hiren B/C assignment.

---

*End notes.*

## ffprobe raw
```
# part3-variant-b-prototype-silent.mp4
codec_name=h264
codec_type=video
width=1280
height=720
codec_name=aac
codec_type=audio
duration=180.023220
size=1877914

# part4-variant-c-prototype-silent.mp4
codec_name=h264
codec_type=video
width=1280
height=720
codec_name=aac
codec_type=audio
duration=180.023220
size=1432534

# part5-shared-close-prototype-silent.mp4
codec_name=h264
codec_type=video
width=1280
height=720
codec_name=aac
codec_type=audio
duration=60.023220
size=522484

```
