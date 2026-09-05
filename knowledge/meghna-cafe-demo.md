# Meghna’s Café Fausse — Quantic video part pack (3 minutes)

**Who this is for:** Meghna (teammate).  
**Job:** Live walk of the restaurant site so the room sees the product working.  
**Then:** Hand the mic to the **Architecture** person at the end of Reservations.  
**Built from:** team notes 2026-09-05.

**Owner rule (2026-09-05):**  
- **Spoken script / what Meghna says on camera:** plain English only — **no FR / NFR jargon**.  
- **Supporting notes** (this doc’s mapping tables, Coverage, slides): FR/NFR IDs are fine.

---

## 1. TLDR (≈30s read)

You have **3 minutes** on the live share **`https://cafe.artof.link/`**.

**Click path (locked):** **Home → Gallery → Menu → Reservations**.

**Say on camera:** this is a temporary staging share for the weekend — not the forever restaurant host. Point at real copy and prices on screen. On Menu, if you show **Bruschetta ($8.50)**, say honestly there is **no matching photo**.

**Do not say on camera:** requirement code names, “NFR-1 met,” “four browsers pass,” “operator is an admin feature,” or inventing extra requirements.

**Optional if time left:** book a table → check the read-only operator page, newsletter signup, or a full-slot “sorry, fully booked” (see §4). Otherwise stop at the form look and **hand off to Architecture**.

---

## 2. Spoken script — timed beat sheet (~180s)

*Say only the “Say” column out loud. No requirement codes in speech.*

| Clock | Dur | Beat | Do | Say (plain English) |
| ---: | ---: | --- | --- | --- |
| **0:00–0:20** | 20s | Open | Open `https://cafe.artof.link/` | “Here’s Café Fausse live. I’ll walk Home, Gallery, Menu, then Reservations. This host is staging for the weekend — not forever.” |
| **0:20–0:55** | 35s | **Home** | Scroll Visit / Hours / Explore; show top nav | “Home shows the restaurant name, how to reach us, and when we’re open. Nav goes to Menu, Gallery, Reservations, and About.” |
| **0:55–1:30** | 35s | **Gallery** | Nav → Gallery; one lightbox; awards + a review | “Gallery uses the official photos. Lightbox for a closer look. Awards and guest quotes are the freeze text — we don’t rewrite them.” |
| **1:30–2:15** | 45s | **Menu** | Nav → Menu; Bruschetta; optional one main | “Menu categories and prices come from the freeze — we don’t invent prices. Bruschetta, eight-fifty — honestly, no matching photo. Grilled Salmon — price as printed on the page.” |
| **2:15–2:50** | 35s | **Reservations** | Nav → Reservations; show fields; **no submit** unless optional | “Booking form: date, time slot, guests, name, email, optional phone. Only valid future slots for our hours — Sunday ends earlier. Happy path assigns a table from one through thirty. If the slot is full, we say no — we don’t invent a thirty-first table. If the database can’t take the write, we fail closed instead of faking success.” |
| **2:50–3:00** | 10s | **Handoff** | Stay on Reservations (or honesty breath) | See §5 |

**Room clock tip:** if you are already at **2:40** on Menu, skip extras and go straight to Reservations + handoff.

---

## 3. Supporting notes — click checklist + FR/NFR map

*For rehearsal sheets, Coverage, slides, and graders — not for Meghna’s spoken lines.*

### Honesty (say once early in plain English; map lives here)

| Say in plain English | Map |
| --- | --- |
| We are not claiming page-load or form-submit speed budgets are met | NFR-1 / NFR-2 — **not claimed met** |
| Browser check is partial — not Chrome + Firefox + Safari + Edge | NFR-7 — **partial** |
| This host is weekend staging, not production forever | Lightsail #57 |
| Operator page is a read-only recording helper, not an admin console | **not FR-19** |

Grade floor = official SRS only: **FR-1..FR-18**, **NFR-1..NFR-9**.

---

### Home (`/`) — ~0:20–0:55

| Do | Spoken (plain) | Map |
| --- | --- | --- |
| Land on Home; short scroll | Name, contact, hours | **FR-1** name · **FR-2** contact + hours |
| Show top nav | Menu, Reservations, About, Gallery | **FR-4** nav · **FR-3** images/theme (light) |
| — | Theme / layout look intentional; no speed claims | **NFR-3**, **NFR-4**, **NFR-8** (light); not NFR-1/2 |

---

### Gallery (`/gallery`) — ~0:55–1:30

| Do | Spoken (plain) | Map |
| --- | --- | --- |
| Image grid | Official photos | **FR-12** |
| One lightbox open/close | Closer look | **FR-13** |
| Awards + review quote | Freeze text | **FR-14** |

