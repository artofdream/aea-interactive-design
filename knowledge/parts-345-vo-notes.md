# Parts 3–5 — VO integration notes (PROTOTYPE TTS)

**Label:** **PROTOTYPE TTS** (`en-US-GuyNeural`) — **not** teammate VO · **not** Quantic submit.  
Public index: [Parts 3–5 materials](parts-345-materials.md) (§2 silent · §2b VO-integrated).  
**Honesty:** unchanged from scripts (**NFR-1** / **NFR-2** **met** via probes [#124](https://github.com/artofdream/aea-interactive-design/pull/124) / [#126](https://github.com/artofdream/aea-interactive-design/pull/126); **NFR-7** **Partial**; staging [#57](https://github.com/artofdream/aea-interactive-design/issues/57) not forever; Futures parked; no FR-19).  
**Built:** 2026-09-06 Europe/Berlin (UTC+2)

---

## TTS

| Setting | Value |
| --- | --- |
| Engine | `edge-tts` (pip) |
| Voice | `en-US-GuyNeural` (clear English, technical) |
| Rate | `+0%` |
| Source lines | **Timed lines (technical — IDs OK)** from [Part 3 VO](part3-variant-b-voiceover.md) · [Part 4 VO](part4-variant-c-voiceover.md) · [Part 5 VO](part5-shared-close-voiceover.md) (not the plain-English twins) |
| Pack-local scripts / wav | Coordinator box only — **not** published on this site. Pages hosts the muxed mp4s. |
| Pause between paragraphs | ~900 ms silence |

---

## Duration match

| Part | Silent video | Raw VO | Mux strategy | VO-integrated mp4 |
| --- | --- | --- | --- | --- |
| 3 Variant B | [silent](clips/part3-variant-b-prototype-silent.mp4) ~180.02 s | ~91.54 s | Pad audio with silence (`apad`) to video length | [VO](clips/part3-variant-b-prototype-vo.mp4) ~180.02 s |
| 4 Variant C | [silent](clips/part4-variant-c-prototype-silent.mp4) ~180.02 s | ~101.21 s | Pad audio with silence (`apad`) to video length | [VO](clips/part4-variant-c-prototype-vo.mp4) ~180.02 s |
| 5 Shared close | [silent](clips/part5-shared-close-prototype-silent.mp4) ~60.02 s | ~64.50 s | Pad video last-frame (`tpad` clone) ~4.48 s (under 5 s rule) | [VO](clips/part5-shared-close-prototype-vo.mp4) ~64.50 s |

Silent `*-silent.mp4` files were **not** overwritten.

---

## Outputs (ffprobe)

### [`clips/part3-variant-b-prototype-vo.mp4`](clips/part3-variant-b-prototype-vo.mp4)

- Format duration: **180.022 s**
- Video: H.264 1280×720 ~180.000 s
- Audio: AAC ~180.011 s (VO then silence pad)

### [`clips/part4-variant-c-prototype-vo.mp4`](clips/part4-variant-c-prototype-vo.mp4)

- Format duration: **180.022 s**
- Video: H.264 1280×720 ~180.000 s
- Audio: AAC ~180.011 s (VO then silence pad)

### [`clips/part5-shared-close-prototype-vo.mp4`](clips/part5-shared-close-prototype-vo.mp4)

- Format duration: **64.500 s**
- Video: H.264 1280×720 ~64.467 s (original ~60 s + last-frame pad)
- Audio: AAC ~64.500 s (full technical close script)

---

## What this is / is not

| Is | Is not |
| --- | --- |
| Rehearsal / timing prototype with machine VO | Quantic submission film |
| Technical ID-ok narration from the VO markdown | Teammate (Claude/Hiren) recorded VO |
| Same honesty lines as the Part 5 script | Old Unknown NFR-1/2 wording |

**Recorded teammate VO** remains **Unknown** until Claude / Hiren / shared records.

---

*End VO notes · PROTOTYPE TTS only.*
