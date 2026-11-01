"""Extrait les formes de six verbes modèles depuis les pages enregistrées du Conjugueur."""
import html, json, re, sys
from pathlib import Path

entree, sortie = Path(sys.argv[1]), Path(sys.argv[2])
VERBES = ["chanter", "finir", "prendre", "etre", "avoir", "aller"]
MODES = {"ind": "indicatif", "sub": "subjonctif", "cnd": "conditionnel",
         "imp": "imperatif", "par": "participe", "inf": "infinitif", "ger": "gerondif"}

def lignes(bloc):
    bloc = re.sub(r"<br\s*/?>", "\n", bloc)
    bloc = re.sub(r"</(div|p|h\d)>", "\n", bloc)
    bloc = html.unescape(re.sub(r"<[^>]+>", "", bloc)).replace("\xa0", " ")
    return [re.sub(r"\s+", " ", l).strip() for l in bloc.split("\n") if l.strip()]

resultat = {}
for verbe in VERBES:
    t = (entree / f"{verbe}.html").read_text(encoding="utf8", errors="ignore")
    debut = t.find('<body')
    t = t[debut:]
    pos = [(m.start(), m.group(1)) for m in re.finditer(r'<h2 class="modeBloc" id="(\w+)"', t)]
    fin = t.find('<h2 class="modeBloc">R')
    formes = {}
    for i, (p, code) in enumerate(pos):
        if code not in MODES:
            continue
        q = pos[i + 1][0] if i + 1 < len(pos) else fin
        q = min(x for x in (q, fin) if x > p)
        for b in re.split(r'<div class="conjugBloc">', t[p:q])[1:]:
            ls = lignes(b)
            if len(ls) >= 2:
                formes[f"{MODES[code]}:{ls[0]}"] = ls[1:]
    resultat[verbe] = formes
sortie.write_text(json.dumps(resultat, ensure_ascii=False, indent=1), encoding="utf8")
print({v: len(f) for v, f in resultat.items()})
for k, v in resultat["etre"].items():
    print(k, v[:6])
