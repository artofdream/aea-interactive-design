---
title: Agent skills matrix
nav: Quantic
---

# Agent skills matrix

This page is a **documentation matrix** of Grok Bot skill ids used on Café Fausse. Recipes live in Grok Bot. GitHub Pages does **not** host the recipe bodies. Official SRS (**FR-1..FR-18**, **NFR-1..NFR-9**) wins on conflict. Do not invent **FR-19** or **NFR-10**.

Delivery-only ([#205](https://github.com/artofdream/aea-interactive-design/issues/205)): linked from [Quantic / MSAIE](quantic.md) and [Honesty](honesty.md). Not in the global top nav.

Sibling issues [#206](https://github.com/artofdream/aea-interactive-design/issues/206)–[#212](https://github.com/artofdream/aea-interactive-design/issues/212) stay open; this page is the matrix only.

## Shared Grok skills (adopt / link)

Adopt by id. Do not duplicate recipe bodies in-repo.

| Skill | Scope | Why? | What |
|---|---|---|---|
| PR train rebase (`pr-train-rebase`) | Parallel cloud PRs **CONFLICTING** | [#201](https://github.com/artofdream/aea-interactive-design/issues/201) after Stack [#199](https://github.com/artofdream/aea-interactive-design/issues/199) / [#202](https://github.com/artofdream/aea-interactive-design/issues/202) | Order merge + rebase survivors; no invented scope in conflicts |
| Honesty ledger gate (`honesty-ledger-gate`) | FR/NFR status promotions | Store-only SES / no **FR-19** | Evidence-backed status; never invent deferred rules |
| Companion plain docs (`companion-plain-docs`) | Knowledge companion layer | Quantic plain English + diagrams | Cite **FR/NFR**; official SRS wins on conflict |
| Persona journey validation (`persona-journey-validation`) | Live UX audit | Must-film + ROG/mobile | Personas → journeys → issues → fix |

## Café App Grok skills (created 2026-09-12)

Document only. Recipes live in Grok Bot.

| Skill | Scope | Why? | What |
|---|---|---|---|
| Freeze-first generation (`freeze-first-generation`) | App MVP from SRS + `freeze.json` | Freeze-first build | No invented IDs; no student-app copy |
| Fail-closed missing DB (`fail-closed-missing-db`) | Postgres-required writes | Fail-closed tests | Honest errors; no fake success |
| Probe before status words (`probe-before-status-words`) | Live / Probed / PASS / sent claims | SES skipped probe; NFR timings | This-session probe or **Unknown** |
| Optional mail after store (`optional-mail-after-store`) | Future SES after **FR-15** / **FR-16** | [#135](https://github.com/artofdream/aea-interactive-design/issues/135) / [#138](https://github.com/artofdream/aea-interactive-design/issues/138) | Store first; fail soft; not a new FR |
| Official image allowlist (`official-image-allowlist`) | Gallery / menu images | Official 4 webps vs supplemental | Basename allowlist only |
| Staging keep/tear honesty (`staging-keep-tear-honesty`) | `cafe.artof.link` temporary staging | Keep-until-scoring / [#190](https://github.com/artofdream/aea-interactive-design/issues/190) | Lock keep/tear the day decided; no auto-tear |
