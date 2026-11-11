// Builds the map figures for explainer.html from Natural Earth coastlines.
// Run: npm i world-atlas@2.0.2 topojson-client@3.1.0 d3-geo@3.1.1 && node maps.mjs > maps.json
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { feature } from "topojson-client";
import { geoPath, geoConicEqualArea, geoEquirectangular, geoOrthographic, geoMercator, geoCircle } from "d3-geo";
const require = createRequire(import.meta.url);
const load = (n) => { const t = JSON.parse(readFileSync(require.resolve("world-atlas/" + n))); return feature(t, t.objects.land); };
const land110 = load("land-110m.json"), land50 = load("land-50m.json"), land10 = load("land-10m.json");
const box = (a, b, c, d) => ({ type: "MultiPoint", coordinates: [[a, b], [c, b], [a, d], [c, d], [(a + c) / 2, b], [(a + c) / 2, d]] });
const f = (n) => Math.round(n * 10) / 10;
const out = {};
const txt = (p, s, o = {}) => `<text x="${f(p[0] + (o.dx || 0))}" y="${f(p[1] + (o.dy || 0))}" font-size="${o.size || 13}"${o.bold ? ' font-weight="600"' : ""}${o.anchor ? ` text-anchor="${o.anchor}"` : ""} class="halo${o.muted ? " t-muted" : ""}">${s}</text>`;
const arrow = (pr, a, b, cls, w, extra = "") => { const p = pr(a), q = pr(b); return `<path d="M${f(p[0])} ${f(p[1])}L${f(q[0])} ${f(q[1])}" class="${cls} nofill" stroke-width="${w}" stroke-linecap="round" ${extra}/>`; };

