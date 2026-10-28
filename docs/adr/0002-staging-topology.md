# ADR-0002: Staging topology: one Lightsail instance (Caddy → Flask → on-host PostgreSQL) for cafe.artof.link

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-09-05: the topology was first recorded in the repo (PR #70). The keep-until-scoring window was recorded on 2026-09-09 (PR #190).

## Context

Issue #57 asked for a stable public restaurant host for Saturday prep and the Sunday recording. The owner accepted the AWS cost. Permanent hosting stays Future #22. The SRS (§4) only requires that the app be deployable locally or on a web server. `AGENTS.md` keeps AWS out of the restaurant MVP *code*, so the staging infrastructure is recorded in documentation commits, not in committed infrastructure code.

## Decision

As recorded in `knowledge/stack.md`, `knowledge/honesty.md`, `README.md` and `knowledge/developer-system-map.md`:

- One AWS Lightsail instance in us-east-1 is the staging host. A Route53 A record for `cafe.artof.link` (TTL 60) points at it. That record overrides the `*.artof.link` wildcard, which is not Café Fausse.
- Request path: browser → **Caddy** (Let's Encrypt TLS, reverse proxy, HTTP to HTTPS redirect) → **Flask**, serving the built React SPA and `/api/*` on the same origin → **PostgreSQL on the same instance** ("on-box Postgres", not a shared RDS).
- The staging host stays up **until Quantic scoring is done**, unless the owner overrides tear-down (owner lock 2026-09-09). The Knowledge site is a separate GitHub Pages host, with no shared load balancer.
- No SES mail settings are configured on staging, so the newsletter is store-only there ([ADR-0004](0004-store-only-newsletter.md)).

## Consequences

- Staging runs the same React → Flask → PostgreSQL design as local development ([ADR-0001](0001-stack-react-flask-postgresql.md)), so it proves the SRS stack over public HTTPS.
- A single instance is a single point of failure, and the database shares that host with no managed backups. That is acceptable for temporary staging. It is not a production claim, and the docs repeat "not production forever".
- The host cannot be rebuilt from the repo. No compose file, Caddyfile, Dockerfile or deploy script is committed, so a rebuild depends on knowledge outside the repo.
- There is an ongoing cost (about $12/month per `knowledge/stack.md`) until tear-down.
- Any status word about the host needs a probe in the same session (`AGENTS.md` honesty rules).

## Related requirements

Related requirements: none

Deployment (SRS §4) and HTTP/HTTPS (SRS §3.3.3) are un-numbered SRS sections, so no FR or NFR ID applies. NFR-1 and NFR-2 were *measured* on this host, but the topology was not designed against those budgets.

## Evidence

- `17961f5` docs(knowledge): AWS staging HLD + 2nd-brain honesty (#67) (PR #70): Lightsail, Route53 A, Caddy + Let's Encrypt, PostgreSQL on the instance.
- `2f9b536` docs(honesty): align README and guides with Lightsail staging (#77) (PR #78).
- `eed2b91` docs(honesty): staging stays up until owner tear-down (#77) (PR #78).
- `8bacf1e` Knowledge: developer system map (stack, API, schema, FE/BE) (PR #161): `Caddy:2` edge, same-origin via Caddy, PostgreSQL on the host.
- `1f6ffa1` Add root ai-tooling.md and staging.md for Quantic submit (PR #186): `staging.md` names `https://cafe.artof.link/` as temporary MSAIE staging.
- `4d41900` Knowledge: keep cafe staging until Quantic scoring (PR #190).
- Issue #57 (open) is the staging tracker. Issue #22 is permanent hosting (Future).

## OPEN

- OPEN: Whether the staging services run as a **Docker compose** stack is unknown. No compose file, Caddyfile, Dockerfile or deploy script is committed. The docs say `Caddy:2` and "on-box Postgres" but never say compose. This needs the owner or the staging host's own config.
- OPEN: Whether Flask runs under gunicorn on staging is unknown. `gunicorn` is in `backend/requirements.txt` and in the developer map, but no committed process config shows it.
- OPEN: Why Lightsail was chosen over EC2, ECS or another host is not recorded. Issue #57 records the need and the cost acceptance, not the choice.
- OPEN: No tear-down date after Quantic scoring is set. Whether graders need the host up is still Unknown (`knowledge/honesty.md`).
- OPEN: Backup and restore for the on-host database are not recorded.
