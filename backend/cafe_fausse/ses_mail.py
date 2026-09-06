"""Optional Amazon SES v2 send after newsletter store (Future #135, not a new FR).

Fail soft: missing config or send errors never undo a successful store.
This is a transactional confirmation / demo send, not a live broadcast list.
"""

from __future__ import annotations

import logging
import os
from typing import Any
from urllib.parse import quote

logger = logging.getLogger(__name__)

SKIPPED_NOT_CONFIGURED: dict[str, Any] = {
    "attempted": False,
    "status": "skipped",
    "reason": "email not configured",
}

_SEND_FAILED: dict[str, Any] = {
    "attempted": True,
    "status": "failed",
    "reason": "SES send failed; signup was stored.",
}


def ses_region() -> str:
    return (os.environ.get("SES_REGION") or os.environ.get("AWS_DEFAULT_REGION") or "").strip()


def ses_from_email() -> str:
    return (os.environ.get("SES_FROM_EMAIL") or "").strip()


def public_base_url() -> str:
    return (os.environ.get("PUBLIC_BASE_URL") or "https://cafe.artof.link").rstrip("/")


def is_configured() -> bool:
    """True only when From + region are set. Credentials come from the boto3 chain."""
    return bool(ses_region() and ses_from_email())


def unsubscribe_url(email: str) -> str:
    return f"{public_base_url()}/unsubscribe?email={quote(email, safe='')}"


def confirmation_text(email: str, *, unsub_url: str) -> str:
    return (
        "Café Fausse — newsletter confirmation (demo)\n\n"
        "Your email was stored for the Café Fausse newsletter.\n"
        "This is a one-time confirmation so outbound mail can be demonstrated. "
        "It is not a live broadcast list.\n\n"
        f"To stop future demo mail to {email}, open:\n{unsub_url}\n\n"
        "A full one-click List-Unsubscribe header (RFC 8058) is a later Future follow-up.\n\n"
        "Café Fausse\n"
        "1234 Culinary Ave, Suite 100, Washington, DC 20002\n"
        "(202) 555-4567\n"
    )


def confirmation_html(email: str, *, unsub_url: str) -> str:
    # Keep markup static except for escaped values supplied by the caller.
    from html import escape

    safe_email = escape(email, quote=True)
    safe_url = escape(unsub_url, quote=True)
    return (
        "<p>Your email was stored for the Café Fausse newsletter.</p>"
        "<p>This is a one-time <strong>confirmation</strong> (demo send), "
        "not a live broadcast list.</p>"
        f"<p>To stop future demo mail to {safe_email}, "
        f'<a href="{safe_url}">unsubscribe</a>.</p>'
        "<p>A full one-click List-Unsubscribe header (RFC 8058) is a later "
        "Future follow-up.</p>"
        "<p>Café Fausse<br>1234 Culinary Ave, Suite 100, Washington, DC 20002<br>"
        "(202) 555-4567</p>"
    )


def _ses_client():
    import boto3
    from botocore.config import Config

    return boto3.client(
        "sesv2",
        region_name=ses_region(),
        config=Config(
            connect_timeout=2,
            read_timeout=3,
            retries={"max_attempts": 1, "mode": "standard"},
        ),
    )


def send_newsletter_confirmation(to_email: str) -> dict[str, Any]:
    """Send a demo confirmation. Never raises to the signup caller."""
    if not is_configured():
        return dict(SKIPPED_NOT_CONFIGURED)

    unsub = unsubscribe_url(to_email)
    from_addr = ses_from_email()
    configuration_set = (os.environ.get("SES_CONFIGURATION_SET") or "").strip()
    try:
        client = _ses_client()
        kwargs: dict[str, Any] = {
            "FromEmailAddress": from_addr,
            "Destination": {"ToAddresses": [to_email]},
            "Content": {
                "Simple": {
                    "Subject": {
                        "Data": "Café Fausse newsletter confirmation (demo)",
                        "Charset": "UTF-8",
                    },
                    "Body": {
                        "Text": {
                            "Data": confirmation_text(to_email, unsub_url=unsub),
                            "Charset": "UTF-8",
                        },
                        "Html": {
                            "Data": confirmation_html(to_email, unsub_url=unsub),
                            "Charset": "UTF-8",
                        },
                    },
                }
            },
        }
        if configuration_set:
            kwargs["ConfigurationSetName"] = configuration_set
        client.send_email(**kwargs)
    except Exception:
        logger.exception("Future #135 SES send failed; newsletter store is unchanged.")
        return dict(_SEND_FAILED)

    logger.info("Future #135 SES confirmation attempted for a stored signup.")
    return {"attempted": True, "status": "sent", "provider": "ses-v2"}