// A. East Asia: the snow machine from above.
{
  const W = 720, H = 400;
  const pr = geoConicEqualArea().parallels([35, 55]).rotate([-131, 0]).center([0, 45]).fitExtent([[0, 0], [W, H]], box(119, 32, 151, 55)).clipExtent([[0, 0], [W, H]]);
  const path = geoPath(pr).digits(1);
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Map of north-east Asia. Cold wind blows from Siberia across the Sea of Japan, forms lines of cloud over the water and drops snow on the west coast of Japan and Hokkaido."><defs><marker id="mA" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" class="f-cold"/></marker></defs>`;
  s += `<rect width="${W}" height="${H}" class="f-sea"/><path d="${path(land50)}" class="f-land s-coast" stroke-width=".6"/>`;
  const streaks = [[[130.0, 38.9], [135.2, 36.3]], [[130.3, 40.9], [136.9, 37.5]], [[131.8, 42.4], [138.6, 38.7]], [[133.2, 43.0], [139.5, 40.1]], [[135.0, 44.0], [139.8, 41.7]], [[136.8, 45.2], [140.1, 43.3]], [[138.6, 46.9], [141.3, 44.9]]];
  for (const [a, b] of streaks) s += arrow(pr, a, b, "s-cloud", 6, 'stroke-dasharray="1 10"');
  for (const [a, b] of [[[122, 50.5], [131, 46]], [[128, 53.5], [137, 49]], [[121, 45.5], [128.5, 41.8]]]) s += arrow(pr, a, b, "s-cold", 5, 'marker-end="url(#mA)"');
  for (const c of [[140.5, 42.6], [141.5, 43.7], [141.9, 44.7], [140.2, 40.4], [139.6, 38.6], [138.4, 37.2], [136.6, 36.5], [140.9, 41.2]]) { const p = pr(c); s += `<circle cx="${f(p[0])}" cy="${f(p[1])}" r="3.2" class="f-cold s-surface" stroke-width="1"/>`; }
  const nis = pr([140.69, 42.86]); s += `<circle cx="${f(nis[0])}" cy="${f(nis[1])}" r="5" class="f-ink s-surface" stroke-width="1.5"/>`;
  const tok = pr([139.7, 35.7]); s += `<circle cx="${f(tok[0])}" cy="${f(tok[1])}" r="3" class="f-surface s-ink" stroke-width="1.5"/>`;
  s += txt(pr([120, 54]), "Siberia", { size: 17, bold: 1 }) + txt(pr([120, 54]), "1  Cold, dry wind blows out", { dy: 19, size: 14, bold: 1 });
  s += txt(pr([134.2, 40.3]), "Sea of Japan", { size: 15, bold: 1, anchor: "middle" }) + txt(pr([134.2, 40.3]), "2  The warm sea adds moisture", { dy: 18, size: 14, bold: 1, anchor: "middle" });
  s += txt(pr([144.6, 44.6]), "Hokkaido", { size: 15, bold: 1 }) + txt(nis, "Niseko", { dx: -9, dy: 4, anchor: "end" }) + txt(tok, "Tokyo", { dx: 8, dy: 4, muted: 1 });
  s += txt(pr([146.5, 35.2]), "Pacific Ocean", { muted: 1, anchor: "middle" }) + txt(pr([121.5, 40.6]), "China", { muted: 1 }) + txt(pr([127.6, 36.6]), "Korea", { muted: 1, size: 12, anchor: "middle" });
  s += txt(pr([143.3, 40.4]), "3  Snow falls on the", { size: 14, bold: 1 }) + txt(pr([143.3, 40.4]), "west-facing coast", { size: 14, bold: 1, dy: 17 });
  out.asia = s + "</svg>";
}

// B. Pacific: where El Nino sits and what it does near Japan.
{
  const W = 720, H = 362;
  const pr = geoEquirectangular().rotate([-170, 0]).fitExtent([[0, 0], [W, H]], box(-65 + 170, -30, 118 + 170 - 360, 62));
  pr.fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [[105, -30], [105, 62], [-72, -30], [-72, 62]] }).clipExtent([[0, 0], [W, H]]);
  const path = geoPath(pr).digits(1);
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Map of the Pacific Ocean. A tongue of unusually warm water lies along the equator off South America. It shifts the pressure pattern over the North Pacific and weakens the winter wind over Japan."><defs><marker id="mB" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" class="f-cold"/></marker><marker id="mBi" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" class="f-ink"/></marker></defs>`;
  s += `<rect width="${W}" height="${H}" class="f-sea"/>`;
  const tongue = (lw, le, lat, op) => { const t = pr([lw, 0]), a = pr([le, lat]), b = pr([le, -lat]), m = (t[0] + a[0]) / 2; return `<path d="M${f(t[0])} ${f(t[1])}Q${f(m)} ${f(a[1])} ${f(a[0])} ${f(a[1])}L${f(b[0])} ${f(b[1])}Q${f(m)} ${f(b[1])} ${f(t[0])} ${f(t[1])}z" class="f-warm" opacity="${op}"/>`; };
  s += tongue(175, -76, 9, .28) + tongue(-165, -76, 6.5, .45) + tongue(-140, -76, 4.5, .9);
  const e0 = pr([105, 0]), e1 = pr([-72, 0]);
  s += `<path d="${path(land110)}" class="f-land s-coast" stroke-width=".5"/><line x1="0" x2="${W}" y1="${f(e0[1])}" y2="${f(e1[1])}" class="s-muted" stroke-width="1" stroke-dasharray="3 5"/>`;
  const a0 = pr([-135, 9]), a1 = pr([-172, 40]), ac = pr([-128, 36]);
  s += `<path d="M${f(a0[0])} ${f(a0[1])}Q${f(ac[0])} ${f(ac[1])} ${f(a1[0])} ${f(a1[1])}" class="s-ink nofill" stroke-width="1.8" stroke-dasharray="5 5" marker-end="url(#mBi)"/>`;
  const lo = pr([172, 48]); s += `<circle cx="${f(lo[0])}" cy="${f(lo[1])}" r="26" class="nofill s-ink" stroke-width="1.5" stroke-dasharray="4 4"/>`;
  s += arrow(pr, [116, 50], [131, 41], "s-cold", 2.5, 'stroke-dasharray="7 6" marker-end="url(#mB)"');
  const jp = pr([138, 36.5]); s += `<circle cx="${f(jp[0])}" cy="${f(jp[1])}" r="12" class="nofill s-ink" stroke-width="1.8"/>`;
  s += txt(jp, "Japan", { dx: 16, dy: 5, size: 14, bold: 1 });
  s += txt(pr([-124, -9]), "1  Water up to 4 °C warmer than normal", { size: 14, bold: 1, anchor: "middle", dy: 8 });
  s += txt(pr([-124, 26]), "2  The heat shifts the weather", { size: 14, bold: 1 }) + txt(pr([-124, 26]), "pattern across the ocean", { size: 14, bold: 1, dy: 17 });
  s += txt(lo, "3  The storm zone here", { size: 14, bold: 1, dx: 34, dy: -2 }) + txt(lo, "weakens on Japan's side", { size: 14, bold: 1, dx: 34, dy: 15 });
  s += txt(pr([108, 57]), "4  Weaker winter", { size: 14, bold: 1 }) + txt(pr([108, 57]), "wind over Japan", { size: 14, bold: 1, dy: 17 });
  s += txt(pr([107, 2.5]), "the equator", { muted: 1, size: 12 }) + txt(pr([-105, 45]), "North America", { muted: 1, anchor: "middle" }) + txt(pr([134, -24]), "Australia", { muted: 1, anchor: "middle" }) + txt(pr([112, 32]), "China", { muted: 1, anchor: "middle" }) + txt(pr([175, 14]), "Pacific Ocean", { muted: 1, anchor: "middle" });
  out.pacific = s + "</svg>";
}

