# DATE_RE

Failure class: scattering session state across chat, random notes, and “whatever file was last edited,” so the next agent cannot find today.

Rule: the only live handoff is `research/daily-briefs/YYYY-MM-DD.md` with date matching `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` (Europe/Berlin). Other notes may exist; they are not the handoff.
