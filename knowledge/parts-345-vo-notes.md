# Parts 3–5 — VO integration notes (PROTOTYPE TTS)

**Label:** **PROTOTYPE TTS** — not teammate VO · not Quantic submit.  
**Honesty:** unchanged from scripts (NFR-1/2 **met** via probes #124 / #126; NFR-7 **Partial**; staging #57 not forever; Futures parked; no FR-19).  
**Built:** 2026-09-06 Europe/Berlin (UTC+2)

---

## TTS

| Setting | Value |
| --- | --- |
| Engine | `edge-tts` (pip) |
| Voice | `en-US-GuyNeural` (clear English, technical) |
| Rate | `+0%` |
| Source lines | **Timed lines (technical — IDs OK)** from each `*-VOICEOVER.md` (not plain-English twin) |
| Scripts | `/workspace/cafe-fausse-prototype/parts-345/vo/*.txt` |
| Raw audio | `/workspace/cafe-fausse-prototype/parts-345/vo/*.wav` (+ `.mp3`) |
| Pause between paragraphs | ~900 ms silence |

---

## Duration match

| Part | Silent video | Raw VO WAV | Mux strategy | VO-integrated mp4 |
| --- | --- | --- | --- | --- |
| 3 Variant B | ~180.02 s | 91.54 s | Pad audio with silence (`apad`) to video length | ~180.02 s |
| 4 Variant C | ~180.02 s | 101.21 s | Pad audio with silence (`apad`) to video length | ~180.02 s |
| 5 Shared close | ~60.02 s | 64.50 s | Pad video last-frame (`tpad` clone) ~4.48 s (&lt;5 s rule) | ~64.50 s |

Silent `*-silent.mp4` files were **not** overwritten.

---

## Outputs (ffprobe)

### `/workspace/cafe-fausse-prototype/parts-345/part3-variant-b-prototype-vo.mp4`

- Format duration: **180.022 s**
- Video: H.264 1280×720 ~180.000 s
- Audio: AAC ~180.011 s (VO then silence pad)

### `/workspace/cafe-fausse-prototype/parts-345/part4-variant-c-prototype-vo.mp4`

- Format duration: **180.022 s**
- Video: H.264 1280×720 ~180.000 s
- Audio: AAC ~180.011 s (VO then silence pad)

### `/workspace/cafe-fausse-prototype/parts-345/part5-shared-close-prototype-vo.mp4`

- Format duration: **64.500 s**
- Video: H.264 1280×720 ~64.467 s (original ~60 s + last-frame pad)
- Audio: AAC ~64.500 s (full technical close script)

---

## What this is / is not

| Is | Is not |
| --- | --- |
| Rehearsal / timing prototype with machine VO | Quantic submission film |
| Technical ID-ok narration from VO markdown | Teammate (Claude/Hiren) recorded VO |
| Same honesty lines as Part 5 script | Old Unknown NFR-1/2 wording |

Recorded teammate VO remains **Unknown** until Claude/Hiren/shared records.

---

*End VO notes · PROTOTYPE TTS only.*
