# Meghna’s Café Fausse — Quantic video part pack (3 minutes)

**Who this is for:** Meghna (teammate). Plain English.  
**Job:** Live walk of the restaurant site so the room sees FR/NFR fulfillment.  
**Then:** Hand the mic to the **Architecture (Variant B)** person at the end of Reservations.  
**Built from:** team notes 2026-09-05 · companion maps on Knowledge.

---

## 1. TLDR (≈30s read)

You have **3 minutes** on the live share **`https://cafe.artof.link/`**.

**Click path (locked):** **Home → Gallery → Menu → Reservations**.

**Say:** this is Lightsail **staging** for the weekend (#57) — **not** production forever. Point at real freeze copy and prices on screen. On Menu, if you show **Bruschetta ($8.50)**, say honestly there is **no matching photo**.

**Do not claim:** NFR-1 or NFR-2 met · NFR-7 as four browsers · `/operator` as FR-19 · inventing FR-19.

**Optional if time left:** happy book → `/operator`, newsletter, or full-slot **409** (see §4). Otherwise stop at the form look and **hand off to Architecture**.

---

## 2. Timed beat sheet (~180s)

| Clock | Dur | Beat | What you do |
| ---: | ---: | --- | --- |
| **0:00–0:20** | 20s | Open | Open `https://cafe.artof.link/`. One breath: “Café Fausse live share — Home → Gallery → Menu → Reservations. Staging for this session, not forever.” |
| **0:20–0:55** | 35s | **Home** | Scroll Visit / Hours / Explore. Point at name, address, phone, hours. Tap nav icons once so the room sees Menu / Gallery / Reservations / About. |
| **0:55–1:30** | 35s | **Gallery** | Nav → **Gallery**. Click one image for lightbox; scroll awards + a review quote. |
| **1:30–2:15** | 45s | **Menu** | Nav → **Menu**. Starters → **Bruschetta $8.50** — say “no matching photo.” Point at one main (e.g. Grilled Salmon) — price from the page. |
| **2:15–2:50** | 35s | **Reservations** | Nav → **Reservations**. Show fields (date, slot, guests, name, email, phone). Say what a happy book / full book would mean — **do not** invent a write unless you run an optional extra. |
| **2:50–3:00** | 10s | **Handoff** | Spoken line in §5. Stop sharing the mic for Architecture (Variant B). |

**Room clock tip:** if you are already at **2:40** on Menu, skip extras and go straight to Reservations + handoff.

---

## 3. Per page — click, say, FR/NFR (honest)

### Honesty lines (say once early, or at Reservations)

- **NFR-1 / NFR-2:** **not claimed met** (local Vite timings are notes only).
- **NFR-7:** **partial** — Edge + Firefox home probed; Chrome / Safari **Unknown**. Not a four-browser pass.
- **Host:** `cafe.artof.link` = Lightsail staging share for this weekend — **not** production forever. Tear-down only if the owner asks.
- **`/operator`:** read-only recording helper — **not FR-19**, not an admin console (no cancel / CRUD).

Grade floor = official SRS only: **FR-1..FR-18**, **NFR-1..NFR-9**. Do not invent IDs.

---

### Home (`/` ) — ~0:20–0:55

| Do | Say (plain) | Point at |
| --- | --- | --- |
| Land on Home; short scroll | “Home: restaurant name, how to reach us, when we’re open.” | Name, contact, hours cards |
| Hover / show top nav | “Nav to Menu, Reservations, About, Gallery — same five-page floor.” | Nav links / icons |

**FR:** **FR-1** name · **FR-2** contact · **FR-3** hours · **FR-4** nav  
**NFR (light touch):** **NFR-3** theme · **NFR-4** layout (Flex/Grid) · **NFR-8** nav / viewports — “looks intentional; we are not claiming speed budgets NFR-1/2.”

---

### Gallery (`/gallery`) — ~0:55–1:30

| Do | Say (plain) | Point at |
| --- | --- | --- |
| Nav → **Gallery** | “Gallery: official photos of the place and food.” | Image grid (**FR-12**) |
| Click one thumbnail → lightbox → close | “Lightbox for a closer look.” | Enlarged image (**FR-13**) |
| Scroll awards + reviews | “Awards and guest quotes from the freeze — we don’t rewrite them.” | Awards / quotes (**FR-14**) |

**FR:** **FR-12**, **FR-13**, **FR-14**  
**Skip if tight:** second lightbox click. One open/close is enough.

---

### Menu (`/menu`) — ~1:30–2:15

| Do | Say (plain) | Point at |
| --- | --- | --- |
| Nav → **Menu** | “Menu categories and prices come from the freeze file — we don’t invent prices.” | Categories (**FR-5**) |
| Starters → **Bruschetta** | “Bruschetta, eight-fifty — **honestly, no matching photo** for this item.” | Name + **$8.50** on screen |
| Optional one main | “Grilled Salmon — price as printed on the page.” | **$22.00** (or whatever the page shows) |

**FR:** **FR-5**  
**Must say if Bruschetta is on camera:** **no matching photo**. Photos are presentation aids; do not pretend every dish has a dedicated shot.

Other freeze talk picks (prices from page only): Caesar Salad $9.00 · Ribeye Steak $28.00 · Tiramisu $7.50 · Espresso $3.00.

---

### Reservations (`/reservations`) — ~2:15–2:50

| Do | Say (plain) | Point at |
| --- | --- | --- |
| Nav → **Reservations** | “Booking form: date, time slot, guests, name, email, optional phone.” | Form fields (**FR-6**) |
| Open date / slot list if needed | “Only valid future slots for DC hours — Sunday ends earlier.” | Slot picker (**FR-7**) |
| Finger-point at Reserve button (no submit unless optional) | “Happy path: random table **1–30**, success banner. Full slot: honest **no** — no guessed 31st table.” | Button + page honesty note |
| One line on backend (no deep dive — Architecture owns that) | “When Postgres accepts it, Customers + Reservations get the row. Fail-closed if the DB can’t take the write.” | Page note / form (**FR-8**, **FR-9**, **FR-17**, **FR-18**, **NFR-5**, **NFR-6**) |

**Default for the 3-min cut:** **show the form; do not submit** unless you have buffer for an optional extra (§4).  
**Do not** open `/operator` in the core path unless you just completed a happy book (optional).

---

## 4. Optional must-film extras (only if time)

Mark these **OPTIONAL**. Core pack stops at Reservations look + handoff. Full click paths: [Must-film shots](MUST-FILM-SHOTS.md).

| Extra | When | What | Freeze IDs | Time |
| --- | --- | --- | ---: |
| **Happy book → `/operator`** | ≥45s left after form look | Unique email → Reserve → green “Table N” → open `/operator` → point at new row. Say: “**not FR-19**.” | FR-6..9, FR-17..18 | ~70–90s |
| **Newsletter** | ≥40s left | Footer subscribe with fresh email → `/operator` **Newsletter only** | FR-15, FR-16 | ~45–60s |
| **Full-book 409** | Pre-staged 30 tables off-mic | 31st attempt → banner “fully booked” / Network **409** | FR-9, NFR-5 | ~40–60s on cam |

If staging is slow or a write fails: **do not invent success**. Fall back to Coverage cite or committed clip **02-happy-book** as a **look only**.

---

## 5. Spoken handoff line (Architecture / Variant B)

Say this (or close) at **~2:50**, still on Reservations or after a quick honesty breath:

> “That’s the live path — Home, Gallery, Menu, Reservations — showing the freeze requirements on staging. I’m handing off to Architecture for **Variant B**: how React, Flask, and Postgres fit together, the diagrams, and how Coverage maps the boxes. Over to you.”

Then stop talking. Let Architecture take the screen (HLD / Coverage / sensors).

---

## 6. Links (keep this tab list open)

| What | URL | Note |
| --- | --- | --- |
| **Live café (your surface)** | https://cafe.artof.link/ | Prefer this share. Staging #57 — not forever. |
| **Operator (helper)** | https://cafe.artof.link/operator | Read-only. **Not FR-19.** Not in primary nav. |
| **Knowledge — Coverage** | https://knowledge.cafe.artof.link/coverage.html | Every FR/NFR + evidence. |
| **Knowledge — Must-film shots** | https://knowledge.cafe.artof.link/ (see must-film / video script) · local pack: `MUST-FILM-SHOTS.md` | Happy book / newsletter / 409 / NFR-6. |
| **Knowledge — Quantic hub** | https://knowledge.cafe.artof.link/quantic.html | Navigation hub only — does not invent IDs. |
| **Presentation (Variant B)** | https://knowledge.cafe.artof.link/presentation.html | Architecture cut after your handoff. |
| **Health (mute pre-flight)** | https://cafe.artof.link/api/health | Expect `{"ok":true}` before you go live. |

Backup host (if needed): `https://54-165-102-60.sslip.io/` — same honesty (staging, not forever).

---

## 7. Bruschetta reminder

If **Menu** is on camera and you point at **Bruschetta**:

- Price from the page: **$8.50** (do not invent).
- Say out loud: **“no matching photo.”**
- Do not apologize into a fake stock image story — honesty is the grade story.

---

## 8. Do-not-say checklist

- “`/operator` is FR-19” / “admin console”
- “`cafe.artof.link` is production forever” / “live Café Fausse forever”
- “NFR-1 met” / “NFR-2 met”
- “NFR-7 pass on Chrome, Firefox, Safari, and Edge”
- Invented prices or a guessed table on a full slot
- Any invented requirement ID (including FR-19)

---

## Pre-flight (30s, mute)

1. `GET https://cafe.artof.link/api/health` → `{"ok":true}`  
2. Click through Home → Gallery → Menu → Reservations once (cold cache).  
3. Confirm Architecture person is ready for Variant B at your handoff.  
4. Optional: warm `/operator` only if you plan a happy-book extra.

---

*End of Meghna 3-min Café demo pack. Path locked 2026-09-05. No FR-19 invented.*
