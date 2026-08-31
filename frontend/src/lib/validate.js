/** Client-side checks. The Flask API is the authority (FR-7, FR-15). */

export const EMAIL_RE = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

export function isValidEmail(value) {
  if (typeof value !== "string") return false;
  return EMAIL_RE.test(value.trim());
}

export function isValidName(value) {
  if (typeof value !== "string") return false;
  const name = value.trim();
  return name.length > 0 && name.length <= 120;
}

export function isValidGuests(value, max = 8) {
  const n = Number(value);
  return Number.isInteger(n) && n >= 1 && n <= max;
}
