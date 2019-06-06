#! /usr/bin/python3
# -*- coding: utf8 -*-

import os
from pdfrw import PdfReader,PdfWriter
from splittoc import Book

"""
This script generates the pdf's for printing/commercialization
by thebookedition.com and lulu.com

Usage
-----

- compile with 
  ```
  pytex lst_book.py
  ``` 
  this generates 0-book.pdf which will be used here to extract the
  TOC/matters.
- launch this script


Number of volumes
-----------------

The variable `tot_volumes` is the number of volumes we want. 
It has to be the same
- here
- in `lst_frido.py`
- in `lst_book.py`
"""


def first_filename(v,imprimeur):
    """
    return the filename in which to write the pdf containing
    the 5 first pages.
    """
    return "firsts_5_"+imprimeur+"_"+str(v)

def matter_filename(volume):
    """
    Return the filename in which to write the pdf containing
    the matter of volume 'v'.
    """
    return f"matter_{volume}.pdf"


def isbn(title, year, v, imprimeur=None):
    if title == "Le Frido" and year == 2018:
        if imprimeur == "lulu":
            if v == 1:
                return "979-10-97085-14-8"
            if v == 2:
                return "979-10-97085-15-5"
            if v == 3:
                return "979-10-97085-16-2"
            if v == 4:
                return "979-10-97085-17-9"
        if imprimeur == "thebookedition":
            if v == 1:
                return "979-10-97085-10-0"
            if v == 2:
                return "979-10-97085-11-7"
            if v == 3:
                return "979-10-97085-12-4"
            if v == 4:
                return "979-10-97085-13-1"

    if title == "Le Frido" and year == 2017:
        if imprimeur == "lulu":
            if v == 1:
                return "ISBN-lulu1"
            if v == 2:
                return "ISBN-lulu2"
            if v == 3:
                return "ISBN-lulu3"
            if v == 4:
                return "ISBN-lulu4"
        if imprimeur == "thebookedition":
            if v == 1:
                return "ISBN-thebookedition1"
            if v == 2:
                return "ISBN-thebookedition2"
            if v == 3:
                return "ISBN-thebookedition3"
            if v == 4:
                return "ISBN-thebookedition4"

    if title == "Le Frido":
        if v == 1:
            return "978-2-9540936-5-9"
        if v == 2:
            return "978-2-9540936-6-6"
        if v == 3:
            return "978-2-9540936-7-3"


    default = "No ISBN attributed for the title "+title
    print(default)
    return default

def pepper(imprimeur):
    if imprimeur == "lulu":
        return ""
    if imprimeur == "thebookedition":
        return "(c) 2015 David Revoy  pour les illustrations de couverture CC-BY, \\url{https://www.peppercarrot.com/}"
    raise ValueError(f"Unknown printer : {imprimeur}")


def latex_code(title,year,v,imprimeur):
    """
    Return the LaTeX code to be compiled.

    @param 'v' (integer), the volume number.
    @param 'imprimeur' (string) 'lulu' or 'thebookedition'
    @param 'year' (integer) the year
    """

    text = open("generic.tex",'r').read()

    substitutions = [  ["TITLE",title],["NUMBER",str(v)],["RISBN",isbn(title,year=year,v=v,imprimeur=imprimeur)],["YEAR+1",str(year+1)],["YEAR",str(year)],["PEPPERCARROT",pepper(imprimeur)]  ]

    for s in substitutions:
        text = text.replace(s[0],s[1])
    return text


def make_5_pages(tot_volumes, title, year):
    """
    This script creates the pdf of the firsts page for the commercialized Frido.
    - two withe pages
    - one with the title on the top (small)
    - one speaking about the numerous versions of the book
    - one with the copyright on the bottom

    @param {int} `tot_volumes` 
            the number of volumes
    """

    for imprimeur in ["lulu", "thebookedition"]:
        for v in range(1, tot_volumes + 1):
            code = latex_code(title,year,v,imprimeur)
            filename = first_filename(v,imprimeur)+".tex"
            with open(filename,'w') as f:
                f.write(code)
            os.system("pdflatex "+filename)

def split_book(book, tot_volumes):
    """
    Split the book into some volumes

    @param  book (type Book)
    @param {int} tot_volumes
            the number of volumes

    The 'book' parameter has to contain the pdf filename.
    """

    # - 'front.pdf' contains thematic index, toc, indexes
    print("Title: ", book.get_chapter(n=1).title())
    print("Number of pages: ", book.tot_pages())
    print("Creating front matter")
    book.extract_sub_pdf(2, 
                 book.volume_first_page(1, tot_volumes) - 1, 
                 "front.pdf")
    for volume in range(1, tot_volumes + 1):
        pI = book.volume_first_page(volume, tot_volumes)
        pF = book.volume_last_page(volume, tot_volumes)
        filename = matter_filename(volume)
        print(f"Creating matter of volume {volume} : {pI} -> {pF}")
        book.extract_sub_pdf(pI, pF, filename)

def concatenate(tot_volumes):
    for imprimeur in ["lulu", "thebookedition"]:
        for v in range(1, tot_volumes + 1):
            print(f"Concatenating for {imprimeur}, volume {v}")
            first = PdfReader(first_filename(v,imprimeur)+".pdf")
            front = PdfReader("front.pdf")
            matter = PdfReader(matter_filename(v))

            out_filename = f"book_{v}_{imprimeur}.pdf"
            outpdf = PdfWriter(out_filename)
            outpdf.addpages(first.pages)

            if v == 1:
                outpdf.addpages(front.pages)
            outpdf.addpages(matter.pages)

            outpdf.write()

def make_the_work():
    """
    Make the whole work.
    """
    tot_volumes = 4
    pdf_filename = "../0-book.pdf"
    toc_filename = "../Inter_book-mazhe_pytex.toc"

    # Creating the 5 first pages
    make_5_pages(tot_volumes, title="Le Frido", year=2018)

    # Creating the front and matter of the 4 books.
    book = Book(toc_filename, pdf_filename)
    split_book(book, tot_volumes)

    # Concatenating the files
    concatenate(tot_volumes)

make_the_work()
