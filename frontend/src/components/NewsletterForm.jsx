import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { apiFetch } from "../api.js";

/** Auto-dismiss polish; route change is the primary clear. */
export const NEWSLETTER_STATUS_DISMISS_MS = 5000;

export default function NewsletterForm() {
  const location = useLocation();
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState(null);
  const [pending, setPending] = useState(false);

  useEffect(() => {
    setStatus(null);
  }, [location.pathname]);

  useEffect(() => {
    if (!status) {
      return undefined;
    }
    const timer = window.setTimeout(() => {
      setStatus(null);
    }, NEWSLETTER_STATUS_DISMISS_MS);
    return () => window.clearTimeout(timer);
  }, [status]);

  async function onSubmit(event) {
    event.preventDefault();
    setPending(true);
    setStatus(null);
    try {
      const data = await apiFetch("/api/newsletter", {
        method: "POST",
        body: JSON.stringify({ email }),
      });
      const sent = data.email_delivery && data.email_delivery.status === "sent";
      setStatus({
        ok: true,
        message: sent
          ? `${data.message} A confirmation email was sent (demo, not a broadcast).`
          : data.message,
      });
      setEmail("");
    } catch (err) {
      setStatus({ ok: false, message: err.message || "Signup failed. Nothing was saved." });
    } finally {
      setPending(false);
    }
  }

  return (
    <form className="newsletter-form" onSubmit={onSubmit}>
      <label htmlFor="newsletter-email">Email address</label>
      <input
        id="newsletter-email"
        name="email"
        type="email"
        required
        autoComplete="email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
      />
      <button type="submit" disabled={pending}>
        {pending ? "Saving…" : "Subscribe"}
      </button>
      {status ? (
        <p className={`banner ${status.ok ? "is-ok" : "is-error"}`} role="status">
          {status.message}
        </p>
      ) : null}
    </form>
  );
}
