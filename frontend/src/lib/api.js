/** Thin fetch wrapper. Network or HTTP failures become user-facing messages (NFR-6). */

async function readJson(res) {
  const body = await res.json().catch(() => null);
  if (!body) {
    throw new Error("The server sent an unexpected response. Please try again.");
  }
  return body;
}

export async function getHealth() {
  try {
    const res = await fetch("/api/health");
    const body = await readJson(res);
    return { ok: res.ok && body.ok === true, body };
  } catch {
    return {
      ok: false,
      body: {
        ok: false,
        error: "unreachable",
        message:
          "We could not reach the reservation service. Please try again or call (202) 555-4567.",
      },
    };
  }
}

export async function getSlots(date) {
  const res = await fetch(`/api/slots?date=${encodeURIComponent(date)}`);
  const body = await readJson(res);
  if (!res.ok || body.ok === false) {
    throw new Error(body.message || "We could not load available times.");
  }
  return body.slots;
}

export async function createReservation(payload) {
  const res = await fetch("/api/reservations", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const body = await readJson(res);
  if (!res.ok || body.ok === false) {
    const err = new Error(body.message || "The reservation could not be completed.");
    err.code = body.error;
    throw err;
  }
  return body;
}

export async function subscribeNewsletter(email) {
  const res = await fetch("/api/newsletter", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email }),
  });
  const body = await readJson(res);
  if (!res.ok || body.ok === false) {
    const err = new Error(body.message || "Newsletter signup could not be saved.");
    err.code = body.error;
    throw err;
  }
  return body;
}
