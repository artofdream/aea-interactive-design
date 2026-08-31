---
name: coherence-guardian
description: Guard ID freeze, honesty probes, DATE_RE handoff, and GitHub PR loop. Use when status words, requirement IDs, memory, or merge discipline are in play.
---

# Coherence guardian

- **IDs:** cite FR-1..FR-18 and NFR-1..NFR-9 from `docs/srs.md` only. Do not invent IDs. Official PDF is SoT.
- **Status word = claim.** Probe **this session** (command, HTTP GET, CI log, committed file) or write **Unknown**. A previous session is not a probe.
- **DATE_RE live handoff:** `research/daily-briefs/YYYY-MM-DD.md` only (`^[0-9]{4}-[0-9]{2}-[0-9]{2}$`, Europe/Berlin).
- **Uncommitted files are not shared memory.** Handoff is committed git + today’s brief.
- **Loop:** one finding → one GitHub issue → one branch → one PR. **Author does not merge their own PR.** GitHub only.
- Fail closed: missing freeze/PDF/DB, full book, timeout → honest no.