---

### Menu (`/menu`) — ~1:30–2:15

| Do | Spoken (plain) | Map |
| --- | --- | --- |
| Categories + prices from page | Freeze menu | **FR-5** |
| Bruschetta $8.50 | “no matching photo” | honesty (presentation aid) |
| Optional Grilled Salmon | Price as printed | freeze talk pick |

Other freeze talk picks (prices from page only): Caesar Salad $9.00 · Ribeye Steak $28.00 · Tiramisu $7.50 · Espresso $3.00.

---

### Reservations (`/reservations`) — ~2:15–2:50

| Do | Spoken (plain) | Map |
| --- | --- | --- |
| Show form fields | date, slot, guests, name, email, phone | **FR-6** |
| Slot list | valid future slots; Sunday shorter | **FR-7** |
| Point at Reserve (default: **no submit**) | table 1–30 on success; full slot = honest no | **FR-8**, **FR-9**, **NFR-5** |
| One line on backend | Postgres write or fail closed | **FR-17**, **FR-18**, **NFR-6** |

**Default for the 3-min cut:** show the form; do not submit unless you have buffer for an optional extra (§4).  
**Do not** open `/operator` in the core path unless you just completed a happy book (optional).

---

## 4. Optional must-film extras (only if time)

Mark these **OPTIONAL**. Core pack stops at Reservations look + handoff. Full click paths: [Must-film shots](MUST-FILM-SHOTS.md) · live https://knowledge.cafe.artof.link/must-film-shots.html

| Extra | When | What (plain) | Map | Time |
| --- | --- | --- | --- | ---: |
| **Happy book → operator** | ≥45s left | Unique email → Reserve → green table N → open `/operator` → new row. Say: “read-only helper, not an admin console.” | FR-6..9, FR-17..18 | ~70–90s |
| **Newsletter** | ≥40s left | Footer subscribe → `/operator` newsletter-only | FR-15, FR-16 | ~45–60s |
| **Full-book** | Pre-staged 30 tables off-mic | 31st attempt → “fully booked” / Network **409** | FR-9, NFR-5 | ~40–60s |

If staging is slow or a write fails: **do not invent success**. Fall back to Coverage or the happy-book clip as a **look only**.

---

## 5. Spoken handoff line (Architecture)

Say this (or close) at **~2:50**:

> “That’s the live path — Home, Gallery, Menu, Reservations — on staging. I’m handing off to Architecture: how React, Flask, and Postgres fit together, the diagrams, and how Coverage maps the boxes. Over to you.”

Then stop talking. Let Architecture take the screen.

---

## 6. Links (keep this tab list open)

| What | URL | Note |
| --- | --- | --- |
| **Live café (your surface)** | https://cafe.artof.link/ | Prefer this share. Staging — not forever. |
| **Operator (helper)** | https://cafe.artof.link/operator | Read-only. Not an admin console. Not in primary nav. |
| **Knowledge — Coverage** | https://knowledge.cafe.artof.link/coverage.html | Full FR/NFR + evidence (supporting doc). |
| **Knowledge — Must-film shots** | https://knowledge.cafe.artof.link/must-film-shots.html | Happy book / newsletter / 409. |
| **Knowledge — Quantic hub** | https://knowledge.cafe.artof.link/quantic.html | Navigation hub. |
| **Presentation (Architecture)** | https://knowledge.cafe.artof.link/presentation.html | After your handoff. |
| **Health (mute pre-flight)** | https://cafe.artof.link/api/health | Expect `{"ok":true}` before you go live. |

Backup host (if needed): `https://54-165-102-60.sslip.io/` — same honesty (staging, not forever).

---

## 7. Bruschetta reminder

If **Menu** is on camera and you point at **Bruschetta**:

- Price from the page: **$8.50** (do not invent).
- Say out loud: **“no matching photo.”**
- Do not apologize into a fake stock image story — honesty is the grade story.

---

## 8. Do-not-say checklist (spoken)

- Requirement code names on camera (save those for Coverage / supporting notes)
- “Operator is an admin console” / inventing an admin requirement
- “This host is production forever”
- “We met the three-second page budget” / “two-second form budget”
- “We passed Chrome, Firefox, Safari, and Edge”
- Invented prices or a guessed table on a full slot

---

## Pre-flight (30s, mute)

1. `GET https://cafe.artof.link/api/health` → `{"ok":true}`  
2. Click through Home → Gallery → Menu → Reservations once (cold cache).  
3. Confirm Architecture person is ready at your handoff.  
4. Optional: warm `/operator` only if you plan a happy-book extra.

---

*End of Meghna 3-min Café demo pack. Spoken = plain English. Mapping = supporting notes. Path locked 2026-09-05.*
