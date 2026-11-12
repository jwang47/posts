// Builds the drawn figures for explainer.html: four maps from Natural Earth
// coastlines and two diagrams. Each figure has a wide layout and a narrow
// (phone) layout, so nothing scrolls sideways and the text stays readable.
// The steps of each figure are numbered badges; the words are an HTML list
// under the figure, not labels on the map.
//
// Run in a folder with the three packages, then inject:
//   npm i world-atlas@2.0.2 topojson-client@3.1.0 d3-geo@3.1.1
//   node make_maps.mjs > figures.json && python3 inject_figures.py figures.json
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { feature } from "topojson-client";
import { geoPath, geoConicEqualArea, geoEquirectangular, geoOrthographic, geoMercator } from "d3-geo";
const require = createRequire(import.meta.url);
const load = (n) => { const t = JSON.parse(readFileSync(require.resolve("world-atlas/" + n))); return feature(t, t.objects.land); };
const land110 = load("land-110m.json"), land50 = load("land-50m.json"), land10 = load("land-10m.json");
const box = (a, b, c, d) => ({ type: "MultiPoint", coordinates: [[a, b], [c, b], [a, d], [c, d], [(a + c) / 2, b], [(a + c) / 2, d]] });
const f = (n) => Math.round(n * 10) / 10;
const txt = (p, s, o = {}) => `<text x="${f(p[0] + (o.dx || 0))}" y="${f(p[1] + (o.dy || 0))}" font-size="${o.size || 13}"${o.bold ? ' font-weight="600"' : ""}${o.anchor ? ` text-anchor="${o.anchor}"` : ""} class="${o.plain ? "" : "halo"}${o.muted ? " t-muted" : ""}">${s}</text>`;
const line = (p, q, cls, w, extra = "") => `<path d="M${f(p[0])} ${f(p[1])}L${f(q[0])} ${f(q[1])}" class="${cls} nofill" stroke-width="${w}" stroke-linecap="round" ${extra}/>`;
const badge = (p, n) => `<circle cx="${f(p[0])}" cy="${f(p[1])}" r="11.5" class="f-ink s-surface" stroke-width="2"/><text x="${f(p[0])}" y="${f(p[1] + 4.6)}" font-size="13.5" font-weight="700" text-anchor="middle" class="f-surface">${n}</text>`;
const head = (id, cls) => `<marker id="${id}" viewBox="0 0 10 10" refX="6.5" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto"><path d="M0 0L10 5L0 10z" class="${cls}"/></marker>`;
const open = (W, H, kind, label, defs = "") => `<svg class="${kind}" viewBox="0 0 ${W} ${H}" role="img" aria-label="${label}"><defs>${defs}</defs>`;
const both = (fn) => `${fn(false)}\n${fn(true)}`;
const out = {};