// C. The Arctic from above: tight ring and wobbly ring.
{
  const W = 720, H = 372, R = 158;
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Two views of the Arctic from above. On the left a tight ring of wind keeps the cold air over the pole. On the right the ring has buckled and a lobe of cold air reaches Japan.">`;
  const globe = (cx, title, wob) => {
    let g = 0, pr;
    for (const cand of [0, 90, 180, 270]) { // turn the globe until Japan is at the bottom
      const t = geoOrthographic().rotate([0, -90, cand]).translate([cx, 204]).scale(R / Math.sin(64 * Math.PI / 180)).clipAngle(64);
      const j = t([138, 37]); if (Math.abs(j[0] - cx) < 60 && j[1] > 204) { g = cand; pr = t; }
    }
    if (!pr) { // fine search
      for (let c = 0; c < 360; c += 2) { const t = geoOrthographic().rotate([0, -90, c]).translate([cx, 204]).scale(R / Math.sin(64 * Math.PI / 180)).clipAngle(64); const j = t([138, 37]); if (Math.abs(j[0] - cx) < 8 && j[1] > 204) { pr = t; break; } }
    } else { let best = 1e9, bp = pr; for (let c = g - 60; c <= g + 60; c += 1) { const t = geoOrthographic().rotate([0, -90, c]).translate([cx, 204]).scale(R / Math.sin(64 * Math.PI / 180)).clipAngle(64); const j = t([138, 37]); if (j[1] > 204 && Math.abs(j[0] - cx) < best) { best = Math.abs(j[0] - cx); bp = t; } } pr = bp; }
    const path = geoPath(pr).digits(1);
    let o = txt([cx, 22], title, { size: 15, bold: 1, anchor: "middle" });
    o += `<circle cx="${cx}" cy="204" r="${R}" class="f-sea"/><path d="${path(land110)}" class="f-land s-coast" stroke-width=".5"/>`;
    const d = (a, b) => { let x = Math.abs(a - b) % 360; return x > 180 ? 360 - x : x; };
    const pts = [];
    for (let lon = -180; lon < 180; lon += 4) {
      const r = wob ? 23 + 20 * Math.exp(-Math.pow(d(lon, 136) / 24, 2)) + 11 * Math.exp(-Math.pow(d(lon, 25) / 26, 2)) - 7 * Math.exp(-Math.pow(d(lon, -60) / 40, 2)) - 5 * Math.exp(-Math.pow(d(lon, 85) / 22, 2)) : 23;
      pts.push(pr([lon, 90 - r]));
    }
    o += `<path d="M${pts.map((p) => f(p[0]) + " " + f(p[1])).join("L")}z" class="f-cold s-cold" fill-opacity=".28" stroke-width="4.5" stroke-linejoin="round"${wob ? ' stroke-dasharray="10 6"' : ""}/>`;
    o += `<circle cx="${cx}" cy="204" r="${R}" class="nofill s-coast" stroke-width="1"/>`;
    const np = pr([0, 90]), jp = pr([138, 36.5]);
    o += txt(np, "Arctic cold", { size: 13, bold: 1, anchor: "middle", dy: 4 });
    o += `<circle cx="${f(jp[0])}" cy="${f(jp[1])}" r="9" class="nofill s-ink" stroke-width="1.8"/>` + txt(jp, "Japan", { dx: 14, dy: 5, bold: 1 });
    o += txt(pr([100, 58]), "Siberia", { muted: 1, anchor: "middle", size: 12 }) + txt(pr([-100, 50]), "North America", { muted: 1, anchor: "middle", size: 12 }) + txt(pr([15, 49]), "Europe", { muted: 1, anchor: "middle", size: 12 });
    if (wob) o += txt(pr([150, 52]), "a cold burst", { dx: 40, dy: -6, size: 13, bold: 1 });
    return o;
  };
  s += globe(180, "Tight ring: cold locked in", false) + globe(540, "Buckled ring: cold spills south", true);
  out.arctic = s + "</svg>";
}

