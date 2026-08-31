import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

import { formatSlot, todayISODate } from "./restaurantTime.js";

const freeze = JSON.parse(
  readFileSync(join(dirname(fileURLToPath(import.meta.url)), "../../shared/freeze.json"), "utf8"),
);

const TZ = freeze.timezone;

function clockLabel(value) {
  return String(value).replace(/\u202f|\u00a0/g, " ");
}

describe("restaurant timezone freeze", () => {
  it("is America/New_York (Washington, DC hours)", () => {
    assert.equal(TZ, "America/New_York");
  });
});

describe("todayISODate", () => {
  it("requires the restaurant timezone (no browser-calendar fallback)", () => {
    assert.throws(() => todayISODate(new Date("2026-08-31T04:30:00Z")), /timezone is required/);
  });

  it("uses the New York calendar when UTC is already the next morning", () => {
    // 2026-08-31 00:30 EDT = 04:30 UTC. Pacific would still be 2026-08-30.
    assert.equal(todayISODate(new Date("2026-08-31T04:30:00Z"), TZ), "2026-08-31");
  });

  it("stays on the New York date when Europe is already the next day", () => {
    // 2026-08-31 23:30 EDT = 2026-09-01 03:30 UTC. Berlin would be 2026-09-01.
    assert.equal(todayISODate(new Date("2026-09-01T03:30:00Z"), TZ), "2026-08-31");
  });

  it("uses Eastern Date when Tokyo is already the restaurant's next morning", () => {
    // 2026-08-30 21:00 EDT = 2026-08-31 01:00 UTC. Tokyo would be 2026-08-31.
    assert.equal(todayISODate(new Date("2026-08-31T01:00:00Z"), TZ), "2026-08-30");
  });
});

describe("formatSlot", () => {
  it("requires the restaurant timezone (no browser-clock fallback)", () => {
    assert.throws(() => formatSlot("2028-06-15T17:00:00-04:00"), /timezone is required/);
  });

  it("labels first seating as 5:00 PM Eastern, not Pacific 2:00 PM", () => {
    const label = clockLabel(formatSlot("2028-06-15T17:00:00-04:00", TZ));
    assert.equal(label, "5:00 PM");
    assert.notEqual(label, "2:00 PM");
  });

  it("labels Monday–Saturday last seating as 10:00 PM Eastern", () => {
    assert.equal(clockLabel(formatSlot("2028-06-15T22:00:00-04:00", TZ)), "10:00 PM");
  });

  it("labels Sunday last seating as 8:00 PM Eastern (not 10:00 PM)", () => {
    assert.equal(clockLabel(formatSlot("2028-06-18T20:00:00-04:00", TZ)), "8:00 PM");
  });

  it("keeps 5:00 PM in Eastern Standard Time", () => {
    assert.equal(clockLabel(formatSlot("2028-01-15T17:00:00-05:00", TZ)), "5:00 PM");
  });
});
