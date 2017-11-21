# How to compile

In this tutorial we assume that you have an empty directory `~/FOO` and we are going to install everything therein.

## clone the dependencies

```
cd ~/FOO
git clone https;//github.com/LaurentClaessens/mazhe
git clone https://github.com/LaurentClaessens/pytex
```
Then :
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