// A. North-east Asia: the snow machine from above.
out.asia = both((n) => {
  const W = n ? 340 : 720, H = n ? 372 : 400, id = n ? "mAn" : "mAw";
  const pr = geoConicEqualArea().parallels([35, 55]).rotate([-134, 0]).center([0, 43])
    .fitExtent([[0, 0], [W, H]], n ? box(127.5, 33.5, 146.5, 51) : box(119, 32, 151, 55)).clipExtent([[0, 0], [W, H]]);
  const path = geoPath(pr).digits(1);
  let s = open(W, H, n ? "narrow" : "wide", "Map of north-east Asia. Cold wind blows from Siberia across the Sea of Japan, forms lines of cloud over the water and drops snow on the west coast of Japan and Hokkaido.", head(id, "f-cold"));
  s += `<rect width="${W}" height="${H}" class="f-sea"/><path d="${path(land50)}" class="f-land s-coast" stroke-width=".6"/>`;
  // Cloud lines: they start part of the way across, once the air has picked up moisture, and thicken toward Japan.
  const streaks = [[[130.0, 38.9], [135.4, 36.2]], [[130.3, 40.9], [137.0, 37.4]], [[131.8, 42.4], [138.7, 38.6]], [[133.2, 43.0], [139.6, 40.0]], [[135.0, 44.0], [139.9, 41.6]], [[136.8, 45.2], [140.2, 43.2]], [[138.6, 46.9], [141.4, 44.8]]];
  const dense = [];
  for (let i = 0; i < streaks.length; i++) { dense.push(streaks[i]); if (i + 1 < streaks.length) dense.push(streaks[i].map((p, k) => [(p[0] + streaks[i + 1][k][0]) / 2, (p[1] + streaks[i + 1][k][1]) / 2])); }
  dense.forEach(([a, b], i) => { // each line is a thin wedge that widens toward Japan
    const t0 = i % 2 ? 0.42 : 0.26, p = pr([a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0]), q = pr(b);
    const len = Math.hypot(q[0] - p[0], q[1] - p[1]), ux = (q[1] - p[1]) / len, uy = -(q[0] - p[0]) / len, w = (n ? 2.3 : 3) * (i % 2 ? 0.75 : 1);
    s += `<path d="M${f(p[0])} ${f(p[1])}L${f(q[0] + ux * w)} ${f(q[1] + uy * w)}L${f(q[0] - ux * w)} ${f(q[1] - uy * w)}z" class="f-cloud" opacity="${i % 2 ? 0.6 : 0.85}"/>`;
  });
  // The snow belt: the coast that faces the wind.
  const belt = [[141.75, 45.2], [141.6, 44.2], [141.3, 43.3], [140.4, 42.9], [140.0, 41.9], [140.0, 40.4], [139.8, 39.2], [139.3, 38.2], [138.4, 37.3], [137.0, 36.9], [136.2, 36.1]].map(pr);
  const beltD = "M" + belt.map((p) => f(p[0]) + " " + f(p[1])).join("L");
  s += `<path d="${beltD}" class="s-cold nofill" stroke-width="${n ? 13 : 15}" stroke-linecap="round" stroke-linejoin="round" opacity=".45"/><path d="${beltD}" class="s-cloud nofill" stroke-width="${n ? 5 : 6}" stroke-linecap="round" stroke-linejoin="round"/>`;
  const arrows = n ? [[[128.2, 49.6], [133.2, 46.0]], [[127.8, 46.6], [131.6, 43.6]], [[133.6, 50.4], [138.2, 47.6]]] : [[[121.5, 51.5], [131.5, 46.2]], [[127, 54.2], [137.3, 49.2]], [[120.5, 46.3], [129, 42.2]]];
  for (const [a, b] of arrows) s += line(pr(a), pr(b), "s-cold", n ? 4.5 : 5.5, `marker-end="url(#${id})"`);
  const nis = pr([140.69, 42.86]), tok = pr([139.7, 35.7]);
  s += `<circle cx="${f(nis[0])}" cy="${f(nis[1])}" r="${n ? 4.5 : 5}" class="f-warm s-surface" stroke-width="1.6"/>` + `<circle cx="${f(tok[0])}" cy="${f(tok[1])}" r="3" class="f-surface s-ink" stroke-width="1.5"/>`;
  s += txt(pr(n ? [128.3, 50.6] : [120.5, 53.6]), "Siberia", { size: n ? 15 : 17, bold: 1 });
  s += txt(pr(n ? [132.3, 37.3] : [132.6, 37.6]), "Sea of Japan", { size: n ? 13 : 15, bold: 1, anchor: "middle" });
  s += txt(pr([143.7, 43.7]), "Hokkaido", { size: n ? 12.5 : 14, bold: 1, anchor: "middle", dy: 4 });
  s += txt(nis, "Niseko", { dx: n ? 2 : 4, dy: n ? 19 : 21, size: n ? 12.5 : 13, bold: 1 });
  s += txt(tok, "Tokyo", { dx: 8, dy: 4, muted: 1, size: 12 });
  s += txt(pr(n ? [145.6, 37.8] : [146.5, 36.5]), n ? "Pacific" : "Pacific Ocean", { muted: 1, anchor: "middle", size: 12 });
  if (!n) s += txt(pr([121.5, 40.6]), "China", { muted: 1 }) + txt(pr([127.6, 36.6]), "Korea", { muted: 1, size: 12, anchor: "middle" });
  s += badge(pr(n ? [131.6, 48.4] : [127.2, 50.4]), 1) + badge(pr([134.6, 40.9]), 2);
  const b3 = pr(n ? [143.6, 40.6] : [144.2, 40.3]), t3 = pr([140.25, 40.6]);
  s += line(t3, [b3[0] - 12, b3[1]], "s-ink", 1.4) + badge(b3, 3);
  return s + "</svg>";
});

