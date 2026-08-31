import { useState } from "react";
import { subscribeNewsletter } from "../lib/api.js";
import { isValidEmail } from "../lib/validate.js";

export default function NewsletterForm({ compact = false }) {
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState(null);
  const [busy, setBusy] = useState(false);

  async function onSubmit(event) {
    event.preventDefault();
    setStatus(null);
    if (!isValidEmail(email)) {
      setStatus({ kind: "error", text: "Please enter a valid email address." });
      return;
    }
    setBusy(true);
    try {
      const result = await subscribeNewsletter(email.trim());
      setStatus({ kind: "ok", text: result.message });
      setEmail("");
    } catch (err) {
      setStatus({
        kind: "error",
        text: err.message || "Newsletter signup could not be saved. Please try again.",
      });
    } finally {
      setBusy(false);
    }
  }

  return (
    <form className={compact ? "newsletter" : "form"} onSubmit={onSubmit} noValidate>
      <label htmlFor={compact ? "footer-email" : "newsletter-email"}>
        Email address
        <span className={compact ? "newsletter-row" : undefined}>
          <input
            id={compact ? "footer-email" : "newsletter-email"}
            type="email"
            name="email"
            autoComplete="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="you@example.com"
            required
          />
          {compact ? (
            <button className="btn" type="submit" disabled={busy}>
              {busy ? "Saving…" : "Subscribe"}
            </button>
          ) : null}
        </span>
      </label>
      {!compact ? (
        <button className="btn" type="submit" disabled={busy}>
          {busy ? "Saving…" : "Subscribe to the newsletter"}
        </button>
      ) : null}
      {status ? <p className={`banner ${status.kind}`}>{status.text}</p> : null}
    </form>
  );
}
