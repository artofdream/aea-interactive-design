# Schema / outer harness layers (Future)

**Future / not-MVP.** The assignment floor is the SRS freeze, not this diagram.

The outer harness wraps shared understanding and (later) domain services. Six layers, scaled to this repo — not a florist copy:

1. **Guides** — `AGENTS.md`, `.cursor/rules`, four hats (knowledge-guardian, coherence-guardian, product-owner, engineer) plus `pr-coordinator` procedure memory (not a hat), SRS ID freeze. Not a 14-hat library.
2. **Sensors** — GitHub Actions (fail closed if `docs/srs.md` or the official PDF is missing; knowledge site must build). Later: availability checks, HTTP GET probes **this session**.
3. **Loop** — interpret, act, verify, remember. One finding → one GitHub issue → one branch → one PR. Author does not merge their own PR. Closing a PR is not a probe.
4. **Memory** — live handoff `research/daily-briefs/YYYY-MM-DD.md`; freeze in `docs/srs.md`; this knowledge site. Uncommitted files are not shared memory.
5. **Permissions** — Café Fausse Knowledge vs Café Fausse App; owner enables Pages/DNS and adds `quantic-grader`. When Flask exists, domain services stay authoritative for bookings.
6. **Observability** — every status word needs evidence **this session**. Missing evidence → **Unknown**.

Ratchet: a failure adds a tighter guide or sensor. Do not claim the system is antifragile.
