# Parts 3–5 — materials pack (Quantic VIDEO Architecture / Coding / Close)

Everything for the locked five-part talk (#97) after Meghna’s cafe demo:

| Clock (room) | Part | Who | This pack |
| --- | --- | --- | --- |
| ~3:30–6:30 | **3 Architecture** (Variant B) | Claude or Hiren | scripts + silent ~180s + tech TTS + **NATURAL TTS** |
| ~6:30–9:30 | **4 Coding** (Variant C) | the other | scripts + silent ~180s + tech TTS + **NATURAL TTS** |
| ~9:30–10:00 | **5 Shared close** | Shared | scripts + silent ~60s + tech TTS + **NATURAL TTS** |

**Label:** all videos are **PROTOTYPE** — not Quantic submission.

### Speaking rule (owner)

- **On camera / preferred VO:** clear, accurate, **natural demo language** (`*-NATURAL.md`, `*-vo-natural.mp4`).
- **Demo focus:** **cafe.artof.link** — prefer **staging environment for the MSAIE project** (or “MSAIE staging environment”).
- **Architecture comparison (Part 3):** **Local (dev) vs AWS MSAIE staging** — see [`PART3-LOCAL-VS-AWS.md`](PART3-LOCAL-VS-AWS.md) (honest cut: same React+JSX→Flask→Postgres both sides; local cts-ai; staging Lightsail/Caddy/on-box PG not AEA RDS; newsletter store-only until SES). Spoken beats stay MSAIE / cafe.artof.link; ops names in the markdown table only.
- **Avoid on camera:** FR/NFR IDs, issue numbers, SHA, CI job names, “weekend Lightsail staging”, and heavy Lightsail / Route53 / Caddy ops jargon.
- **ID / freeze / probe mapping** lives in [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) — not in natural Timed lines.
- **Technical scripts + technical VO mp4s** kept for post-mortem / ID-ok rehearsal (`PART*-SCRIPT.md`, `*-prototype-vo.mp4`) — **unchanged**.
- Still accurate: no invented requirements; no claiming four-browser complete; `cafe.artof.link` is temporary MSAIE staging not forever; operator is read-only helper not admin; SES outbound is Future (not in spoken grade story unless optional).
- Speakable honesty: load/submit timings **met** on phone broadband probe; browser support still **partial**; Future items **parked**.

**Honesty UPDATE (2026-09-06):** NFR-1/2 **met** (probes in handoff); NFR-7 **Partial**; staging #57 not forever; no FR-19; Futures parked.  
**Wording lock UPDATE (2026-09-06):** MSAIE staging phrase + Local vs AWS MSAIE staging on NATURAL track; no “weekend Lightsail” on camera. **Honest cut UPDATE:** PART3-LOCAL-VS-AWS.md encodes cts-ai local + Lightsail/Caddy/on-box Postgres (host tip `73d202d`); NATURAL VO lightly fixed (no Docker-style local claim).


---

## 1. Scripts + talking points

| File | What |
| --- | --- |
| [`PART3-VARIANT-B-SCRIPT-NATURAL.md`](PART3-VARIANT-B-SCRIPT-NATURAL.md) | **Preferred spoken** ~3 min Architecture (natural) |
| [`PART4-VARIANT-C-SCRIPT-NATURAL.md`](PART4-VARIANT-C-SCRIPT-NATURAL.md) | **Preferred spoken** ~3 min Coding (natural) |
| [`PART5-SHARED-CLOSE-SCRIPT-NATURAL.md`](PART5-SHARED-CLOSE-SCRIPT-NATURAL.md) | **Preferred spoken** ~30–60s close (natural) |
| [`PART3-VARIANT-B-SCRIPT.md`](PART3-VARIANT-B-SCRIPT.md) | Technical / ID-ok Architecture (post-mortem) |
| [`PART4-VARIANT-C-SCRIPT.md`](PART4-VARIANT-C-SCRIPT.md) | Technical / ID-ok Coding (post-mortem) |
| [`PART5-SHARED-CLOSE-SCRIPT.md`](PART5-SHARED-CLOSE-SCRIPT.md) | Technical / ID-ok close (post-mortem) |
| [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) | **Off-camera** FR/NFR / freeze / probe ID map |
| [`PART3-LOCAL-VS-AWS.md`](PART3-LOCAL-VS-AWS.md) | Local (cts-ai Flask/Vite/Postgres) vs AWS MSAIE staging (Lightsail/Caddy/on-box PG — off-camera); what / why / how |

Knowledge talk cuts: https://knowledge.cafe.artof.link/presentation.html  
Stack / HLD: https://knowledge.cafe.artof.link/stack.html

---

## 2. Prototype videos (silent)

| Asset | Path | Duration |
| --- | --- | --- |
| Part 3 Architecture | `/workspace/cafe-fausse-prototype/parts-345/part3-variant-b-prototype-silent.mp4` | ~180s |
| Part 4 Coding | `/workspace/cafe-fausse-prototype/parts-345/part4-variant-c-prototype-silent.mp4` | ~180s |
| Part 5 Shared close | `/workspace/cafe-fausse-prototype/parts-345/part5-shared-close-prototype-silent.mp4` | ~60s |

Format: 1280×720 H.264 + silent AAC.

### 2b. NATURAL VO-integrated (preferred PROTOTYPE TTS)

| Asset | Path | Duration |
| --- | --- | --- |
| Part 3 + natural TTS | `/workspace/cafe-fausse-prototype/parts-345/part3-variant-b-prototype-vo-natural.mp4` | ~180s |
| Part 4 + natural TTS | `/workspace/cafe-fausse-prototype/parts-345/part4-variant-c-prototype-vo-natural.mp4` | ~180s |
| Part 5 + natural TTS | `/workspace/cafe-fausse-prototype/parts-345/part5-shared-close-prototype-vo-natural.mp4` | ~60s |

**Label:** **PROTOTYPE TTS** (`en-US-GuyNeural`) — natural-language Timed lines · IDs in handoff only · not teammate VO · not Quantic submit.

### 2c. Technical VO-integrated (post-mortem; IDs OK — unchanged)

| Asset | Path | Duration |
| --- | --- | --- |
| Part 3 + tech TTS | `/workspace/cafe-fausse-prototype/parts-345/part3-variant-b-prototype-vo.mp4` | ~180s |
| Part 4 + tech TTS | `/workspace/cafe-fausse-prototype/parts-345/part4-variant-c-prototype-vo.mp4` | ~180s |
| Part 5 + tech TTS | `/workspace/cafe-fausse-prototype/parts-345/part5-shared-close-prototype-vo.mp4` | ~64.5s |

See [`PARTS-345-VO-NOTES.md`](PARTS-345-VO-NOTES.md).

---

## 3. Voice-over

| Asset | Path | Status |
| --- | --- | --- |
| Part 3 NATURAL VO | [`PART3-VARIANT-B-VOICEOVER-NATURAL.md`](PART3-VARIANT-B-VOICEOVER-NATURAL.md) | Preferred Timed lines |
| Part 4 NATURAL VO | [`PART4-VARIANT-C-VOICEOVER-NATURAL.md`](PART4-VARIANT-C-VOICEOVER-NATURAL.md) | Preferred Timed lines |
| Part 5 NATURAL VO | [`PART5-SHARED-CLOSE-VOICEOVER-NATURAL.md`](PART5-SHARED-CLOSE-VOICEOVER-NATURAL.md) | Preferred Timed lines |
| Part 3 tech VO | [`PART3-VARIANT-B-VOICEOVER.md`](PART3-VARIANT-B-VOICEOVER.md) | Technical + plain twin (post-mortem) |
| Part 4 tech VO | [`PART4-VARIANT-C-VOICEOVER.md`](PART4-VARIANT-C-VOICEOVER.md) | Technical + plain twin (post-mortem) |
| Part 5 tech VO | [`PART5-SHARED-CLOSE-VOICEOVER.md`](PART5-SHARED-CLOSE-VOICEOVER.md) | Technical + updated honesty (post-mortem) |
| Narration NATURAL | `vo/*-vo-natural.{txt,wav,mp3}` | Built for natural TTS mux |
| Narration technical | `vo/*-vo.{txt,wav,mp3}` | Technical / extracted from tech mp4 |
| Handoff ID map | [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) | Off-camera only |
| VO build notes | [`PARTS-345-VO-NOTES.md`](PARTS-345-VO-NOTES.md) | Natural + technical tracks |
| Recorded teammate VO | — | **Unknown** until Claude/Hiren/shared records |

---

## 4. Supporting visuals in this folder

| What | Files |
| --- | --- |
| HLD PNGs (from GitHub SVGs) | `hld-aws-staging-720.png`, `hld-as-is-720.png`, `hld-to-be-720.png` (+ raw `.svg`) |
| Cards | `card-p3-*.png`, `card-p4-*.png`, `card-p5-*.png` |
| Reservation look | `still-reservation-720.png` (from `assets/02-happy-book.mp4`) |
| Reused slides (fitted) | `fit-02-stack.png`, `fit-08-forms.png`, `fit-11-nfr56.png`, `fit-13-index.png`, `fit-15-layers.png`, `fit-17-future.png` |

---

## 5. Sister packs / docs

| What | Link / path |
| --- | --- |
| Meghna materials (Part 2) | `/workspace/cafe-fausse-prototype/MEGHNA-MATERIALS.md` |
| Coverage | https://knowledge.cafe.artof.link/coverage.html |
| Presentation | https://knowledge.cafe.artof.link/presentation.html |
| Stack | https://knowledge.cafe.artof.link/stack.html |
| Live staging | https://cafe.artof.link/ (MSAIE staging environment — temporary, not forever) |
| Local vs AWS (Knowledge / handoff) | [`PART3-LOCAL-VS-AWS.md`](PART3-LOCAL-VS-AWS.md) — Lightsail/Caddy/on-box PG OK here |
| Build notes | [`PARTS-345-NOTES.md`](PARTS-345-NOTES.md) |
| Handoff ID map | [`PARTS-345-HANDOFF-MAPPING.md`](PARTS-345-HANDOFF-MAPPING.md) |

---

## 6. Still open (not pack-blocking)

- Hiren Architecture vs Coding pick (B vs C)
- Final Quantic submit = live must-film + recorded voice (this silent pack ≠ submit)
- Recorded VO takes

---

*Packed 2026-09-06 Europe/Berlin · talk #97 · PROTOTYPE only · NATURAL spoken track beside technical originals.*

*Packed 2026-09-06 Europe/Berlin · talk #97 · PROTOTYPE only · NATURAL spoken track · MSAIE staging + Local vs AWS wording lock.*
