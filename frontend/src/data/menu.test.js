import { describe, expect, it } from "vitest";
import { formatPrice, menuCategories } from "./menu";
import { restaurant } from "./restaurant";

describe("FR-5 menu freeze", () => {
  const items = Object.fromEntries(
    menuCategories.flatMap((c) => c.items.map((i) => [i.name, i.price])),
  );

  it("keeps official prices", () => {
    expect(items.Bruschetta).toBe(8.5);
    expect(items["Caesar Salad"]).toBe(9.0);
    expect(items["Grilled Salmon"]).toBe(22.0);
    expect(items["Ribeye Steak"]).toBe(28.0);
    expect(items["Vegetable Risotto"]).toBe(18.0);
    expect(items.Tiramisu).toBe(7.5);
    expect(items.Cheesecake).toBe(7.0);
    expect(items["Red Wine (Glass)"]).toBe(10.0);
    expect(items["White Wine (Glass)"]).toBe(9.0);
    expect(items["Craft Beer"]).toBe(6.0);
    expect(items.Espresso).toBe(3.0);
  });

  it("formats currency with two decimals", () => {
    expect(formatPrice(8.5)).toBe("$8.50");
    expect(formatPrice(9)).toBe("$9.00");
  });
});

describe("FR facts freeze", () => {
  it("keeps the official name, address, phone, hours, and owners", () => {
    expect(restaurant.name).toBe("Café Fausse");
    expect(restaurant.address.line).toBe(
      "1234 Culinary Ave, Suite 100, Washington, DC 20002",
    );
    expect(restaurant.phone).toBe("(202) 555-4567");
    expect(restaurant.founded).toBe(2010);
    expect(restaurant.owners.map((o) => o.name)).toEqual([
      "Chef Antonio Rossi",
      "Maria Lopez",
    ]);
    expect(restaurant.tableCount).toBe(30);
  });

  it("keeps awards and reviews from FR-14", () => {
    expect(restaurant.awards).toHaveLength(3);
    expect(restaurant.reviews).toHaveLength(2);
    expect(restaurant.reviews[0].source).toBe("Gourmet Review");
    expect(restaurant.reviews[1].source).toBe("The Daily Bite");
  });
});
