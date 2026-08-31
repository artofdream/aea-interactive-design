import React, { useEffect, useMemo, useState } from "react";
import freeze from "@shared/freeze.json";
import { apiFetch } from "../api.js";
import { formatSlot, todayISODate } from "../restaurantTime.js";

export default function Reservations() {
  const minDate = useMemo(() => todayISODate(new Date(), freeze.timezone), []);
  const [date, setDate] = useState(minDate);
  const [slots, setSlots] = useState([]);
  const [slotError, setSlotError] = useState("");
  const [timeSlot, setTimeSlot] = useState("");
  const [guests, setGuests] = useState("2");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [status, setStatus] = useState(null);
  const [pending, setPending] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setSlotError("");
    setTimeSlot("");
    setSlots([]);
    apiFetch(`/api/slots?date=${encodeURIComponent(date)}`)
      .then((data) => {
        if (cancelled) return;
        setSlots(data.slots || []);
        if (!(data.slots || []).length) {
          setSlotError("No remaining seating times on this date.");
        }
      })
      .catch((err) => {
        if (cancelled) return;
        setSlotError(err.message || "Could not load time slots.");
      });
    return () => {
      cancelled = true;
    };
  }, [date]);

  async function onSubmit(event) {
    event.preventDefault();
    setPending(true);
    setStatus(null);
    try {
      const data = await apiFetch("/api/reservations", {
        method: "POST",
        body: JSON.stringify({
          time_slot: timeSlot,
          guest_count: Number(guests),
          customer_name: name,
          email,
          phone: phone.trim() || undefined,
        }),
      });
      setStatus({ ok: true, message: data.message });
    } catch (err) {
      setStatus({
        ok: false,
        message: err.message || "Reservation was not saved.",
      });
    } finally {
      setPending(false);
    }
  }

  return (
    <article>
      <h1>Reservations</h1>
      <p>
        Thirty tables. If a seating is full, the site will say so — it will not assign a table.
        If the database is unavailable, the booking is not saved.
      </p>
      <form className="form" onSubmit={onSubmit}>
        <label>
          Date
          <input
            type="date"
            required
            min={minDate}
            value={date}
            onChange={(event) => setDate(event.target.value)}
          />
        </label>
        <label>
          Time slot
          <select
            required
            value={timeSlot}
            onChange={(event) => setTimeSlot(event.target.value)}
            disabled={!slots.length}
          >
            <option value="">{slots.length ? "Select a time" : "No times available"}</option>
            {slots.map((slot) => (
              <option key={slot} value={slot}>
                {formatSlot(slot, freeze.timezone)}
              </option>
            ))}
          </select>
        </label>
        {slotError ? <p className="banner is-error">{slotError}</p> : null}
        <label>
          Number of guests
          <input
            type="number"
            min="1"
            max="20"
            required
            value={guests}
            onChange={(event) => setGuests(event.target.value)}
          />
        </label>
        <label>
          Name
          <input
            type="text"
            required
            autoComplete="name"
            value={name}
            onChange={(event) => setName(event.target.value)}
          />
        </label>
        <label>
          Email address
          <input
            type="email"
            required
            autoComplete="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </label>
        <label>
          Phone number (optional)
          <input
            type="tel"
            autoComplete="tel"
            value={phone}
            onChange={(event) => setPhone(event.target.value)}
          />
        </label>
        <button type="submit" disabled={pending || !timeSlot}>
          {pending ? "Booking…" : "Reserve a table"}
        </button>
        {status ? (
          <p className={`banner ${status.ok ? "is-ok" : "is-error"}`} role="status">
            {status.message}
          </p>
        ) : null}
      </form>
    </article>
  );
}
