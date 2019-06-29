# Compilation 

Dans ce fichier nous décrivons comment compiler le Frido.

Nous supposons un répertoire vide `~/FRIDO` dans lequel nous allons tout mettre.

## La méthode directe

```
cd ~/FRIDO
git clone https://github.com/LaurentClaessens/mazhe
cd mazhe
```

Vous pouvez maintenant compiler avec ceci :
```
pdflatex mazhe.tex
bibtex mazhe
makeindex mazhe
```
À lancer au moins trois fois pour avoir toutes les références correctes.


## Ce n'est pas le Frido, ça !

En effet, en compilant `mazhe.tex` vous obtenez plus que le Frido. Le Frido est en effet une partie d'un livre plus long contenant de la mathématique plus avancée.

La compilation du Frido demande l'utilisation d'un script spécifique.

## Prérequis

Vous devez avoir python3 installé et disponible sur votre système. 

## Les dépendances

D'abord il faut cloner les sources du Frido lui-même et les sources de `pytex` : 
```
cd ~/FRIDO
git clone https://github.com/LaurentClaessens/mazhe
git clone https://github.com/LaurentClaessens/pytex
```

### pytex accessible à bash

- Le répertoire `~/FRIDO/pytex` doit être accessible à bash. Le plus simple est d'ajouter ceci dans votre `~/.bashrc` :
```
PATH=$PATH:~/FRIDO/pytex
```

### Compiler le Frido

Maintenant il est possible de compiler le Frido :
```
cd ~/FRIDO/mazhe
pytex lst_frido.py
```
Vous pouvez vérifier les références vers le futur :
```
pytex lst_frido.py --verif
```

### Compiler seulement une partie

- Regardez le fichier `lst_exemple.py`. 
- Copiez-le sous le nom `lst_foobar.py`
- Modifiez la liste des fichiers à inclure
- Compilez `pytex lst_foobar.py`

## Contribuer

C'est parti !
