# Honesty / probe

Failure class: treating a hostname, memory, or closed task as evidence that something is live.

Rule: status words need a probe **this session** (command, HTTP GET, CI log, committed file). If the probe did not happen this session, the status is **Unknown**.

This repo: `knowledge.cafe.artof.link` and `cafe.artof.link` stay **Unknown** until a GET **this session**. A previous session, a hostname on a slide, or a closed PR is not that probe. Last standing probe in the live handoff (2026-09-05): both HTTPS GET 200 — Knowledge Pages, and Lightsail weekend staging on `cafe.artof.link` (#57, not forever production). Permanent hosting stays #22. Uncommitted files are not a probe.
