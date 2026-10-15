// Renders every slide of every deck in headless Chrome and reports the ones whose content does not fit.
// Usage: start the slides server (`yarn serve-slides`) and run `node tools/scripts/slide-overflow-check.cjs`.
const path = require("path");
const fs = require("fs");
const root = path.resolve(__dirname, "..", "..");
const puppeteer = require(path.join(root, "node_modules", "puppeteer"));
const chrome = process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const base = process.env.SLIDES_URL || "http://localhost:1948";
const decks = fs.readdirSync(path.join(root, "content", "eidas")).filter((d) => /^\d\d-/.test(d)).sort();

(async () => {
  const browser = await puppeteer.launch({ executablePath: chrome, headless: "new", args: ["--window-size=1400,900"] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });
  let total = 0;
  const bad = [];
  for (const d of decks) {
    await page.goto(`${base}/content/eidas/${d}/slides.md`, { waitUntil: "networkidle0", timeout: 60000 });
    await page.waitForFunction("window.Reveal && Reveal.isReady && Reveal.isReady()", { timeout: 30000 });
    const res = await page.evaluate(async () => {
      const out = [];
      const cfg = Reveal.getConfig();
      for (const s of Reveal.getSlides()) {
        const idx = Reveal.getIndices(s);
        Reveal.slide(idx.h, idx.v || 0);
        await new Promise((r) => setTimeout(r, 60));
        const title = (s.querySelector("h1,h2,h3") || {}).textContent || "(sense títol)";
        const hOver = s.scrollHeight - cfg.height;
        let wOver = 0, wWho = "";
        for (const el of s.querySelectorAll("pre, table, img, p, ul, ol, h1, h2")) {
          const over = Math.max(el.scrollWidth - el.clientWidth, el.offsetLeft + el.offsetWidth - s.clientWidth);
          if (over > wOver) {
            wOver = over;
            wWho = el.tagName.toLowerCase();
          }
        }
        out.push({ h: idx.h, v: idx.v || 0, title: title.trim(), height: s.scrollHeight, hOver, wOver, wWho });
      }
      return out;
    });
    total += res.length;
    for (const r of res) if (r.hOver > 0 || r.wOver > 2) bad.push({ deck: d, ...r });
    const tallest = res.reduce((a, b) => (a.height > b.height ? a : b));
    console.log(
      `${d.padEnd(22)} ${String(res.length).padStart(3)} diapositives | la més alta: ${tallest.height}px de ${900} (${
        tallest.title.slice(0, 40)
      })`,
    );
  }
  console.log(`\nTOTAL ${total} diapositives; amb desbordament: ${bad.length}`);
  for (const b of bad) {
    console.log(
      `  ${b.deck} #/${b.h}/${b.v}  "${b.title.slice(0, 45)}"  vertical:+${Math.max(0, b.hOver)}px  horitzontal:+${
        Math.round(b.wOver)
      }px (${b.wWho})`,
    );
  }
  await browser.close();
  process.exit(bad.length ? 1 : 0);
})().catch((e) => {
  console.error("ERROR", e.message);
  process.exit(2);
});
