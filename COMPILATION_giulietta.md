# Compile Giulietta

This file describes how to compile the full book `Giulietta`.

## Get the sources

- Here are the LaTeX sources:
```
git clone https://github.com/LaurentClaessens/mazhe
```

## Compilation, the easy way

Now you can compile the whole document:
```
pdflatex mazhe.tex
bibtex mazhe
makeindex mazhe
```
to be done more or less three times to get all the cross-references correct.

## Compilation, the efficient way

### Prerequisites

You need `python3` installed and ready to use on your system.

### Download 

You need to clone the sources of Giulietta and `pytex`:
```
cd ~/GIULIETTA
git clone https://github.com/LaurentClaessens/mazhe
git clone https://github.com/LaurentClaessens/pytex
```

### pytex callable by bash

The directory `~/GIULIETTA/pytex` muse be accessible for bash. The easier is to add the following in `~/.bashrc`:
```
PATH=$PATH:~/GIULIETTA/pytex
```

### Compile a part

It is now possible to compile only a part of Giulietta.

To compile everything:
```
cd ~/GIULIETTA/mazhe
pytex lst_giulietta.py
```

If you want a part, see the file `lst_example.py`.

### Check mathematical consistency

Pytex allows to ensure yourself that every `\ref` and `\eqref` are pointing to labels which are defined before:
```
pytex lst_giulietta.py --verif
```
