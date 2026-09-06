import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const src = readFileSync(
  join(dirname(fileURLToPath(import.meta.url)), "components/NewsletterForm.jsx"),
  "utf8",
);

describe("NewsletterForm status (issue #85)", () => {
  it("clears success/error status when the React Router path changes", () => {
    assert.match(src, /from "react-router-dom"/);
    assert.match(src, /useLocation/);
    assert.match(src, /\[location\.pathname\]/);
    assert.match(src, /setStatus\(null\)/);
  });

  it("mentions demo confirmation only when SES reports sent (Future #135)", () => {
    assert.match(src, /email_delivery/);
    assert.match(src, /demo, not a broadcast/);
    assert.match(src, /status === "sent"/);
  });

  it("auto-dismisses the banner after a short timeout (4–6s polish)", () => {
    const match = src.match(/NEWSLETTER_STATUS_DISMISS_MS = (\d+)/);
    assert.ok(match, "dismiss timeout constant is defined");
    const ms = Number(match[1]);
    assert.ok(ms >= 4000 && ms <= 6000, `expected 4000–6000ms, got ${ms}`);
    assert.match(src, /setTimeout/);
  });
});
