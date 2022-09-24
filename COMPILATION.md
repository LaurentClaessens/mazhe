# Compilation 

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

### pyenv

J'explique ici comment installer [pyenv](https://github.com/pyenv/pyenv).

```
# git clone https://github.com/pyenv/pyenv.git
# cd .pyenv/bin
# ./pyenv install 3.10.4
```

Si il vous indique des dépendances manquantes, un ou plusieurs des paquets suivants peuvent vous aider:
```
apt install  libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev  libffi-dev liblzma-dev python-openssl 
```
Si vous avez un problème avec libffi, il faut peut-être aussi faire la manipulation suivante:
``` 
cd /usr/lib/x86_64-linux-gnu
sudo ln -s libffi.so.7 libffi.so.6  # adaptez les numéros
``` 


### Le Frido
```
git clone https://github.com/LaurentClaessens/mazhe
cd mazhe
./make_venv.sh
./lst_frido.py
```

Vous pouvez vérifier les références vers le futur :
```
./lst_frido.py --verif
```
