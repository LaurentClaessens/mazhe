# Compile Giulietta

This file describes how to compile the full book `Giulietta`.

## Get the sources

- Here are the LaTeX sources:
```
mkdir FRIDO
cd FRIDO
git clone https://github.com/LaurentClaessens/mazhe
cd mazhe
```

Now you can compile the whole document:
```
pdflatex mazhe.tex
bibtex mazhe
makeindex mazhe
```
to be done more or less three times to get all the cross-references correct.
