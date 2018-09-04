# Compile mazhe

This file describes how to compile the full book `mazhe`.

In this tutorial we assume that you have an empty directory `~/FOO` and we are going to install everything therein.

## Download the dependencies

- Here are the LaTeX sources:
```
git clone https://tuleap.net/plugins/git/lefrido/lefrido.git
```
- Here is a LaTeX dependency:
```
git clone https://github.com/LaurentClaessens/exocorr
```
You have to put that somewhere where LaTeX will find it.

## Make it available for latex

The directory `~/FOO/exocorr` must be available for LaTeX's usepackage mechanism.

The simplest is to append the following in `~/.bashrc` :
```
PATH=$PATH:~/FOO/pytex
```

Then, for the package `exocorr`,
```
sudo mktexlst
```

## Compilation

Now you can compile the whole document:
```
pdflatex mazhe.tex
bibtex mazhe
makeindex mazhe
```
to be done more or less three times to get all the cross-references correct.

## Contribute

Now you can efficiently contribute.
