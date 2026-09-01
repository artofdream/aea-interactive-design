---
name: pr-coordinator
description: GitHub PR procedure memory (not a hat). Use when opening, reviewing, checking CI, handling Bugbot, or deciding merge. GitHub only — never GitLab/glab.
---

# PR coordinator

This is **procedure memory** for GitHub issues/PRs/Actions (`gh`). It is not a fifth hat and not a florist GitLab MRC.

## Loop

One finding → one GitHub issue → one branch → one PR against `main`. Do not batch unrelated findings. Do not use GitLab, `glab`, GitLab MRs, or GitLab CI.

## Author does not merge

The authoring agent does **not** merge its own PR. Unreviewed PRs are not mergeable. Red CI is not mergeable.

`cursor[bot]` is the distinct reviewer for **`artofdream`-authored** PRs: it may submit GitHub review `APPROVE` and merge after a this-run CI probe. The author still does not merge.

## Review identity (GitHub self-APPROVE)

Same GitHub login **cannot** `APPROVE` its own PR. That is GitHub's self-APPROVE rule, not a repo setting we can relax.

Owner PAT / GitHub MCP / `gh` as `artofdream` is **not** a distinct reviewer. A COMMENT from that login is still self-review. Do not self-APPROVE.

**Chosen distinct identity: `cursor[bot]`** (Cursor GitHub App, already installed). Probe: it merged PR #16. Do **not** install a second GitHub App, mint an app private key, or use a second personal account for this.

Merge gate is a submitted GitHub review **`APPROVE` from a login that is not the PR author**. Bugbot posts as `cursor[bot]` too; those inline comments and `COMMENTED` reviews are a **signal**, not the gate.

- Author `artofdream` → `cursor[bot]` coordinator `APPROVE`, then `cursor[bot]` may merge. Owner PAT / `artofdream` cannot `APPROVE` or merge that PR.
- Author `cursor[bot]` → owner `artofdream` may `APPROVE` and merge (different login). `cursor[bot]` must **not** `APPROVE` or merge a PR it authored.

Sweep: `.cursor/rules/pr-coordinator-cloud.mdc`.

## Probe CI this session

Status words (`green`, `passing`, `ready to merge`) are claims. Probe GitHub Actions **this session** (`gh pr checks` / Actions logs) or write **Unknown**.

Fail closed:

- Missing required checks → do not merge
- Failing checks → do not merge
- Checks not probed this session → Unknown; do not merge
- Unreviewed PR (no non-author GitHub review `APPROVE`) → do not merge

Fail-closed CI stays required even after review. Do not merge unreviewed or failing checks.

## Cursor Bugbot

Enabled on this repo: every push, Smart, draft PRs on, summaries/risk on, autofix = **create new branch**.

- Bugbot comments are a **review signal**. Resolve them or **explicitly decline** with a reason. Do not ignore.
- Autofix opens a **new branch/PR**. That is not a silent merge. Do not squash it into an unrelated finding PR. One autofix finding → its own issue/branch/PR if it needs a change.

## Freeze

Official SRS is SoT (`docs/srs.md`, FR-1..FR-18 / NFR-1..NFR-9). Do not invent IDs. Do not implement the restaurant app from a PR-procedure task.