// D. Hokkaido: where the snow lands.
{
  const W = 720, H = 440;
  const pr = geoMercator().fitExtent([[0, 0], [W, H]], box(138.0, 41.25, 148.2, 45.75)).clipExtent([[-2, -2], [W + 2, H + 2]]);
  const path = geoPath(pr).digits(1);
  // Keep only the islands near Hokkaido: clipping the mainland polygon fills the whole frame.
  const near = { type: "MultiPolygon", coordinates: land10.features[0].geometry.coordinates.filter((poly) => { const xs = poly[0].map((c) => c[0]), ys = poly[0].map((c) => c[1]); const x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys); return x1 > 137 && x0 < 149 && y1 > 40.5 && y0 < 46.5 && x1 - x0 < 30; }) };
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Map of Hokkaido. Wind from the north-west crosses the Sea of Japan and hits the west side first, where Niseko, Rusutsu and Kiroro are. Furano, Tomamu and Asahidake sit in the colder, drier centre."><defs><marker id="mD" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" class="f-cold"/></marker></defs>`;
  s += `<rect width="${W}" height="${H}" class="f-sea"/><path d="${path(near)}" class="f-land s-coast" stroke-width=".7"/>`;
  for (const [a, b] of [[[138.3, 44.2], [139.7, 43.3]], [[138.9, 45.3], [141.0, 44.5]], [[138.2, 43.1], [139.6, 42.5]]]) s += arrow(pr, a, b, "s-cold", 5, 'marker-end="url(#mD)"');
  const west = [["Niseko", 140.69, 42.86, { dx: -10, dy: 5, anchor: "end" }], ["Rusutsu", 140.9, 42.75, { dx: 4, dy: 20 }], ["Kiroro", 140.98, 43.07, { dx: -4, dy: -11, anchor: "end" }]];
  const mid = [["Furano", 142.38, 43.33, { dx: 10, dy: 5 }], ["Tomamu", 142.63, 43.06, { dx: 10, dy: 12 }], ["Asahidake", 142.85, 43.66, { dx: 10, dy: 2 }]];
  for (const [n, x, y, o] of west) { const p = pr([x, y]); s += `<circle cx="${f(p[0])}" cy="${f(p[1])}" r="6.5" class="f-cold s-surface" stroke-width="2"/>` + txt(p, n, { ...o, bold: 1, size: 14 }); }
  for (const [n, x, y, o] of mid) { const p = pr([x, y]); s += `<path d="M${f(p[0])} ${f(p[1] - 7)}L${f(p[0] + 7)} ${f(p[1] + 5.5)}L${f(p[0] - 7)} ${f(p[1] + 5.5)}z" class="f-ink s-surface" stroke-width="2"/>` + txt(p, n, { ...o, bold: 1, size: 14 }); }
  const sap = pr([141.35, 43.06]); s += `<rect x="${f(sap[0] - 4)}" y="${f(sap[1] - 4)}" width="8" height="8" class="f-surface s-ink" stroke-width="1.6"/>` + txt(sap, "Sapporo", { dx: 9, dy: -5, muted: 1 });
  const cts = pr([141.69, 42.78]); s += `<rect x="${f(cts[0] - 3)}" y="${f(cts[1] - 3)}" width="6" height="6" class="f-surface s-ink" stroke-width="1.4"/>` + txt(cts, "airport", { dx: 8, dy: 12, muted: 1, size: 12 });
  s += txt(pr([139.0, 41.75]), "Sea of Japan", { size: 15, bold: 1, anchor: "middle" }) + txt(pr([146.6, 44.7]), "Sea of Okhotsk", { muted: 1, anchor: "middle" }) + txt(pr([143.1, 45.55]), "Snowfall in strong El Niño winters, against usual", { size: 13, bold: 1 }) + txt(pr([143.1, 45.55]), "west: December 80 to 86%, January 94 to 100%", { size: 13, dy: 19 }) + txt(pr([143.1, 45.55]), "centre: December 84 to 98%, January 104 to 126%", { size: 13, dy: 38 }) + txt(pr([144.6, 41.7]), "Pacific Ocean", { muted: 1, anchor: "middle" });
  s += txt(pr([138.15, 45.5]), "winter wind", { size: 13, bold: 1 });
  out.hokkaido = s + "</svg>";
}
process.stdout.write(JSON.stringify(out));
