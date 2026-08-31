# Honesty / probe

Failure class: treating a hostname, memory, or closed task as evidence that something is live.

Rule: status words need a probe **this session** (command, HTTP GET, CI log, committed file). If the probe did not happen this session, the status is **Unknown**.

This repo: `knowledge.cafe.artof.link` and `cafe.artof.link` stay Unknown until a GET this session after owner enablement. Closing the foundation PR is not that probe. Uncommitted files are not a probe.
