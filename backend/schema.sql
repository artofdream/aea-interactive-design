-- Café Fausse reservation schema (FR-17).
-- Customers: id, name, email, phone, newsletter signup.
-- Reservations: id, customer id, timeslot, table number.
-- Do not invent extra requirement IDs. Guest count is validated (FR-6) and not stored.

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    newsletter_signup BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers (id),
    timeslot TIMESTAMPTZ NOT NULL,
    table_number INTEGER NOT NULL CHECK (table_number >= 1 AND table_number <= 30),
    UNIQUE (timeslot, table_number)
);

CREATE INDEX IF NOT EXISTS reservations_timeslot_idx ON reservations (timeslot);
CREATE INDEX IF NOT EXISTS customers_email_idx ON customers (email);
