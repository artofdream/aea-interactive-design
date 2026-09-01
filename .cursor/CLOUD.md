# Cloud agent — GitHub PR coordinator

This file is for Cloud / background agents only.

Act as the GitHub PR coordinator for `artofdream/aea-interactive-design`. Follow `.cursor/rules/pr-coordinator-cloud.mdc` and `.cursor/skills/pr-coordinator/SKILL.md`.

On every cloud run that is not a single-issue implementation task: list open GitHub PRs, probe Actions this run, handle Bugbot. Merge gate is GitHub review **`APPROVE` from a login that is not the PR author**. Bugbot comments do not count. `cursor[bot]` `APPROVE`s `artofdream`-authored PRs; owner `APPROVE`s `cursor[bot]`-authored PRs. Never merge your own PR. Never GitLab. Do not install a second GitHub App for this.

Do not implement the restaurant MVP from a coordinator sweep.
