---
name: pr-coordinator
description: GitHub PR procedure memory (not a hat). Use when opening, reviewing, checking CI, handling Bugbot, or deciding merge. GitHub only — never GitLab/glab.
---

# PR coordinator

This is **procedure memory** for GitHub issues/PRs/Actions (`gh`). It is not a fifth hat and not a florist GitLab MRC.

## Loop

One finding → one GitHub issue → one branch → one PR against `main`. Do not batch unrelated findings. Do not use GitLab, `glab`, GitLab MRs, or GitLab CI.

## Author does not merge

The authoring agent does **not** merge its own PR. Red CI is not mergeable. Same-login review is not a distinct second identity.

`cursor[bot]` is the distinct second identity for **`artofdream`-authored** PRs. The author still does not merge.

## Review identity (GitHub self-APPROVE)

Same GitHub login **cannot** `APPROVE` its own PR. That is GitHub's self-APPROVE rule, not a repo setting we can relax.

Owner PAT / GitHub MCP / `gh` as `artofdream` is **not** a distinct reviewer. A COMMENT from that login is still self-review. Do not self-APPROVE.

**Chosen distinct identity: `cursor[bot]`** (Cursor GitHub App, already installed). Probe: it merged PR #16 and PR #27. Do **not** install a second GitHub App, mint an app private key, or use a second personal account for this.

### Probed #27: merge works; REST APPROVE is 403

On #27, `cursor[bot]` **merged** with no GitHub review `APPROVE` (only author `COMMENTED`). REST `POST .../pulls/27/reviews` `event=APPROVE` as the Cursor App returned **403** (`Resource not accessible by integration` / `addPullRequestReview`).

For `artofdream`-authored PRs, the probed second-identity action is **`cursor[bot]` merge after this-run green checks + Bugbot terminal**.

Do **not** block a sweep or merge on an `APPROVE` the App cannot submit (403). Missing `APPROVE` is **not** a reason to treat a `cursor[bot]` merge as invalid.

Owner PAT / `artofdream` still must **not** `APPROVE` or merge those PRs.

MRC **COMMENT** remains the role-approve signal in the room until the Cursor App can `APPROVE` (issue #13 / PR #14). Owner may later grant the existing Cursor App **pull-request-reviews** write. Do **not** install a custom GitHub App or mint a private key for this.

Bugbot posts as `cursor[bot]` too; those inline comments and `COMMENTED` reviews are a **signal**, not the second-identity merge action.

- Author `artofdream` → `cursor[bot]` may merge after this-run green checks and Bugbot resolve-or-decline. Owner PAT / `artofdream` cannot `APPROVE` or merge that PR. Do not wait for an App `APPROVE` that returns 403.
- Author `cursor[bot]` → owner `artofdream` may `APPROVE` and merge (different login). `cursor[bot]` must **not** `APPROVE` or merge a PR it authored.

Sweep: `.cursor/rules/pr-coordinator-cloud.mdc`.

## Probe CI this session

Status words (`green`, `passing`, `ready to merge`) are claims. Probe GitHub Actions **this session** (`gh pr checks` / Actions logs) or write **Unknown**.

Fail closed:

- Missing required checks → do not merge
- Failing checks → do not merge
- Checks not probed this session → Unknown; do not merge
- Author merging own PR → do not merge
- Owner PAT / `artofdream` `APPROVE` or merge of an `artofdream`-authored PR → do not (self-review / author-merge)
- Missing `APPROVE` on an `artofdream`-authored PR when the App returns 403 → **not** a fail-closed block; `cursor[bot]` merge after green + Bugbot terminal is valid

Fail-closed CI stays required. Do not merge failing or unprobed checks. Do not self-APPROVE.

## Cursor Bugbot

Enabled on this repo: every push, Smart, draft PRs on, summaries/risk on, autofix = **create new branch**.

- Bugbot comments are a **review signal**. Resolve them or **explicitly decline** with a reason. Do not ignore.
- Autofix opens a **new branch/PR**. That is not a silent merge. Do not squash it into an unrelated finding PR. One autofix finding → its own issue/branch/PR if it needs a change.

## Freeze

Official SRS is SoT (`docs/srs.md`, FR-1..FR-18 / NFR-1..NFR-9). Do not invent IDs. Do not implement the restaurant app from a PR-procedure task.
