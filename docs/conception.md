# Carte de la conjugaison française — conception et plan

Date : 1er novembre 2026.

## Intention

Laetitia prépare le CRPE. Elle veut une carte mentale qui lui permette de naviguer dans toutes
les caractéristiques des verbes et de leur conjugaison, pour classer et organiser ses révisions.
Le contenu s'appuie sur des sources officielles, et chaque fiche indique la sienne.

## Ce qui a été validé

- Une carte centrée sur « Le verbe », à sept branches : identifier le verbe, construire la forme,
  modes et temps, personne et nombre, voix, valeurs et aspect, orthographe et pièges.
- Un clic sur une notion ouvre une fiche : définition, formation, exemples, source.
- Recherche, liens entre les fiches, filtres pour classer, version imprimable.
- Une page web publique, sur GitHub Pages. Pas de suivi « acquis / à revoir » dans cette version.

## Sources, par ordre de priorité

1. Éduscol et ministère : terminologie grammaticale, programmes du cycle 4 (2020 et 2026),
   programme du lycée, fiches d'étude de la langue.
2. Office québécois de la langue française (Vitrine linguistique) et Académie française :
   règles de formation, accords, rectifications de 1990.
3. Le Conjugueur (Le Figaro), source privée : uniquement les tableaux de formes.

Quand une notion n'a pas de source officielle trouvée, la fiche le dit.

## Points relevés pendant la recherche

- Session 2027 : le programme de français porte sur le cycle 4 « en vigueur à la rentrée 2026 ».
  Le nouveau programme (BO n° 10 du 5 mars 2026) s'applique en 5e à la rentrée 2026 ; la 4e et la 3e
  restent sur celui de 2020 cette année-là. La carte couvre les deux.
- Le concours bac+5 ajoute « L'étude de la langue au lycée » : valeurs temporelles, aspectuelles,
  modales et concordance des temps. La carte l'intègre.
- La terminologie officielle classe le conditionnel parmi les temps de l'indicatif. Le Conjugueur
  en fait un mode. La carte suit la terminologie et signale l'écart.

## Plan

1. Extraire les formes des six verbes modèles dans `donnees/formes.json`.
2. Rédiger les fiches dans `donnees/fiches.js`.
3. Écrire la page dans `src/page.html`.
4. Assembler et contrôler avec `scripts/assembler.py` : liens, sources, formes.
5. Vérifier le rendu, publier, produire la version PDF.
