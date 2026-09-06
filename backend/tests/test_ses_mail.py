"""Future #135 SES helper — no live AWS. Not a new FR."""

from __future__ import annotations

from cafe_fausse.ses_mail import (
    confirmation_text,
    is_configured,
    send_newsletter_confirmation,
    unsubscribe_url,
)


def test_not_configured_without_env(monkeypatch):
    monkeypatch.delenv("SES_FROM_EMAIL", raising=False)
    monkeypatch.delenv("SES_REGION", raising=False)
    monkeypatch.delenv("AWS_DEFAULT_REGION", raising=False)
    assert is_configured() is False
    result = send_newsletter_confirmation("guest@example.com")
    assert result["attempted"] is False
    assert result["status"] == "skipped"
    assert result["reason"] == "email not configured"


def test_send_uses_ses_v2_when_configured(monkeypatch):
    monkeypatch.setenv("SES_REGION", "us-east-1")
    monkeypatch.setenv("SES_FROM_EMAIL", "newsletter@cafe.artof.link")
    monkeypatch.setenv("PUBLIC_BASE_URL", "https://cafe.artof.link")

    class FakeClient:
        last = None

        def send_email(self, **kwargs):
            FakeClient.last = kwargs
            return {"MessageId": "fake-id"}

    monkeypatch.setattr("cafe_fausse.ses_mail._ses_client", lambda: FakeClient())
    result = send_newsletter_confirmation("guest@example.com")
    assert result == {"attempted": True, "status": "sent", "provider": "ses-v2"}
    sent = FakeClient.last
    assert sent["FromEmailAddress"] == "newsletter@cafe.artof.link"
    assert sent["Destination"]["ToAddresses"] == ["guest@example.com"]
    text = sent["Content"]["Simple"]["Body"]["Text"]["Data"]
    assert "not a live broadcast list" in text
    assert "unsubscribe" in text.lower()
    assert "email=guest%40example.com" in unsubscribe_url("guest@example.com")


def test_send_failure_is_soft(monkeypatch):
    monkeypatch.setenv("SES_REGION", "us-east-1")
    monkeypatch.setenv("SES_FROM_EMAIL", "newsletter@cafe.artof.link")

    class BoomClient:
        def send_email(self, **kwargs):
            raise RuntimeError("sandbox recipient not verified")

    monkeypatch.setattr("cafe_fausse.ses_mail._ses_client", lambda: BoomClient())
    result = send_newsletter_confirmation("stranger@example.com")
    assert result["attempted"] is True
    assert result["status"] == "failed"
    assert "stored" in result["reason"]


def test_confirmation_mentions_unsubscribe_follow_up():
    text = confirmation_text("a@b.co", unsub_url="https://cafe.artof.link/unsubscribe?email=a%40b.co")
    assert "RFC 8058" in text
    assert "unsubscribe" in text.lower()
