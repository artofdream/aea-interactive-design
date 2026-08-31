import React, { useState } from "react";
import { apiFetch } from "../api.js";

export default function NewsletterForm() {
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState(null);
  const [pending, setPending] = useState(false);

  async function onSubmit(event) {
    event.preventDefault();
    setPending(true);
    setStatus(null);
    try {
      const data = await apiFetch("/api/newsletter", {
        method: "POST",
        body: JSON.stringify({ email }),
      });
      setStatus({ ok: true, message: data.message });
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