// B. The same machine from the side.
out.side = both((n) => {
  const W = n ? 340 : 720, H = n ? 236 : 300, k = W / 720, r = n ? 0.62 : 1, id = n ? "mSn" : "mSw";
  const X = (x) => f(x * k), Y = (y) => f(n ? y * 0.78 + 4 : y);
  const sea0 = n ? 150 * k + 14 : 150; // a little more land on the left for the label
  let s = open(W, H, n ? "narrow" : "wide", "Cold dry wind from Siberia crosses the warm Sea of Japan, picks up moisture, forms clouds and drops snow on Hokkaido's mountains.", head(id, "f-cold") + head(id + "w", "f-warm"));
  s += `<rect x="0" y="${Y(232)}" width="${f(sea0)}" height="${H}" class="f-land"/><rect x="${f(sea0)}" y="${Y(244)}" width="${f(X(510) - sea0 + 1)}" height="${H}" class="f-sea"/>`;
  s += `<path d="M${X(510)} ${H}L${X(510)} ${Y(244)}L${X(560)} ${Y(200)}L${X(600)} ${Y(150)}L${X(628)} ${Y(118)}L${X(660)} ${Y(170)}L${X(700)} ${Y(214)}L${X(720)} ${Y(226)}L${X(720)} ${H}z" class="f-land"/>`;
  s += `<path d="M${X(582)} ${Y(172)}L${X(600)} ${Y(150)}L${X(628)} ${Y(118)}L${X(650)} ${Y(154)}L${X(634)} ${Y(160)}L${X(622)} ${Y(148)}L${X(606)} ${Y(168)}L${X(596)} ${Y(160)}z" class="f-cloud s-muted" stroke-width="1"/>`;
  for (const [x0, x1, y] of [[30, 190, 150], [30, 170, 190], [250, 400, 150]]) s += line([+X(x0), +Y(y)], [+X(x1), +Y(y)], "s-cold", n ? 4 : 5, `marker-end="url(#${id})"`);
  for (const x of [230, 310, 390]) { const d = n ? 8 : 12; s += `<path d="M${X(x)} ${Y(238)}q${f(d * 0.66)} ${f(-d * 1.1)} 0 ${f(-d * 2.1)}q${f(-d * 0.66)} ${-d} 0 ${-d * 2}" class="s-warm nofill" stroke-width="${n ? 2 : 2.5}" stroke-linecap="round" marker-end="url(#${id}w)"/>`; }
  s += `<g class="f-neutral">` + [[330, 112, 14], [350, 106, 17], [370, 114, 13], [440, 92, 20], [466, 82, 25], [494, 92, 20], [548, 70, 26], [580, 58, 32], [616, 70, 26], [584, 80, 26]].map(([x, y, q]) => `<circle cx="${X(x)}" cy="${Y(y)}" r="${f(q * r)}"/>`).join("") + `</g>`;
  s += `<g class="f-cold">` + [[552, 116], [568, 134], [584, 112], [596, 132], [560, 156], [578, 152], [610, 110], [544, 176], [540, 140]].map(([x, y]) => `<circle cx="${X(x)}" cy="${Y(y)}" r="${n ? 2.4 : 3}"/>`).join("") + `</g>`;
  const ty = n ? H - 26 : 262;
  s += txt([n ? 6 : 16, ty], "Siberia", { size: n ? 13 : 15, bold: 1, plain: 1 }) + txt([n ? 6 : 16, ty + (n ? 15 : 19)], n ? "frozen, dry" : "frozen and dry", { size: n ? 11.5 : 13, muted: 1, plain: 1 });
  s += txt([(sea0 + +X(510)) / 2, ty + (n ? 8 : 14)], "Sea of Japan", { size: n ? 13 : 15, bold: 1, anchor: "middle", plain: 1 }) + txt([(sea0 + +X(510)) / 2, ty + (n ? 22 : 31)], n ? "warmer than the air" : "much warmer than the air", { size: n ? 11.5 : 13, muted: 1, anchor: "middle", plain: 1 });
  s += txt([W - (n ? 6 : 14), ty + (n ? 8 : 0)], "Hokkaido", { size: n ? 13 : 15, bold: 1, anchor: "end", plain: 1 });
  s += badge([+X(110), +Y(150) - (n ? 22 : 26)], 1) + badge([+X(310), +Y(238) - (n ? 44 : 62)], 2) + badge([+X(672), +Y(74)], 3);
  return s + "</svg>";
});

