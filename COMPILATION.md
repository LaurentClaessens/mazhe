# How to compile ?

In this tutorial we assume that you have an empty directory `~/FOO` and we are going to install everything therein.

We propose two levels.
- you want only "Le Frido"
- you want everything, including exercices and some "research level" math.

The first case is less complicated; it is explained in a first section, in French. Then in a second section (in English) we explain the whole thing.

## Le Frido (en français)

Ainsi donc vous voulez avoir les sources du Frido et être capable des compiler. Bon choix.

### Les dépendances

D'abord il faut cloner les sources du Frido lui-même et les sources de `pytex` : 
```
cd ~/FOO
git clone https://tuleap.net/plugins/git/lefrido/lefrido.git
git clone https://github.com/LaurentClaessens/pytex
```

### Ça doit être accessible pour bash

- Le répertoire `~/FOO/pytex` doit être accessible à bash. Le plus simple est d'ajouter ceci dans votre `~/.bashrc` :
```
PATH=$PATH:~/FOO/pytex
```

### Compiler le pdf

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

## Everything (English)

## clone the dependencies

```
cd ~/FOO
git clone https://tuleap.net/plugins/git/lefrido/lefrido.git
git clone https://github.com/LaurentClaessens/pytex
```
The following is not mandatory for "Le Frido"; you only need it if you want to compile everything:
```
cd ~/texmf/tex/latex
git clone https://github.com/LaurentClaessens/exocorr
```

## Make it available for bash, python and latex

- The directory `~/FOO/pytex` must be available for bash.
- The directory `~/FOO/exocorr` must be available for LaTeX's usepackage mechanism.

The simplest is to append the following in `~/.bashrc` :
```
PATH=$PATH:~/FOO/pytex
```

Then, for the package `exocorr`,
```
sudo mktexlst
```

Now you can compile everything you want. For example :
```
cd ~/FOO/mazhe
pytex lst_actu.py
pytex lst_frido.py
pytex lst_everything.py
```
You can check for future references :
```
pytex lst_frido.py --verif
```

## Contribute

Now you can efficiently contribute.
