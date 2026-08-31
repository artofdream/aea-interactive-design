# Honesty / probe

Failure class: treating a hostname, memory, or closed task as evidence that something is live.

Rule: status words need a probe (command, HTTP GET, CI log, file on disk). If the probe did not happen, the status is **Unknown**.

This repo: `knowledge.cafe.artof.link` and `cafe.artof.link` stay Unknown until a GET after owner enablement. Closing the foundation PR is not that probe.
