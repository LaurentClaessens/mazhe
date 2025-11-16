Repasser les showlabels à tiny au lieu de small.

- remplacer 2025 par 2026 partout dans ce fichier.
- Créer la nouvelle entrée dans `isbn.json`.


## Couverture

- Voir si il y a une image de nouvelle année sur pepper et carot
La dernière ici est chouette : https://www.peppercarrot.com/fr/webcomic/ep39_The-Tavern.html

## Tester


```
    cd testing
    ./testing.sh
```

Puis dans le répertoire normal:
```
    ./compile_part.py lst_lefrido.json     
-- attendre la fin
    ./compile_part.py lst_book.json
```

Note : le fichier `0-book.pdf` commence direct par l'index thématique. C'est normal.


Faire du large:
```
    cd make_book
    rm *.log
    rm *.pdf
    rm *.aux
    rm first_5*
    rm output/*.pdf
```

Faire les fichiers
```
    cd make_book
    ./split_book.py 2025
```

- Vérification dans `make_book/output`
- Le faire assez de fois pour que la coupure ne soit pas au milieu d'un chapitre.

- Vérification du nombre de pages. Le max est 900.
- Vérification que les labels sont bien écrits

```
git tag 2025
git commit -a
git push origin 2025
```

## Copier les fichiers bouquin vers mon ftp


## Avant de proposer dans thebookedition.com

Avant de supprimer l'ancienne version, noter les stats de la précédente : ventes et prix.

## Proposer dans thebookedition.com

Choisir des images de couvertures. 
Pour 2025 j'ai oublié de mettre celle-ci :
https://www.davidrevoy.com/data/images/blog/2025/2025-01-03_new-year-illustration_by-david-revoy.jpg
Ce serait bien de trouver celle de 2026.


- Désactiver uMatrix

Les choix à faire :
papier
dos carré collé
A4
sensation tactile
noir et blanc
vente : oui


Titre : 
- Le Frido 2025 -- volume 1
- Le Frido 2025 -- volume 2
- Le Frido 2025 -- volume 3
- Le Frido 2025 -- volume 4

Auteur :
Laurent Claessens

Catégorie : scolaire -> études supérieures


## Résumé

Le Frido est un cours de mathématique libre et contributif recouvrant (presque) l'ensemble de la matière du niveau de l'agrégation de mathématiques. Les démonstrations sont très détaillées; rien n'est considéré comme évident.

Comme point de départ, l'existence de l'ensemble des naturels est supposée. Ensuite tout est construit avec les démonstrations : groupes, corps, analyse réelle, espaces topologiques, probabilités et bien d'autres.

Téléchargement du pdf, des sources LaTeX et dernières mises à jour : 
https://laurent.claessens-donadello.eu/frido.html

Gardez un oeil sur erratum :
https://github.com/LaurentClaessens/mazhe/blob/master/erratum.md

Une nouvelle version tous les mois de septembre.

## les mots-clefs

mathématique, agrégation, master



## Mettre à jour sur mon site


## Quand tout est fini


Copier ce fichier vers `readmes/README_2025.md`
