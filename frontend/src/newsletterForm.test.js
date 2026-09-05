import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = readFileSync(join(here, "components/NewsletterForm.jsx"), "utf8");
const layoutSrc = readFileSync(join(here, "components/Layout.jsx"), "utf8");

describe("NewsletterForm status (issue #85)", () => {
  it("clears success/error status when the React Router path changes", () => {
    assert.match(src, /from "react-router-dom"/);
    assert.match(src, /useLocation/);
    assert.match(src, /\[location\.pathname\]/);
    assert.match(src, /setStatus\(null\)/);
    assert.match(layoutSrc, /<NewsletterForm key=\{location\.pathname\}/);
  });

  it("auto-dismisses the banner after a short timeout (4–6s polish)", () => {
    const match = src.match(/NEWSLETTER_STATUS_DISMISS_MS = (\d+)/);
    assert.ok(match, "dismiss timeout constant is defined");
    const ms = Number(match[1]);
    assert.ok(ms >= 4000 && ms <= 6000, `expected 4000–6000ms, got ${ms}`);
    assert.match(src, /setTimeout/);
  });
});
