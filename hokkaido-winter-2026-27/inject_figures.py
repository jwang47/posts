"""Puts the figures from make_maps.mjs into explainer.html.

    python3 inject_figures.py figures.json

Each figure lives in <div class="fig" data-fig="NAME">. The div holds a wide
and a narrow SVG; the page's CSS shows one of them.
"""
import json
import pathlib
import re
import sys

here = pathlib.Path(__file__).parent
figs = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
page = here / "explainer.html"
s = page.read_text(encoding="utf-8")
for name, svg in figs.items():
    pat = re.compile(r'<div class="fig" data-fig="%s">.*?</div>' % name, re.S)
    assert len(pat.findall(s)) == 1, name
    s = pat.sub(lambda m: '<div class="fig" data-fig="%s">\n%s\n</div>' % (name, svg), s)
page.write_text(s, encoding="utf-8")
print("injected", ", ".join(figs))
