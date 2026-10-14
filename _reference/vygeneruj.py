"""Vygeneruje sekci referencí do stránek podle _reference/reference.json.

Přepisuje jen obsah mezi značkami <!-- REFERENCE:START --> a <!-- REFERENCE:END -->.
Spuštění z kořene repa: python3 _reference/vygeneruj.py
"""
import json
from html import escape
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
DATA = json.loads((KOREN / "_reference" / "reference.json").read_text(encoding="utf-8"))
START, END = "<!-- REFERENCE:START -->", "<!-- REFERENCE:END -->"


def popis(r, s_rokem=True):
    casti = [r["typ"], r["misto"]] + ([r["rok"]] if s_rokem else [])
    return " · ".join(c for c in casti if c)


def karta(r):
    sirka, vyska = r["obrazek_rozmer"]
    novinka = '<span class="ref-new">Novinka</span> ' if r.get("novinka") else ""
    stitky = "".join(f"<li>{escape(s)}</li>" for s in r["stitky"])
    return f"""
      <article class="ref-card">
        <a class="ref-shot" href="{escape(r['url'])}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">
          <img loading="lazy" decoding="async" src="{escape(r['obrazek'])}" width="{sirka}" height="{vyska}" alt="{escape(r['nazev'])} — realizace, tvorba webových stránek">
        </a>
        <div class="ref-body">
          <p class="ref-meta">{novinka}{escape(popis(r))}</p>
          <h3 class="ref-title">{escape(r['nazev'])}</h3>
          <dl class="ref-facts">
            <div><dt>Zadání</dt><dd>{escape(r['zadani'])}</dd></div>
            <div class="ref-result"><dt>Výsledek</dt><dd>{escape(r['vysledek'])}</dd></div>
          </dl>
          <ul class="ref-tags">{stitky}</ul>
          <a class="ref-link" href="{escape(r['url'])}" target="_blank" rel="noopener">Prohlédnout web ↗</a>
        </div>
      </article>"""


def radek(r):
    return f"""
        <li><a class="ref-row" href="{escape(r['url'])}" target="_blank" rel="noopener">
          <span class="ref-row-name">{escape(r['nazev'])}</span>
          <span class="ref-row-type">{escape(popis(r, s_rokem=False))}</span>
          <span class="ref-row-kpi">{escape(r['vysledek_kratce'])}</span>
          <span class="ref-row-year">{escape(r['rok'] or '')}</span>
          <span class="ref-row-arrow" aria-hidden="true">↗</span>
        </a></li>"""


def pocet(n):
    return f"{n} zakázka" if n == 1 else f"{n} zakázky" if n < 5 else f"{n} zakázek"


def sekce(stranka):
    podle_id = {r["id"]: r for r in DATA["reference"]}
    vyber = [podle_id[i] for i in DATA["vyber"][stranka]]
    ostatni = [r for r in DATA["reference"] if r["id"] not in DATA["vyber"][stranka]]
    html = '<div class="ref-grid">' + "".join(karta(r) for r in vyber) + "\n    </div>"
    if ostatni:
        html += f"""
    <div class="ref-all">
      <div class="ref-all-head"><h3>Další realizace</h3><span>celkem {pocet(len(DATA['reference']))}</span></div>
      <ul class="ref-list">{''.join(radek(r) for r in ostatni)}
      </ul>
    </div>"""
    return f"{START}\n    {html}\n    {END}"


for stranka in DATA["vyber"]:
    soubor = KOREN / stranka / "index.html"
    text = soubor.read_text(encoding="utf-8")
    a, b = text.index(START), text.index(END) + len(END)
    soubor.write_text(text[:a] + sekce(stranka) + text[b:], encoding="utf-8")
    print("aktualizováno:", soubor.relative_to(KOREN))
