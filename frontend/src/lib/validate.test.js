import { describe, expect, it } from "vitest";
import { isValidEmail, isValidGuests, isValidName } from "./validate";

describe("email (FR-15)", () => {
  it("accepts a normal address", () => {
    expect(isValidEmail("diner@example.com")).toBe(true);
  });
  it("rejects missing domain", () => {
    expect(isValidEmail("diner@")).toBe(false);
  });
  it("rejects empty", () => {
    expect(isValidEmail("")).toBe(false);
  });
});

describe("name (FR-6)", () => {
  it("requires a non-empty name", () => {
    expect(isValidName("  ")).toBe(false);
    expect(isValidName("Ada")).toBe(true);
  });
});

describe("guests (FR-6)", () => {
  it("allows 1 through 8", () => {
    expect(isValidGuests(1)).toBe(true);
    expect(isValidGuests(8)).toBe(true);
    expect(isValidGuests(0)).toBe(false);
    expect(isValidGuests(9)).toBe(false);
  });
});