// C. Pacific: where El Nino sits and what it does near Japan.
out.pacific = both((n) => {
  const W = n ? 340 : 720, H = n ? 190 : 362, id = n ? "mPn" : "mPw", z = n ? 0.6 : 1;
  const pr = geoEquirectangular().rotate([-170, 0]);
  pr.fitExtent([[0, 0], [W, H]], { type: "MultiPoint", coordinates: [[105, -30], [105, 62], [-72, -30], [-72, 62]] }).clipExtent([[0, 0], [W, H]]);
  const path = geoPath(pr).digits(1);
  let s = open(W, H, n ? "narrow" : "wide", "Map of the Pacific Ocean. A tongue of unusually warm water lies along the equator off South America. It shifts the pressure pattern over the North Pacific and weakens the winter wind over Japan.", head(id, "f-cold") + head(id + "i", "f-ink"));
  s += `<rect width="${W}" height="${H}" class="f-sea"/>`;
  const tongue = (lw, le, lat, op) => { const t = pr([lw, 0]), a = pr([le, lat]), b = pr([le, -lat]), m = (t[0] + a[0]) / 2; return `<path d="M${f(t[0])} ${f(t[1])}Q${f(m)} ${f(a[1])} ${f(a[0])} ${f(a[1])}L${f(b[0])} ${f(b[1])}Q${f(m)} ${f(b[1])} ${f(t[0])} ${f(t[1])}z" class="f-warm" opacity="${op}"/>`; };
  s += tongue(175, -76, 9, 0.28) + tongue(-165, -76, 6.5, 0.45) + tongue(-140, -76, 4.5, 0.9);
  const e0 = pr([105, 0]);
  s += `<path d="${path(land110)}" class="f-land s-coast" stroke-width=".5"/><line x1="0" x2="${W}" y1="${f(e0[1])}" y2="${f(e0[1])}" class="s-muted" stroke-width="1" stroke-dasharray="3 5"/>`;
  const a0 = pr([-135, 9]), a1 = pr([-170, 40]), ac = pr([-128, 36]);
  s += `<path d="M${f(a0[0])} ${f(a0[1])}Q${f(ac[0])} ${f(ac[1])} ${f(a1[0])} ${f(a1[1])}" class="s-ink nofill" stroke-width="${n ? 1.5 : 1.8}" stroke-dasharray="5 5" marker-end="url(#${id}i)"/>`;
  const lo = pr([172, 48]); s += `<circle cx="${f(lo[0])}" cy="${f(lo[1])}" r="${f(26 * z)}" class="nofill s-ink" stroke-width="1.5" stroke-dasharray="4 4"/>`;
  s += line(pr([114, 52]), pr([131, 41.5]), "s-cold", n ? 2.5 : 3.5, `stroke-dasharray="${n ? "5 5" : "8 7"}" marker-end="url(#${id})"`);
  const jp = pr([138, 36.5]); s += `<circle cx="${f(jp[0])}" cy="${f(jp[1])}" r="${f(12 * z)}" class="nofill s-ink" stroke-width="1.8"/>`;
  s += txt(jp, "Japan", { dx: n ? 10 : 16, dy: n ? 13 : 5, size: n ? 12.5 : 14, bold: 1 });
  s += txt(pr([-105, 45]), "North America", { muted: 1, anchor: "middle", size: n ? 11 : 13 }) + txt(pr([134, -24]), "Australia", { muted: 1, anchor: "middle", size: n ? 11 : 13 }) + txt(pr([-178, 14]), "Pacific Ocean", { muted: 1, anchor: "middle", size: n ? 11 : 13 });
  if (!n) s += txt(pr([107, 2.5]), "the equator", { muted: 1, size: 12 }) + txt(pr([112, 32]), "China", { muted: 1, anchor: "middle" });
  s += badge(pr([-112, n ? -13 : -10]), 1) + badge(pr([-131, 30]), 2) + badge([lo[0], lo[1]], 3) + badge(pr([n ? 118 : 116, n ? 40 : 44]), 4);
  return s + "</svg>";
});

