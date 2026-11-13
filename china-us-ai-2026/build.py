"""Build index.html for the China vs US AI post.

Run from this folder: python3 build.py
It reads data.json and page.html (the text, with {{chart:NAME}} markers)
and writes index.html with each chart as a static SVG. No JavaScript.
"""
import html
import json
import pathlib

HERE = pathlib.Path(__file__).parent
DATA = json.loads((HERE / "data.json").read_text())

class L:
    """Layout. wide: label column left of bars. narrow: label above bar."""
    def __init__(self, narrow):
        self.narrow = narrow
        self.W = 360 if narrow else 700
        self.x0 = 0 if narrow else 300          # where bars start
        self.plot_w = self.W - self.x0 - (64 if narrow else 80)
        self.wrapw = 50 if narrow else 44


BAR_H = 22
GAP = 14


def esc(s):
    return html.escape(str(s), quote=True)


def fmt(v):
    return f"{v:,.0f}" if v >= 100 else f"{v:g}"


def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    lines.append(cur)
    return lines


def bar(x, y, w, h, cls):
    """A bar with a 4px rounded data-end, square at the baseline."""
    r = min(4, w / 2, h / 2)
    return (f'<path class="{cls}" d="M{x:.1f},{y:.1f} h{w - r:.1f} '
            f'a{r},{r} 0 0 1 {r},{r} v{h - 2 * r:.1f} a{r},{r} 0 0 1 -{r},{r} '
            f'h-{w - r:.1f} z"/>')


def labels(lay, y, label, note):
    """Write label lines (and an optional note) from y; return text and height."""
    lines = wrap(label, lay.wrapw)
    out = [f'<text class="lab" x="0" y="{y + 14 + 17 * i}">{esc(ln)}</text>' for i, ln in enumerate(lines)]
    if note:
        out.append(f'<text x="0" y="{y + 14 + 17 * len(lines)}">{esc(note)}</text>')
    return out, 17 * (len(lines) + (1 if note else 0))


def series_rows(lay, y, label, note, bars):
    """One row: labels plus one or more bars. bars: (value, max, cls, text, title)."""
    out, lab_h = labels(lay, y, label, note)
    bh = BAR_H if len(bars) == 1 else 16
    block = len(bars) * bh + (len(bars) - 1) * 2
    if lay.narrow:
        by0 = y + lab_h + 4
        row_h = lab_h + 4 + block
    else:
        row_h = max(lab_h, block)
        by0 = y + (row_h - block) / 2
    for j, (v, m, cls, txt, title) in enumerate(bars):
        by = by0 + j * (bh + 2)
        bw = max(2, lay.plot_w * v / m)
        out.append(f'<g>{bar(lay.x0, by, bw, bh, cls)}<title>{esc(title)}</title></g>')
        out.append(f'<text class="val" x="{lay.x0 + bw + 6:.1f}" y="{by + bh / 2 + 5:.1f}">{esc(txt)}</text>')
    return out, row_h, by0


def svg(lay, h, body, title):
    cls = "narrow" if lay.narrow else "wide"
    return (f'<svg class="chart {cls}" viewBox="0 -4 {lay.W} {h + 8}" role="img" aria-label="{esc(title)}">'
            f'{body}</svg>')


def table(head, rows):
    th = "".join(f"<th>{esc(c)}</th>" for c in head)
    tr = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<details><summary>Show the numbers</summary><div class="wrap"><table><tr>{th}</tr>{tr}</table></div></details>'


def simple(lay, rows, max_v, suffix, unit, extra=None):
    """rows: (label, value, note, cls)."""
    out, y, first_bar = [], 0, None
    for label, v, note, cls in rows:
        o, h, by = series_rows(lay, y, label, note, [(v, max_v, cls, f"{fmt(v)}{suffix}", f"{label}: {fmt(v)}{suffix} {unit}")])
        if first_bar is None:
            first_bar = by
        out += o
        y += h + GAP
    if not lay.narrow:
        out.insert(0, f'<line class="zero" x1="{lay.x0}" x2="{lay.x0}" y1="0" y2="{y - GAP}"/>')
    if extra:
        out.append(extra(lay, y - GAP, first_bar))
    return y - GAP, "\n".join(out)


def both(make, title):
    return "".join(svg(lay, *make(lay), title) for lay in (L(False), L(True)))


def chart_lag():
    d = DATA["lag"]
    rows = [(r[0], r[1], r[2], "cn") for r in d["rows"]]

    def whisker(lay, h, by):
        x4, x14 = lay.x0 + lay.plot_w * 4 / 14, lay.x0 + lay.plot_w
        y = by + BAR_H / 2
        return (f'<line class="whisker" x1="{x4:.1f}" x2="{x14:.1f}" y1="{y}" y2="{y}"/>'
                f'<line class="whisker" x1="{x4:.1f}" x2="{x4:.1f}" y1="{y - 4}" y2="{y + 4}"/>'
                f'<line class="whisker" x1="{x14:.1f}" x2="{x14:.1f}" y1="{y - 4}" y2="{y + 4}"/>')

    def make(lay):
        return simple(lay, rows, 14, "", d["unit"])
    return both(make, d["title"]) + table(["Estimate", "Months behind", "Note"], [r[:3] for r in d["rows"]])


def chart_compute():
    d = DATA["compute"]
    rows = [(r[0], r[1], "", "us") for r in d["rows"]]
    return (both(lambda lay: simple(lay, rows, 100, "%", "of new AI compute"), d["title"])
            + table(["Period", "US share of new AI compute"], [(r[0], f"{r[1]}%") for r in d["rows"]]))


def chart_pairs():
    d = DATA["pairs"]

    def make(lay):
        out, y = [], 0
        for label, us, cn, unit, _ in d["rows"]:
            m = max(us, cn)
            o, h, _ = series_rows(lay, y, label, "", [
                (us, m, "us", f"US {fmt(us)}", f"US: {fmt(us)} {unit}"),
                (cn, m, "cn", f"China {fmt(cn)}", f"China: {fmt(cn)} {unit}")])
            out += o
            y += h + 18
        if not lay.narrow:
            out.insert(0, f'<line class="zero" x1="{lay.x0}" x2="{lay.x0}" y1="0" y2="{y - 18}"/>')
        return y - 18, "\n".join(out)
    return both(make, d["title"]) + table(["Measure", "US", "China"], [(r[0], fmt(r[1]), fmt(r[2])) for r in d["rows"]])


def chart_price():
    d = DATA["price"]
    rows = [(r[0], r[1], "", r[2]) for r in d["rows"]]
    return (both(lambda lay: simple(lay, rows, 40, "", "US$ per million output tokens"), d["title"])
            + table(["Model", "US$ per million output tokens"], [(r[0], f"${r[1]}") for r in d["rows"]]))


def chart_distill():
    d = DATA["distill"]
    rows = [(r[0], r[1], "", "cn") for r in d["rows"]]
    return (both(lambda lay: simple(lay, rows, max(r[1] for r in rows), "M", "exchanges"), d["title"])
            + table(["Lab", "Exchanges (million)"], [(r[0], r[1]) for r in d["rows"]]))


CHARTS = {"lag": chart_lag, "compute": chart_compute, "pairs": chart_pairs,
          "price": chart_price, "distill": chart_distill}

page = (HERE / "page.html").read_text()
for name, fn in CHARTS.items():
    page = page.replace("{{chart:%s}}" % name, fn())
assert "{{chart:" not in page, "unknown chart marker"
(HERE / "index.html").write_text(page)
print("wrote index.html", len(page), "bytes")
