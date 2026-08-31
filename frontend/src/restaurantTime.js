/**
 * Restaurant-local calendar and clock (Washington, DC).
 * Must match /api/slots, which uses freeze.timezone (America/New_York).
 * Do not use the browser calendar for reservation dates or slot labels.
 */

export function todayISODate(now, timeZone) {
  if (!timeZone) {
    throw new Error("Restaurant timezone is required.");
  }
  const instant = now ?? new Date();
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(instant);
  const year = parts.find((part) => part.type === "year")?.value;
  const month = parts.find((part) => part.type === "month")?.value;
  const day = parts.find((part) => part.type === "day")?.value;
  if (!year || !month || !day) {
    throw new Error("Could not read the restaurant local date.");
  }
  return `${year}-${month}-${day}`;
}

export function formatSlot(iso, timeZone) {
  if (!timeZone) {
    throw new Error("Restaurant timezone is required.");
  }
  return new Date(iso).toLocaleTimeString("en-US", {
    hour: "numeric",
    minute: "2-digit",
    timeZone,
  });
}
