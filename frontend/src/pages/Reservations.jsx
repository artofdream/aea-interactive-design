import { useEffect, useState } from "react";
import { restaurant } from "../data/restaurant.js";
import { createReservation, getHealth, getSlots } from "../lib/api.js";
import { isValidEmail, isValidGuests, isValidName } from "../lib/validate.js";

function defaultDate() {
  const d = new Date();
  d.setDate(d.getDate() + 1);
  return d.toISOString().slice(0, 10);
}

export default function Reservations() {
  const [date, setDate] = useState(defaultDate);
  const [slots, setSlots] = useState([]);
  const [timeslot, setTimeslot] = useState("");
  const [guests, setGuests] = useState("2");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [service, setService] = useState({ ok: true, message: "" });
  const [status, setStatus] = useState(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    let cancelled = false;
    (async () => {
      const health = await getHealth();
      if (cancelled) return;
      if (!health.ok) {
        setService({
          ok: false,
          message:
            health.body.message ||
            "Online reservations are closed. Please call (202) 555-4567.",
        });
        setSlots([]);
        return;
      }
      setService({ ok: true, message: "" });
      try {
        const list = await getSlots(date);
        if (!cancelled) {
          setSlots(list);
          setTimeslot((current) =>
            list.some((s) => s.timeslot === current) ? current : list[0]?.timeslot || "",
          );
        }
      } catch (err) {
        if (!cancelled) {
          setService({
            ok: false,
            message: err.message || "Available times could not be loaded.",
          });
          setSlots([]);
        }
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [date]);

  async function onSubmit(event) {
    event.preventDefault();
    setStatus(null);
    if (!timeslot) {
      setStatus({ kind: "error", text: "Please choose a time slot." });
      return;
    }
    if (!isValidGuests(Number(guests), restaurant.maxGuests)) {
      setStatus({
        kind: "error",
        text: `Number of guests must be from 1 to ${restaurant.maxGuests}.`,
      });
      return;
    }
    if (!isValidName(name)) {
      setStatus({ kind: "error", text: "Please enter the name for this reservation." });
      return;
    }
    if (!isValidEmail(email)) {
      setStatus({ kind: "error", text: "Please enter a valid email address." });
      return;
    }
    setBusy(true);
    try {
      const result = await createReservation({
        timeslot,
        guests: Number(guests),
        name: name.trim(),
        email: email.trim(),
        phone: phone.trim(),
      });
      setStatus({ kind: "ok", text: result.message });
    } catch (err) {
      setStatus({
        kind: "error",
        text: err.message || "The reservation could not be completed.",
      });
    } finally {
      setBusy(false);
    }
  }

  const openSlots = slots.filter((s) => s.tables_remaining > 0);
  const selected = slots.find((s) => s.timeslot === timeslot);

  return (
    <section className="wrap">
      <p className="kicker">{restaurant.tableCount} tables</p>
      <h1 className="section-title">Reservations</h1>
      <p className="muted">
        Choose a date and a half-hour seating during restaurant hours. We assign one of{" "}
        {restaurant.tableCount} tables at random when the slot is open.
      </p>

      {!service.ok ? <p className="banner error">{service.message}</p> : null}

      <form className="form" onSubmit={onSubmit} noValidate style={{ marginTop: "1.5rem" }}>
        <label htmlFor="res-date">
          Date
          <input
            id="res-date"
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </label>
        <label htmlFor="res-slot">
          Time slot
          <select
            id="res-slot"
            value={timeslot}
            onChange={(e) => setTimeslot(e.target.value)}
            disabled={!service.ok || openSlots.length === 0}
            required
          >
            {openSlots.length === 0 ? <option value="">No open seatings</option> : null}
            {openSlots.map((slot) => (
              <option key={slot.timeslot} value={slot.timeslot}>
                {new Date(slot.timeslot).toLocaleTimeString("en-US", {
                  hour: "numeric",
                  minute: "2-digit",
                  timeZone: "America/New_York",
                })}{" "}
                — {slot.tables_remaining} tables left
              </option>
            ))}
          </select>
        </label>
        {slots.length > 0 && openSlots.length === 0 ? (
          <p className="banner error">
            Every seating on this date is fully booked (all {restaurant.tableCount} tables).
            Please choose another day.
          </p>
        ) : null}
        <label htmlFor="res-guests">
          Number of guests
          <input
            id="res-guests"
            type="number"
            min="1"
            max={restaurant.maxGuests}
            value={guests}
            onChange={(e) => setGuests(e.target.value)}
            required
          />
        </label>
        <label htmlFor="res-name">
          Name
          <input
            id="res-name"
            type="text"
            autoComplete="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <label htmlFor="res-email">
          Email address
          <input
            id="res-email"
            type="email"
            autoComplete="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label htmlFor="res-phone">
          Phone number (optional)
          <input
            id="res-phone"
            type="tel"
            autoComplete="tel"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </label>
        <button className="btn" type="submit" disabled={busy || !service.ok || !timeslot}>
          {busy ? "Booking…" : "Book this table"}
        </button>
        {selected && service.ok ? (
          <p className="muted">
            Selected seating still has {selected.tables_remaining} of {restaurant.tableCount}{" "}
            tables free.
          </p>
        ) : null}
        {status ? <p className={`banner ${status.kind}`}>{status.text}</p> : null}
      </form>
    </section>
  );
}
