# Compilation 

Dans ce fichier nous décrivons comment compiler le Frido.

La compilation du Frido demande l'utilisation d'un script spécifique.

Nous supposons un répertoire vide `~/FOO` dans lequel nous allons tout mettre.

## Prérequis

Vous devez avoir python3 installé et disponible sur votre système. 

## Les dépendances

D'abord il faut cloner les sources du Frido lui-même et les sources de `pytex` : 
```
cd ~/FOO
git clone https://tuleap.net/plugins/git/lefrido/lefrido.git
git clone https://github.com/LaurentClaessens/pytex
```

### pytex accessible à bash

- Le répertoire `~/FOO/pytex` doit être accessible à bash. Le plus simple est d'ajouter ceci dans votre `~/.bashrc` :
```
PATH=$PATH:~/FOO/pytex
```

### Compiler le Frido

Maintenant il est possible de compiler le Frido :
```
cd ~/FOO/lefrido
pytex lst_frido.py
```
Vous pouvez vérifier les références vers le futur :
```
pytex lst_frido.py --verif
```

## Contribuer

C'est parti !
