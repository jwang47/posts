"""Small JMA etrn scraper helpers (stdlib only).

Downloads pages from https://www.data.jma.go.jp/stats/etrn/ with a generic
User-Agent, caches them under raw/, and parses the data tables into rows
keyed by flattened column labels.
"""
import os, re, time, html, hashlib, urllib.request
from html.parser import HTMLParser

BASE = "https://www.data.jma.go.jp/stats/etrn/"
UA = "posts-research (github.com/jwang47/posts)"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "raw")
os.makedirs(CACHE, exist_ok=True)
_last = [0.0]


def fetch(path, force=False):
    url = BASE + path
    fn = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9_.=-]", "_", path)[:180] + ".html")
    if os.path.exists(fn) and not force:
        return open(fn, encoding="utf-8").read()
    for attempt in range(4):
        wait = 0.5 - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                txt = r.read().decode("utf-8", "replace")
            _last[0] = time.time()
            break
        except Exception as e:
            _last[0] = time.time()
            if attempt == 3:
                raise
            time.sleep(2 ** (attempt + 1))
    open(fn, "w", encoding="utf-8").write(txt)
    return txt


class _TP(HTMLParser):
    """Collect tables as lists of rows of (tag, text, rowspan, colspan)."""

    def __init__(self):
        super().__init__()
        self.tables = []  # (attrs, rows)
        self.stack = []
        self.cell = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table":
            self.stack.append((a, []))
        elif not self.stack:
            return
        elif tag == "tr":
            self.stack[-1][1].append([])
        elif tag in ("td", "th"):
            self.cell = [tag, "", int(a.get("rowspan", 1) or 1), int(a.get("colspan", 1) or 1)]
        elif tag == "br" and self.cell is not None:
            self.cell[1] += ""

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None and self.stack:
            if self.stack[-1][1]:
                self.stack[-1][1][-1].append(tuple(self.cell))
            self.cell = None
        elif tag == "table" and self.stack:
            self.tables.append(self.stack.pop())

    def handle_data(self, d):
        if self.cell is not None:
            self.cell[1] += d


def parse_table(txt, table_id="tablefix1"):
    """Return (labels, datarows). labels are '/'-joined header paths."""
    p = _TP()
    p.feed(txt)
    tab = None
    for a, rows in p.tables:
        if a.get("id") == table_id:
            tab = rows
            break
    if tab is None:
        return None, []
    # build grid
    grid = {}
    nrows = len(tab)
    for r, row in enumerate(tab):
        c = 0
        for tag, text, rs, cs in row:
            while (r, c) in grid:
                c += 1
            for dr in range(rs):
                for dc in range(cs):
                    grid[(r + dr, c + dc)] = (tag, text.strip())
            c += cs
    ncols = max(c for (_, c) in grid) + 1
    hdr_rows = [r for r in range(nrows) if all(grid.get((r, c), ("th",))[0] == "th" for c in range(ncols))]
    nh = 0
    while nh in hdr_rows:
        nh += 1
    labels = []
    for c in range(ncols):
        parts = []
        for r in range(nh):
            t = grid.get((r, c), ("th", ""))[1]
            if t and (not parts or parts[-1] != t):
                parts.append(t)
        labels.append("/".join(parts))
    data = []
    for r in range(nh, nrows):
        data.append([grid.get((r, c), ("td", ""))[1] for c in range(ncols)])
    return labels, data


def clean(v):
    """Return (number-or-None, flagged). ']' => flagged; ')' stripped."""
    if v is None:
        return None, False
    v = html.unescape(v).strip().replace("　", "").replace(" ", "")
    flagged = "]" in v
    v = v.replace(")", "").replace("]", "").replace("#", "").replace("*", "")
    if v in ("", "--", "///", "×", "-", "－"):
        return None, flagged
    try:
        f = float(v)
    except ValueError:
        return None, flagged
    return v, flagged
