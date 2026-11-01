# Carte de la conjugaison

Carte mentale interactive pour réviser la conjugaison française au CRPE. Elle compte 98 fiches réparties en sept branches : identifier le verbe, construire la forme, modes et temps, personne et nombre, voix, valeurs et aspect, orthographe et pièges. Chaque fiche donne la définition, la formation, des exemples et sa source.

La page comprend aussi une recherche, des filtres, un tableau triable des 19 temps et les formes de six verbes modèles. Une version imprimable est disponible : [carte-conjugaison.pdf](carte-conjugaison.pdf).

## Sources

Les règles viennent en priorité d'Éduscol et du ministère de l'Éducation nationale, puis de l'Office québécois de la langue française et de l'Académie française. Le Conjugueur (Le Figaro), source privée, ne sert qu'aux tableaux de formes. Quand une notion n'a pas de source officielle, la fiche le signale.

## Assembler la page

```bash
python3 scripts/assembler.py
```

Le script contrôle les parents, les liens, les sources et les formes, puis écrit `index.html` à partir de `src/page.html` et de `donnees/`.

Site : https://laetitiaperez.github.io/conjugaison/
