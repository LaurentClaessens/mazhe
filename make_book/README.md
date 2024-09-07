Il faut laisser les labels dans la version imprimée, sinon les gens m'envoient des corrections
avec les numéros.


- Créer la nouvelle entrée dans `isbn.json`.

```
cd testing
./testing.sh
./compile_part.py lst_lefrido.json
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
```

Faire les fichiers
```
    cd make_book
    ./split_book.py 2024
```

- Vérification dans `make_book/output`
- Le faire assez de fois pour que la coupure ne soit pas au milieu d'un chapitre.

- Vérification du nombre de pages. Le max est 900.

```
git tag 2024
git commit -a
git push origin 2024
```

## Avant de proposer dans thebookedition.com

Avant de supprimer l'ancienne version, noter les stats de la précédente : ventes et prix.

## Proposer dans thebookedition.com



Titre : 
- Le Frido 2023 -- volume 1
- Le Frido 2023 -- volume 2
- Le Frido 2023 -- volume 3
- Le Frido 2023 -- volume 4

Auteur :
Laurent Claessens

Catégorie : scolaire -> études supérieures


## Résumé

Le Frido est un cours de mathématique libre et contributif recouvrant (presque) l'ensemble de la matière du niveau de l'agrégation de mathématiques. Les démonstrations sont très détaillées; rien n'est considéré comme évident.

Comme point de départ, l'existence de l'ensemble des naturels est supposée. Ensuite tout est construit avec les démonstrations : groupes, corps, analyse réelle, espaces topologiques, probabilités et bien d'autres.

Téléchargement du pdf, des sources LaTeX et de la version en préparation de l'année prochaine :
https://laurent.claessens-donadello.eu/frido.html

Gardez un oeil sur erratum :
https://github.com/LaurentClaessens/mazhe/blob/master/erratum.md

## les mots-clefs

mathématique, agrégation, master


À la fin, copier ce fichier vers `readmes/README_2024.md`
