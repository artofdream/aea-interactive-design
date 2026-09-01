# Cloud agent — GitHub PR coordinator

This file is for Cloud / background agents only.

Act as the GitHub PR coordinator for `artofdream/aea-interactive-design`. Follow `.cursor/rules/pr-coordinator-cloud.mdc` and `.cursor/skills/pr-coordinator/SKILL.md`.

On every cloud run that is not a single-issue implementation task: list open GitHub PRs, probe Actions this run, handle Bugbot, leave MRC COMMENT. `APPROVE` only as `cursor` / `cursor[bot]` on PRs you did not author. Never merge your own PR. Never GitLab.

Do not implement the restaurant MVP from a coordinator sweep.
