# The standard compiling procedure

## The constraints

We describe here some problems we encounter when one wants to compile a big stuff like Le Frido/Giulietta and how we did solve them.

From the same LaTeX source we have to be able to create

* The full document : 3900 pages with subdivisions in 'part' (Giulietta).
* Le Frido : 1800 page with no subdivisions in 'part'. This is one of the parts of the full document.
* 3 documents that are the division in 'volumes' of Le Frido. Each of the must contain
   - the full table of content of Le Frido
   - some chapters

  This division is given by the name of two chapters that are the beginning of volume 2 and volume 3.

The universal solution for that adopted in this project is to create many python scripts which perform the necessary changes to the LaTeX code before to launch the compilation. The script [pytex](https://github.com/LaurentClaessens/pytex) is developed for that purpose.

## Le Frido

Invoking
```
pytex lst_frido.py
```
will
* copy the file `mazhe.tex`
* remove the `\input` corresponding to files which have not to be included (the placeholders `%SCRIPT MARK` are there for that purpose)
* change the line `\boolfalse{isFrido}` into `\booltrue{isFrido}`.
* change some lines in the cover file to add the number of the last commit on the cover.
* pass the result to `pdflatex`
* check that, in the bibliography, the reference `MonCerveau` is the first one.
