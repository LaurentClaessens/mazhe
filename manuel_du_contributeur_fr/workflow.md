# The standard compiling procedure

## The constraints

We describe here some problems we encounter when one wants to compile a big stuff like Le Frido/Mazhe and how we did solve them.

From the same LaTeX source we have to be able to create

* The full document : 3900 pages with subdivisions in 'part' (mazhe).
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


## Division in three parts for commercialisation

Well ... I have to admit that I made it when I had to learn C++. So the work in done in C++ instead of python.

We have a script `decoupe.sh` which make the work. Basically :

* The compilation with `pytex lst_book.py` make a Frido compilation, but changing the line `\boolfalse{isBook}` into `\booltrue{isBook}`. One of the use of that boolean is that we have a picture from xkcd (in the RSA part) which is published under a licence authorizing non-commercial use. So this picture is inside a boolean test on `isBook` : when compiling the book, this picture does not appear.
* Let us call  `book.pdf` the result. This is only one pdf.
* The we use `pdftk` to perform massive pdf manipulations.
* We search in the `toc` file at what pages begin the TOC and the two chapters which make the second and third part
* We create 4 files : one containing only the table of content, one containing the chapter of the first volume, one the chapters of the second part and one for the third part.
* We also create 3 files for the covers.
* We combine them in order to create the 3 pdf.

The C++ code is in `publication/volumes`

## Main point to remember : everything is possible 'on the fly'

When we compile such or such part, we first pass the LaTeX code to some script (usually python) that can perform arbitrary string manipulations before to proceed with pdflatex. In particular we can pass a boolean from false to true before the compilation. This is quite powerful. We can of course analyse the `aux`, `toc`, `ind` files between two passes and be really cool.  

## Main point to remember : all automated

I'm a nazis of automation. Only one command line should make all the work of creating one version.

