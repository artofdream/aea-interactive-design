import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const css = readFileSync(join(here, "styles/theme.css"), "utf8");
const operator = readFileSync(join(here, "pages/Operator.jsx"), "utf8");
const layout = readFileSync(join(here, "components/Layout.jsx"), "utf8");
const home = readFileSync(join(here, "pages/Home.jsx"), "utf8");
const menu = readFileSync(join(here, "pages/Menu.jsx"), "utf8");
const phoneQuery = "@media (max-width: 767px)";

function cssAfter(needle) {
  const at = css.indexOf(needle);
  assert.notEqual(at, -1, `theme.css missing ${needle}`);
  return css.slice(at);
}

describe("mobile UX contract (issue #91)", () => {
  it("has a 767px query that stacks operator tables as labeled cards", () => {
    const phone = cssAfter(phoneQuery);
    assert.match(phone, /attr\(data-label\)/);
    assert.match(phone, /\.data-table-wrap\s*\{[^}]*overflow:\s*visible/s);
    assert.match(operator, /data-label/);
    assert.match(operator, /label="Reservation id"/);
    assert.match(operator, /label="Email"/);
  });

  it("keeps tap targets at least 44px for nav, forms, gallery, footer, and home actions", () => {
    for (const needle of [
      ".nav-toggle",
      ".site-nav a",
      ".form input",
      ".newsletter-form button",
      ".gallery-grid button",
      ".lightbox-close",
      ".hero-actions a",
      ".footer-operator a",
    ]) {
      const block = cssAfter(needle);
      assert.match(block, /min-height:\s*44px/, `${needle} must set min-height 44px`);
    }
    assert.match(home, /className="hero-actions"/);
    assert.match(home, /className="card-actions"/);
  });

  it("uses overflow-safe auto-fit grids so 240px mins cannot force horizontal clip", () => {
    assert.match(css, /minmax\(min\(240px, 100%\), 1fr\)/);
    assert.match(css, /minmax\(min\(220px, 100%\), 1fr\)/);
    assert.equal(css.includes("min-width: 44rem"), false);
  });

  it("keeps /operator footer-only and does not invent FR-19", () => {
    assert.match(layout, /to="\/operator"/);
    const linksBlock = layout.slice(layout.indexOf("const LINKS"), layout.indexOf("export default"));
    assert.equal(linksBlock.includes("/operator"), false);
    assert.match(operator, /not FR-19/);
    assert.equal(/\*\*FR-19:\*\*/.test(`${css}\n${operator}\n${layout}\n${home}\n${menu}`), false);
  });

  it("keeps the Bruschetta honest placeholder (no fake photo mapping)", () => {
    assert.match(menu, /visual\.kind === "placeholder"/);
    assert.match(menu, /No matching photo/);
    assert.match(menu, /Bruschetta has no matching photo/);
  });
});
