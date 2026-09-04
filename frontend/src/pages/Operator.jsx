import React, { useEffect, useState } from "react";
import freeze from "@shared/freeze.json";
import { apiFetch } from "../api.js";

function formatOperatorSlot(iso) {
  if (!iso) {
    return "";
  }
  const parsed = new Date(iso);
  if (Number.isNaN(parsed.getTime())) {
    return String(iso);
  }
  return parsed.toLocaleString("en-US", {
    timeZone: freeze.timezone,
    weekday: "short",
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}

function yesNo(flag) {
  return flag ? "yes" : "no";
}

export default function Operator() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError("");
    setData(null);
    apiFetch("/api/operator")
      .then((payload) => {
        if (cancelled) return;
        if (!payload || payload.ok !== true) {
          setError((payload && payload.error) || "Operator snapshot was not loaded.");
          return;
        }
        setData(payload);
      })
      .catch((err) => {
        if (cancelled) return;
        setError(err.message || "Operator snapshot was not loaded.");
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const reservations = data?.reservations || [];
  const newsletterOnly = data?.newsletter_only || [];

  return (
    <article>
      <h1>Operator</h1>
      <p className="hours-note">
        Recording view only. Lists recent customers and table assignments after a booking.
        Not a new SRS page (not FR-19) and not admin CRUD.
      </p>
      {loading ? <p>Loading…</p> : null}
      {error ? (
        <p className="banner is-error" role="alert">
          {error}
        </p>
      ) : null}
      {data ? (
        <>
          <h2>Reservations</h2>
          {reservations.length ? (
            <div className="data-table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Newsletter</th>
                    <th scope="col">Time slot</th>
                    <th scope="col">Table</th>
                    <th scope="col">Guests</th>
                    <th scope="col">Reservation id</th>
                  </tr>
                </thead>
                <tbody>
                  {reservations.map((row) => (
                    <tr key={row.reservation_id}>
                      <td>{row.customer_name}</td>
                      <td>{row.email}</td>
                      <td>{yesNo(row.newsletter)}</td>
                      <td>{formatOperatorSlot(row.time_slot)}</td>
                      <td>{row.table_number}</td>
                      <td>{row.guest_count}</td>
                      <td>{row.reservation_id}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p>No reservations stored.</p>
          )}
          <h2>Newsletter only</h2>
          {newsletterOnly.length ? (
            <div className="data-table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Newsletter</th>
                  </tr>
                </thead>
                <tbody>
                  {newsletterOnly.map((row) => (
                    <tr key={row.customer_id}>
                      <td>{row.customer_name}</td>
                      <td>{row.email}</td>
                      <td>{yesNo(row.newsletter)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <p>No newsletter-only customers stored.</p>
          )}
        </>
      ) : null}
    </article>
  );
}
