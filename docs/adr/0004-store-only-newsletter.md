# ADR-0004: Store-only newsletter; optional SES mail only after the store, failing soft

## Status

Accepted (retroactive, recorded 2026-10-07)

## Date

2026-08-31: the store-only signup landed (PR #9). 2026-09-06: the optional SES step was added after the store (PR #138).

## Context

FR-15 asks for an email signup form that validates email format. FR-16 asks that submitted emails be stored in a backend database for future marketing. The SRS has no outbound-mail requirement. Later the sponsor asked for optional outbound mail through Amazon SES (Future #135). That is explicitly not a new FR, and the grade floor stays store-only.

## Decision

- `POST /api/newsletter` validates the email (`backend/cafe_fausse/validate.py`; the form also uses `type=email`). In one transaction it then upserts `customers` with `newsletter_signup = TRUE`, the "Newsletter Signup" column of the SRS Customers table. It returns **201** only after the commit.
- A missing database, unreachable database or timeout returns **503** and nothing is saved, the same fail-closed rule as [ADR-0003](0003-slot-capacity-model.md).
- **Store first, send second.** `send_newsletter_confirmation()` (`backend/cafe_fausse/ses_mail.py`) runs only after the store has committed. It counts as configured only when `SES_FROM_EMAIL` and `SES_REGION` (or `AWS_DEFAULT_REGION`) are set. Credentials come from the boto3 chain, never from git.
- **Fail soft.** When mail is not configured, the response carries `email_delivery: {attempted: false, status: "skipped", reason: "email not configured"}`. When the send raises, the error is logged and `status` is `"failed"`. The signup stays 201 in every case, so mail can never undo the store. The SES client uses a 2 s connect timeout, a 3 s read timeout and one attempt.
- The form shows the store-success message. It adds the "confirmation email was sent (demo)" sentence only when `email_delivery.status == "sent"`.
- A minimal unsubscribe (`/api/newsletter/unsubscribe`, `/unsubscribe`) turns the flag off.
- **Staging has no SES configuration.** The 2026-09-12 public-host probe returned 201 with `email_delivery` skipped / "email not configured". This repo does not claim that any email is sent.

## Consequences

- The FR-15 / FR-16 grade floor does not depend on AWS mail.
- `email_delivery` makes the mail outcome explicit, so a "sent" claim can't slip in silently.
- Unsubscribe takes a plain email address with no token, so anyone who knows an address can unsubscribe it. The RFC 8058 one-click `List-Unsubscribe` header is deferred.
- Newsletter-only signups share the `customers` table and get the placeholder name "Newsletter subscriber".
- Covered by `test_newsletter_stores_email`, `test_newsletter_without_ses_stays_store_only`, `test_newsletter_with_mocked_ses_still_stores`, `test_newsletter_ses_failure_does_not_fail_signup`, `backend/tests/test_ses_mail.py` and `test_newsletter_without_database_is_honest_no`.

## Related requirements

Related requirements: FR-15, FR-16, NFR-6

## Evidence

- `5603d85` feat: implement Café Fausse restaurant MVP (#7) (PR #9): validated, stored newsletter signup with no mailer.
- `6bae4f7` Future #135: optional SES confirmation after newsletter store (PR #138): store first, send second, fail soft, `email_delivery`.
- `eaddd95` Knowledge: record 2026-09-12 newsletter store-only probe (#198) (PR #201): staging shows `skipped` / "email not configured".

## OPEN

- OPEN: Whether a verified SES sender identity, a sandbox exit or an instance IAM role was ever set up is unknown. No send or inbox probe is on record, so delivery stays Unknown.
- OPEN: No decision has been made on token-based unsubscribe. The RFC 8058 header is listed only as a later follow-up.
