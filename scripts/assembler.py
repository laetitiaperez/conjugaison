"""Assemble la page et contrôle les fiches : parents, liens, sources, formes."""
import json
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
fiches = (RACINE / "donnees/fiches.js").read_text(encoding="utf8")
formes = json.loads((RACINE / "donnees/formes.json").read_text(encoding="utf8"))
page = (RACINE / "src/page.html").read_text(encoding="utf8")

CONTROLE = r"""
const assert = (c, m) => { if (!c) { console.error(m); process.exitCode = 1; } };
const ids = new Set(FICHES.map(f => f.id));
assert(ids.size === FICHES.length, "identifiant en double");
for (const f of FICHES) {
  if (f.p) assert(ids.has(f.p), `parent inconnu : ${f.id} -> ${f.p}`);
  for (const l of f.l || []) assert(ids.has(l), `lien inconnu : ${f.id} -> ${l}`);
  assert(f.s && f.s.length, `sans source : ${f.id}`);
  for (const [k] of f.s || []) assert(SOURCES[k], `source inconnue : ${f.id} -> ${k}`);
  if (f.forme) for (const v of Object.keys(FORMES)) assert(FORMES[v][f.forme], `forme absente : ${f.id} ${v}`);
  if (f.tm) assert(f.tm.length === 5, `classement incomplet : ${f.id}`);
}
for (const [b] of BRANCHES) assert(ids.has(b), `branche inconnue : ${b}`);
const notions = FICHES.length, temps = FICHES.filter(f => f.tm).length;
console.log(`${notions} fiches, ${temps} temps classés, ${Object.keys(SOURCES).length} sources`);
"""
donnees = f"{fiches}\nconst FORMES = {json.dumps(formes, ensure_ascii=False)};\n"
essai = subprocess.run(["node", "-e", donnees + CONTROLE], capture_output=True, text=True)
print(essai.stdout.strip(), essai.stderr.strip())
if essai.returncode:
    sys.exit(1)

sortie = page.replace("/*DONNEES*/", donnees)
(RACINE / "carte-conjugaison.html").write_text(sortie, encoding="utf8")
titre = re.search(r"<title>.*?</title>", sortie).group(0)
site = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{sortie}'
(RACINE / "index.html").write_text(site, encoding="utf8")
print(titre, f"{len(sortie.encode()) // 1024} Ko")