// D. The warm sea: early December against mid January.
out.sea = both((n) => {
  const W = n ? 340 : 720, H = n ? 496 : 240, dx = n ? 0 : 380, dy = n ? 256 : 0;
  let s = open(W, H, n ? "narrow" : "wide", "In early winter a warm sea raises the snow line so the base gets rain. In mid winter the air is cold enough that the same warm sea means heavier snow from top to bottom.");
  s += txt([0, 18], "Early December: snow up high, rain low down", { size: n ? 14.5 : 15, bold: 1, plain: 1 });
  s += `<path d="M20 220L150 70L190 110L230 60L330 220z" class="f-land"/><path d="M118 107L150 70L190 110L230 60L262 110z" class="f-cloud s-muted"/>`;
  s += `<line x1="10" y1="140" x2="336" y2="140" class="s-warm" stroke-width="2" stroke-dasharray="6 5"/>` + txt([336, 133], "snow line", { size: 13, bold: 1, anchor: "end" });
  s += `<g class="f-cold">` + [[60, 60], [90, 90], [120, 50], [280, 70], [300, 110], [40, 110]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3"/>`).join("") + `</g>`;
  s += `<g class="s-warm" stroke-width="2" stroke-linecap="round">` + [[40, 160], [70, 170], [300, 160], [324, 176], [52, 190]].map(([x, y]) => `<path d="M${x} ${y}l-5 14"/>`).join("") + `</g>`;
  s += txt([20, 237], "thin, wet cover where the lifts start", { size: 13, muted: 1, plain: 1 });
  s += `<g transform="translate(${dx} ${dy})">` + txt([n ? 0 : 20, 18], "Mid January: cold enough everywhere", { size: n ? 14.5 : 15, bold: 1, plain: 1 });
  s += `<path d="M20 220L150 70L190 110L230 60L330 220z" class="f-cloud s-muted"/>`;
  s += `<g class="f-cold">` + [[40, 60], [70, 90], [100, 50], [280, 70], [300, 110], [30, 110], [50, 150], [310, 160], [260, 40], [180, 44], [320, 60], [24, 180], [130, 36]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3.5"/>`).join("") + `</g>`;
  s += txt([20, 237], "the extra moisture falls as deeper powder", { size: 13, muted: 1, plain: 1 }) + `</g>`;
  return s + "</svg>";
});

// E. The Arctic from above: tight ring and buckled ring.
out.arctic = both((n) => {
  const R = n ? 150 : 158, W = n ? 340 : 720, H = n ? 716 : 372;
  let s = open(W, H, n ? "narrow" : "wide", "Two views of the Arctic from above. In the first a tight ring of wind keeps the cold air over the pole. In the second the ring has buckled and a lobe of cold air reaches Japan.");
  const globe = (cx, cy, title, wob) => {
    const mk = (c) => geoOrthographic().rotate([0, -90, c]).translate([cx, cy]).scale(R / Math.sin(64 * Math.PI / 180)).clipAngle(64);
    let pr = mk(0), best = 1e9; // turn the globe until Japan is at the bottom
    for (let c = 0; c < 360; c += 1) { const t = mk(c), j = t([138, 37]); if (j[1] > cy && Math.abs(j[0] - cx) < best) { best = Math.abs(j[0] - cx); pr = t; } }
    const path = geoPath(pr).digits(1);
    let o = txt([cx, cy - R - 12], title, { size: 15, bold: 1, anchor: "middle", plain: 1 });
    o += `<circle cx="${cx}" cy="${cy}" r="${R}" class="f-sea"/><path d="${path(land110)}" class="f-land s-coast" stroke-width=".5"/>`;
    const d = (a, b) => { const x = Math.abs(a - b) % 360; return x > 180 ? 360 - x : x; };
    const pts = [];
    for (let lon = -180; lon < 180; lon += 4) {
      const q = wob ? 23 + 20 * Math.exp(-Math.pow(d(lon, 136) / 24, 2)) + 11 * Math.exp(-Math.pow(d(lon, 25) / 26, 2)) - 7 * Math.exp(-Math.pow(d(lon, -60) / 40, 2)) - 5 * Math.exp(-Math.pow(d(lon, 85) / 22, 2)) : 23;
      pts.push(pr([lon, 90 - q]));
    }
    o += `<path d="M${pts.map((p) => f(p[0]) + " " + f(p[1])).join("L")}z" class="f-cold s-cold" fill-opacity=".28" stroke-width="4.5" stroke-linejoin="round"${wob ? ' stroke-dasharray="10 6"' : ""}/>`;
    o += `<circle cx="${cx}" cy="${cy}" r="${R}" class="nofill s-coast" stroke-width="1"/>`;
    const np = pr([0, 90]), jp = pr([138, 36.5]);
    o += txt(np, "Arctic cold", { size: 13, bold: 1, anchor: "middle", dy: 4 });
    o += `<circle cx="${f(jp[0])}" cy="${f(jp[1])}" r="9" class="nofill s-ink" stroke-width="1.8"/>` + txt(jp, "Japan", { dx: 14, dy: 5, bold: 1 });
    o += txt(pr([100, 58]), "Siberia", { muted: 1, anchor: "middle", size: 12 }) + txt(pr([-100, 50]), "North America", { muted: 1, anchor: "middle", size: 12 }) + txt(pr([15, 49]), "Europe", { muted: 1, anchor: "middle", size: 12 });
    if (wob) o += txt(pr([150, 52]), "a cold burst", { dx: n ? 30 : 40, dy: -6, size: 13, bold: 1 });
    return o;
  };
  s += n ? globe(170, 186, "Tight ring: cold locked in", false) + globe(170, 546, "Buckled ring: cold spills south", true)
    : globe(180, 204, "Tight ring: cold locked in", false) + globe(540, 204, "Buckled ring: cold spills south", true);
  return s + "</svg>";
});

// F. Hokkaido: where the snow lands.
out.hokkaido = both((n) => {
  const W = n ? 340 : 720, H = n ? 300 : 440, id = n ? "mHn" : "mHw";
  const pr = geoMercator().fitExtent([[0, 0], [W, H]], n ? box(138.7, 41.3, 145.9, 45.75) : box(138.0, 41.25, 148.2, 45.75)).clipExtent([[-2, -2], [W + 2, H + 2]]);
  const path = geoPath(pr).digits(1);
  // Keep only the islands near Hokkaido: clipping the mainland polygon fills the whole frame.
  const near = { type: "MultiPolygon", coordinates: land10.features[0].geometry.coordinates.filter((poly) => { const xs = poly[0].map((c) => c[0]), ys = poly[0].map((c) => c[1]); const x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys); return x1 > 137 && x0 < 149 && y1 > 40.5 && y0 < 46.5 && x1 - x0 < 30; }) };
  let s = open(W, H, n ? "narrow" : "wide", "Map of Hokkaido. Wind from the north-west crosses the Sea of Japan and hits the west side first, where Niseko, Rusutsu and Kiroro are. Furano, Tomamu and Asahidake sit in colder, drier central Hokkaido.", head(id, "f-cold"));
  s += `<rect width="${W}" height="${H}" class="f-sea"/><path d="${path(near)}" class="f-land s-coast" stroke-width=".7"/>`;
  const arrows = n ? [[[138.85, 44.15], [139.95, 43.45]], [[139.5, 45.35], [141.0, 44.6]], [[138.8, 43.05], [139.75, 42.6]]] : [[[138.3, 44.2], [139.7, 43.3]], [[138.9, 45.3], [141.0, 44.5]], [[138.2, 43.1], [139.6, 42.5]]];
  for (const [a, b] of arrows) s += line(pr(a), pr(b), "s-cold", n ? 4.5 : 5, `marker-end="url(#${id})"`);
  const z = n ? 13 : 14;
  const west = [["Niseko", 140.69, 42.86, { dx: -10, dy: 5, anchor: "end" }], ["Rusutsu", 140.9, 42.75, { dx: n ? -2 : 4, dy: n ? 21 : 20, anchor: n ? "middle" : "start" }], ["Kiroro", 140.98, 43.07, { dx: -4, dy: -11, anchor: "end" }]];
  const mid = [["Furano", 142.38, 43.33, { dx: 10, dy: 5 }], ["Tomamu", 142.63, 43.06, { dx: 10, dy: 12 }], ["Asahidake", 142.85, 43.66, { dx: 10, dy: 2 }]];
  for (const [name, x, y, o] of west) { const p = pr([x, y]); s += `<circle cx="${f(p[0])}" cy="${f(p[1])}" r="${n ? 5.5 : 6.5}" class="f-cold s-surface" stroke-width="2"/>` + txt(p, name, { ...o, bold: 1, size: z }); }
  for (const [name, x, y, o] of mid) { const p = pr([x, y]), q = n ? 6 : 7; s += `<path d="M${f(p[0])} ${f(p[1] - q)}L${f(p[0] + q)} ${f(p[1] + q * 0.8)}L${f(p[0] - q)} ${f(p[1] + q * 0.8)}z" class="f-ink s-surface" stroke-width="2"/>` + txt(p, name, { ...o, bold: 1, size: z }); }
  const sap = pr([141.35, 43.06]); s += `<rect x="${f(sap[0] - 3.5)}" y="${f(sap[1] - 3.5)}" width="7" height="7" class="f-surface s-ink" stroke-width="1.5"/>` + txt(sap, "Sapporo", { dx: n ? 2 : 9, dy: n ? -8 : -5, muted: 1, size: 12 });
  if (!n) { const cts = pr([141.69, 42.78]); s += `<rect x="${f(cts[0] - 3)}" y="${f(cts[1] - 3)}" width="6" height="6" class="f-surface s-ink" stroke-width="1.4"/>` + txt(cts, "airport", { dx: 8, dy: 12, muted: 1, size: 12 }); }
  s += txt(pr(n ? [139.75, 41.65] : [139.0, 41.75]), "Sea of Japan", { size: n ? 12.5 : 15, bold: 1, anchor: "middle" });
  s += txt(pr(n ? [144.6, 45.2] : [146.6, 44.7]), "Sea of Okhotsk", { muted: 1, anchor: "middle", size: 12 });
  s += txt(pr(n ? [138.8, 45.5] : [138.15, 45.5]), "winter wind", { size: 13, bold: 1 });
  return s + "</svg>";
});
process.stdout.write(JSON.stringify(out));
