-- FR-17: Customers and Reservations.
-- Extra columns (guest_count, timestamps) support FR-6 and NFR-9; they do not invent new requirement IDs.

CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email_address TEXT NOT NULL UNIQUE,
    phone_number TEXT,
    newsletter_signup BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS reservations (
    reservation_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers (customer_id),
    time_slot TIMESTAMPTZ NOT NULL,
    table_number INTEGER NOT NULL CHECK (table_number BETWEEN 1 AND 30),
    guest_count INTEGER NOT NULL CHECK (guest_count >= 1 AND guest_count <= 20),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- NFR-5: a slot cannot be assigned the same table twice; 30 distinct tables max.
CREATE UNIQUE INDEX IF NOT EXISTS reservations_slot_table
    ON reservations (time_slot, table_number);

CREATE INDEX IF NOT EXISTS reservations_time_slot
    ON reservations (time_slot);
