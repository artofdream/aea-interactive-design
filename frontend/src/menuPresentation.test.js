import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";

const root = join(dirname(fileURLToPath(import.meta.url)), "../..");
const freeze = JSON.parse(readFileSync(join(root, "shared/freeze.json"), "utf8"));
const presentation = JSON.parse(
  readFileSync(join(root, "shared/menu-presentation.json"), "utf8"),
);

test("menu presentation covers freeze items and does not carry prices", () => {
  const freezeNames = freeze.menu.flatMap((category) => category.items.map((item) => item.name));
  assert.deepEqual(Object.keys(presentation.items).sort(), [...freezeNames].sort());
  for (const visual of Object.values(presentation.items)) {
    assert.equal(Object.hasOwn(visual, "price"), false);
  }
  assert.equal(presentation.items["Ribeye Steak"].file, "gallery-ribeye-steak.webp");
  assert.equal(presentation.items.Bruschetta.file, null);
});
