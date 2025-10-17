# Giulietta

(*English*) This is a big course of mathematics declined in two versions. See below for an English presentation of the English part.

(*Français*) Ce dépôt contient les sources d'un livre de mathématique, décliné en deux versions :

## Le Frido (en français)

[« Le Frido »](http://laurent.claessens-donadello.eu/pdf/lefrido.pdf) contient des mathématiques du niveau de l'agrégation. Il couvre (à peu près) tout le programme de 2015.

### Contribuer

Il y a plusieurs façons de contribuer.

- Le lire et m'écrire quand un passage semble obscur, mal justifié voire faux.
- Rédiger un résultat manquant avec sa preuve à la main sur du papier et m'envoyer une photo de votre feuille.

Dans tous les cas, utilisez au maximum le système de labels du Frido pour faire des références. Ne dites pas "le théorème de Dini" ou (pire) "le théorème 12.316". Dites le "ThoUFPLEZh".



## Compilation


```
    git clone https://github.com/LaurentClaessens/mazhe
    cd mazhe
```

### Partie facile


```
    pdflatex mazhe.tex
```
fera déjà une bonne partie du boulot, mais pas la bibliogrpahie.

### Principe général pour la suite

Pour compiler correctement le Frido, il faut lancer un script en python. Pour ne pas avoir à utiliser le python du système (on ne veut pas y faire de `pip install`), on va :

- compiler python 3.10.12 dans `mazhe/.pyenv/versions`
- créer dans `mazhe` un sous-répertoire `venv/bin` qui contiendra un lien vers `~/.pyenv/versions/3.10.12/python3`
- Faire des `pip install` dans `venv/lib`.

De cette façon, on va pouvoir utiliser un python tout propre avec tout ce qu'il nous faut sans toucher au précieux python du système. Il ne faut jamais toucher au python [installé sur votre système](https://xkcd.com/1987/).


### Si vous n'avez pas encore pyenv



```
    sudo apt install  build-essential zlib1g-dev libffi-dev libssl-dev libreadline-dev libsqlite3-dev liblzma-dev libbz2-dev

    ./make_venv.sh
```

### compiler le frido tl;dr  (trop long; donne un résumé)


Pour créer le répertoire `venv` :
```
    ./make_venv.sh
```

Vous pouvez maintenant compiler le Frido et Giulietta
```
    ./compile_part.py lst_lefrido.json
    ./compile_part.py lst_giulietta.json
```

### compiler une partie du frido : tl;dr


- Éditer le fichier `lst_example.json` (en ayant changé son nom parce comme il est suivi par git, il ne faut pas compter dessus).
- Modifier la liste `tex_files` pour contenir la liste des fichiers à compiler.
- Modifier le champ `pdf_title` si vous voulez.
- compiler :
```
    ./compile_part.py lst_example.json
```
