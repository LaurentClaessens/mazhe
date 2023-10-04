# Compilation 


## tl;rr


```
    git clone https://github.com/LaurentClaessens/mazhe
    ce mazhe
    ./make_venv.sh
    ./lst_lefrido.py
```


Here we explain how to compile Le Frido and Guilietta.

## Download

```
    git clone https://github.com/LaurentClaessens/mazhe
```

## Compile everything (easy)

Run the following at least three times:
```
pdflatex mazhe.tex
bibtex mazhe
makeindex mazhe
```

## Compiler le Frido

Installer les prérequis.

Les paquets suivants sont peut-être utiles pour installer python, mais je ne suis pas certain:

Ubuntu 22.04
```
    sudo apt install  build-essential zlib1g-dev libffi-dev libssl-dev libreadline-dev libsqlite3-dev liblzma-dev libbz2-dev
```
Dites-moi si c'est vraiment nécessaire, et les lignes correspondantes pour les autres systèmes.

Ensuite : 
```
    ./make_venv.sh
```
Ce script installe la bonne version de python via [pyenv](https://github.com/pyenv/pyenv) en utilisant celui qui est déjà dans `~/.pyenv` si il existe. Sinon, ça installe dans ce répertoire-ci.
