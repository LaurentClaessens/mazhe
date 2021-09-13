# Compilation 

Dans ce fichier nous décrivons comment compiler le Frido.

## compiler tout sans distinctions

```
mkdir FRIDO
cd FRIDO
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


## Compiler le Frido

La compilation du Frido demande l'utilisation d'un script spécifique. Il y a plusieurs méthodes

- si vous êtes à l'aise avec python
- si vous êtes à l'aise avec docker

## Méthode si vous être à l'aise avec python

D'abord il faut cloner les sources du Frido lui-même et les sources de `pytex` : 
```
git clone https://github.com/LaurentClaessens/mazhe
git clone https://github.com/LaurentClaessens/pytex
```

Il faut ensuite rendre `pytex` accessible à bash. Le plus simple est d'ajouter ceci dans votre `~/.bashrc` :
```
PATH=$PATH:/path/to/pytex
```

Maintenant il est possible de compiler le Frido :
```
cd /path/to/mazhe
pytex lst_frido.py
```
Vous pouvez vérifier les références vers le futur :
```
pytex lst_frido.py --verif
```

Si vous voulez compiler seulement une partie:

- Regardez le fichier `lst_exemple.py`. 
- Copiez-le sous le nom `lst_foobar.py`
- Modifiez la liste des fichiers à inclure
- Compilez `pytex lst_foobar.py`

## Méthode si vous être à l'aise avec docker


Gjacquenot nous a créé un petit [docker](https://docs.docker.com/engine/install/ubuntu/) avec toutes les dépendances : [Compilation_frido](https://github.com/Gjacquenot/Compilation_frido).

Un simple `make` crée le docker et compile le Frido et ses variations.
