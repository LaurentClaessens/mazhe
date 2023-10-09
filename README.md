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


### compiler le frido tl;dr  (trop long; donne un résumé)


```
    git clone https://github.com/LaurentClaessens/mazhe
    cd mazhe
    ./make_venv.sh
    ./compile_part.py lst_lefrido.json
```

### compiler une partie du frido : tl;dr

```
    git clone https://github.com/LaurentClaessens/mazhe
    cd mazhe
    ./make_venv.sh
```

- Éditer le fichier `lst_example.json` (en ayant changé son nom parce comme il est suivi par git, il ne faut pas compter dessus).
- Modifier la liste `tex_files` pour contenir la liste des fichiers à compiler.
- Modifier le champ `pdf_title` si vous voulez.
- compiler :
```
    ./compile_part.py lst_example.json
```

### Détails (plus geeky)

- Le script `make_venv.sh` installe python 3.10.12 dans le répertoire `pyenv`. Si vous avez déjà pyenv[1], vous pouvez changer la variable `pyenv_dir` dans `make_venv.sh` pour utiliser la version que vous avez déjà.

- Si l'installation de python 3.10.12 rate, vous pouvez essayer de changer le shebang dans `compile_part.py` pour utiliser la version de python de votre système. Faites toutefois attention que j'ai tendance à utiliser des annotation de types comme `list[str]` qui ne fonctionnent pas avec python `<3.10`.

- Le script `make_venv.sh` installe aussi le module `pytex` qui sert à toutes sortes de manipulation LaTeX avant et après la compilation proprement dite.



[1] Si vous ne savez pas ce que c'est, vous ne l'avez pas.
