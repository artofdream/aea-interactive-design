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

Owner or `app/cursor` merges after MRC **COMMENT** (see review identity below). The author still does not merge.

## Review identity (GitHub self-APPROVE)

Same GitHub login **cannot** `APPROVE` its own PR. That is GitHub's self-APPROVE rule, not a repo setting we can relax. Changing branch protection does not lift it.

Another chat agent (Cursor / Claude / Gemini / OpenAI) still posts as `artofdream` if that is the connected `gh` identity. Same login is **not** a distinct reviewer. A COMMENT from that login is still self-review.

Until a distinct GitHub identity exists, MRC **COMMENT** is the role approve. Owner or `app/cursor` merges after that COMMENT. Author does not merge own PR.

Chosen distinct identity: a **GitHub App** (preferred over a second personal/machine user). A GitHub App does **not** use a PAT. It uses an app private key + installation on `artofdream/aea-interactive-design`. Never paste the private key or a PAT into chat.

When the App (or a machine user) is installed and reviews as a different login, that identity may `APPROVE`. Until then, do not treat same-login COMMENT as GitHub `APPROVE`, and do not try to self-APPROVE.

## Probe CI this session

Status words (`green`, `passing`, `ready to merge`) are claims. Probe GitHub Actions **this session** (`gh pr checks` / Actions logs) or write **Unknown**.

Fail closed:

- Missing required checks → do not merge
- Failing checks → do not merge
- Checks not probed this session → Unknown; do not merge
- Unreviewed PR (no MRC COMMENT from the review role, and no distinct-identity APPROVE) → do not merge

Fail-closed CI stays required even after MRC COMMENT. Do not merge unreviewed or failing checks.

## Cursor Bugbot

Enabled on this repo: every push, Smart, draft PRs on, summaries/risk on, autofix = **create new branch**.

- Bugbot comments are a **review signal**. Resolve them or **explicitly decline** with a reason. Do not ignore.
- Autofix opens a **new branch/PR**. That is not a silent merge. Do not squash it into an unrelated finding PR. One autofix finding → its own issue/branch/PR if it needs a change.

## Freeze

Official SRS is SoT (`docs/srs.md`, FR-1..FR-18 / NFR-1..NFR-9). Do not invent IDs. Do not implement the restaurant app from a PR-procedure task.
