# AWS `cafe_fausse_db` vs local MVP schema

**Future / not-MVP.** Parked so a later cut can reuse a teammate dump of AWS RDS objects. This page is **not** a live RDS probe. This VM did **not** connect to AWS this session.

Do **not** apply the AWS DDL onto local `backend/schema.sql`. The restaurant MVP stays the in-repo schema (FR-17 customers + reservations; FR-5 menu from freeze). Menu persistence is Future [#36](https://github.com/artofdream/aea-interactive-design/issues/36). Hosting / IAM tunnel is Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22).

## Source of this dump (honesty)

Reported 2026-09-04 by a teammate as already initialized on AWS:

- Database: `cafe_fausse_db`
- Session: `cafe_fausse_developer` / `cafe_fausse_developer`
- Auth: **RDS IAM**, temporary token (~15 minutes). `PGPASSWORD` is the token, not a stored password.
- Connect path they used: `LOCAL_PORT=15433 ./infrastructure/database/scripts/run-sql.sh` (that tree is **not** in this repo).
- Do **not** mint or share a permanent password for `cafe_fausse_developer`.

Status of that RDS instance from this Knowledge/App VM: **Unknown** (no `psql` / IAM token this session).

## Tables reported

### `customers`

| AWS column | AWS type | AWS null | Local MVP (`backend/schema.sql`) | Reuse |
|---|---|---|---|---|
| `customer_id` | `bigint` | NO | `SERIAL` / `INTEGER` PK | Same role. Import as-is if IDs must be preserved; else let local `SERIAL` assign. |
| `customer_name` | `varchar` | **YES** | `TEXT NOT NULL` | Reject or fill empty names. Local writes require a name (reservation path). |
| `email` | `varchar` | NO | `email_address TEXT NOT NULL UNIQUE` | **Rename on import.** Local Flask uses `email_address` (FR-17 / FR-18). |
| `phone_number` | `varchar` | YES | `TEXT` nullable | Same idea. |
| `newsletter_opt_in` | `boolean` | NO | `newsletter_signup BOOLEAN NOT NULL DEFAULT FALSE` | **Rename on import.** |
| `created_at` | `timestamptz` | NO | `timestamptz NOT NULL DEFAULT NOW()` | Same. |
| `updated_at` | `timestamptz` | NO | `timestamptz NOT NULL DEFAULT NOW()` | Same. |

Local also unique-indexes `email_address`. AWS dump did not list constraints; treat uniqueness as **Unknown** until probed.

### `reservations`

| AWS column | AWS type | AWS null | Local MVP | Reuse |
|---|---|---|---|---|
| `reservation_id` | `bigint` | NO | `SERIAL` PK | Same role. |
| `customer_id` | `bigint` | NO | `INTEGER NOT NULL` FK → `customers` | Same role. |
| `time_slot` | **`timestamp without time zone`** | NO | **`TIMESTAMPTZ NOT NULL`** | **Hazard.** Local slots are America/New_York (`shared/freeze.json`). Import naive AWS timestamps as that zone, then store UTC timestamptz. Do not assume UTC. |
| `guest_count` | `smallint` | NO | `INTEGER NOT NULL CHECK (1..20)` | Same role. Drop or reject rows outside 1–20. |
| `table_number` | `smallint` | **YES** | `INTEGER NOT NULL CHECK (1..30)` | **Hazard.** Local FR-9 path requires an assigned table 1–30. Null AWS rows are not a local booking. |

Local unique index `reservations_slot_table (time_slot, table_number)` and `reservations_time_slot`. AWS dump did not list indexes. Local `created_at` on reservations has no AWS twin in the dump.

### `menu_categories` / `menu_items` (not in local MVP)

| AWS table | Columns (as dumped) | Local MVP |
|---|---|---|
| `menu_categories` | `category_id` bigint NO; `category_name` varchar NO; `display_order` smallint NO | No table. FR-5 menu is `shared/freeze.json` / `GET /api/menu`. |
| `menu_items` | `menu_item_id` bigint NO; `category_id` bigint NO; `item_name` varchar NO; `description` text NO; `price` numeric NO; `display_order` smallint NO; `is_available` boolean NO | No table. Freeze prices/names are SoT. Do not “improve” them. |

Reuse of menu rows is Future [#36](https://github.com/artofdream/aea-interactive-design/issues/36) only. If a later import happens, freeze IDs/prices still win unless a deliberate change is recorded.

## What a local reuse script would do (not written in this PR)

1. Read AWS dump or a CSV/SQL export (not a live IAM session from CI).
2. Map `email` → `email_address`, `newsletter_opt_in` → `newsletter_signup`.
3. Interpret `reservations.time_slot` as America/New_York unless a later probe proves otherwise.
4. Skip reservations with null `table_number` or guests outside 1–20 or tables outside 1–30.
5. Leave `menu_*` unimported until #36.
6. Fail closed if PostgreSQL is missing (same as FR-6..FR-9 / FR-18 writes).

## AWS side (later, not this PR)

- IAM token + `run-sql.sh` + port `15433` stay on the AWS/infra tree, not this student MVP.
- Do not add a permanent DB password.
- Do not point `cafe.artof.link` at RDS from this cut. Hostname remains Future [#22](https://github.com/artofdream/aea-interactive-design/issues/22). Live restaurant URL: **Unknown**.
- Do not invent FR-19 / NFR-10.
