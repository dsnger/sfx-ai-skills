#!/usr/bin/env python3
"""Checks German copy (HTML or Markdown) for mechanically detectable rule breaks.

Usage: python3 check_sentences.py <file> [--max 15] [--things "Word1|Word2"]
       python3 check_sentences.py --selftest
Finds: sentences over the word limit, things as sentence subject (heuristic),
"nicht ... sondern", dashes used as a stylistic device, short punchline sentences,
"Darum/Deshalb/Daher" right after a question.
Heuristic: hits are hints to review, not verdicts. No hits does not mean compliant.
Add project-specific nouns (product names, systems) with --things.
"""
import html, re, sys

THINGS = ("Website|Webseite|Seite|Seiten|Termin|Termine|Preis|Preise|Kosten|Regel|Regeln|Liste|"
          "System|Software|Tool|App|Plattform|Angebot|Paket|Daten|Angaben|Vertrag|Buchung|Google|KI|Technik|"
          "Produkt|Lösung|Service|Funktion|Formular|Datei|Dateien|Dokument|Dokumente")
STATE = (r"(ist|sind|steht|stehen|liegt|liegen|gilt|gelten|bucht|buchen|zeigt|zeigen|kostet|bestimmt|bestimmen|"
         r"bietet|bieten|sorgt|sorgen|bringt|bringen|hilft|helfen|macht|machen|übernimmt|übernehmen|erledigt|erledigen)")
RE_SONDERN = re.compile(r"\bnicht\b[^.?!]{0,60}\bsondern\b", re.I)
RE_DASH = re.compile(r"\s[–—]\s")

def build_thing_re(extra=""):
    things = THINGS + ("|" + extra if extra else "")
    return re.compile(rf"(?:^|[.?!]\s+|,\s*|\b(?i:die|der|das|ihre|ihr|unsere|unser|jede|jeder)\s+)({things})\s+{STATE}\b")

def text_from(raw):
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    raw = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<(br|/p|/h[1-6]|/li|/summary|/div)[^>]*>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(raw)

def sentences(text):
    for line in text.split("\n"):
        line = line.strip(" #-*\t")
        if not line:
            continue
        for s in re.split(r"(?<=[.?!])\s+(?=[A-ZÄÖÜ„])", line):
            if s.strip():
                yield s.strip()

def check(text, maxw=15, extra=""):
    re_thing = build_thing_re(extra)
    hits, prev = [], ""
    for s in sentences(text):
        w = len(s.split())
        if w > maxw:
            hits.append(("long", f"{w} words", s))
        if re_thing.search(s):
            hits.append(("thing-subject", "Who acts?", s))
        if RE_SONDERN.search(s):
            hits.append(("not-but", "", s))
        if RE_DASH.search(s):
            hits.append(("dash", "", s))
        if s.endswith(".") and 1 < w <= 3 and not re.match(r"^\d", s):
            hits.append(("punchline", "short sentence", s))
        if prev.endswith("?") and re.match(r"^(Darum|Deshalb|Daher)\b", s):
            hits.append(("reference", "'Darum' after a question", s))
        prev = s
    return hits

def selftest():
    t = ("Die Website zeigt alle Termine. Ihre Kunden buchen direkt auf der Seite. "
         "Das ist nicht teuer, sondern fair. Bei uns nicht. "
         "Müssen Interessenten lange suchen? Darum legen wir Seiten an. "
         "Dies ist ein sehr langer Satz mit deutlich mehr als fünfzehn Wörtern, damit die Längenprüfung sicher anschlägt.")
    kinds = [h[0] for h in check(t)]
    for expected in ("thing-subject", "not-but", "punchline", "reference", "long"):
        assert expected in kinds, (expected, kinds)
    assert not check("Ihre Kunden buchen direkt auf jeder Seite."), "false alarm with people as subject"
    assert check("Das Dashboard zeigt alles.", extra="Dashboard"), "extra things not applied"
    print("Selftest ok")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit(0)
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    maxw = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 15
    extra = sys.argv[sys.argv.index("--things") + 1] if "--things" in sys.argv else ""
    hits = check(text_from(open(sys.argv[1], encoding="utf-8").read()), maxw, extra)
    for kind, info, s in hits:
        print(f"[{kind}] {info}: {s}")
    print(f"{len(hits)} hints")
    sys.exit(1 if hits else 0)
