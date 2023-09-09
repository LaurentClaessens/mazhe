#! /usr/bin/python3

import os
import sys
import json
import datetime

from pdfrw import PdfReader, PdfWriter

import dirmanage
from src.book import Book
from src.options import Options
_ = sys

"""
This script generates the pdf's for printing/commercialization
by thebookedition.com.

Usage
-----

Step by step in `README.md`.

Number of volumes
-----------------

The variable `tot_volumes` is the number of volumes we want.
It has to be the same
- here
- in `lst_frido.py`
- in `lst_book.py`
"""


def first_filename(v, imprimeur):
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


def isbn(year, volume, imprimeur=None):
    volume_key = f"v{volume}"
    year_key = str(year)
    with open("isbn.json", 'r') as json_file:
        isbns = json.load(json_file)
    return isbns[year_key][imprimeur][volume_key]


def pepper(imprimeur):
    if imprimeur == "lulu":
        return ""
    if imprimeur == "thebookedition":
        return "(c) 2015-2022 David Revoy  pour les illustrations de " \
               "couverture CC-BY, \\url{https://www.peppercarrot.com/}"
    raise ValueError(f"Unknown printer : {imprimeur}")


def latex_code(options, volume, imprimeur):
    """
    Return the LaTeX code to be compiled.

    @param 'v' (integer), the volume number.
    @param 'imprimeur' (string) 'lulu' or 'thebookedition'
    @param 'year' (integer) the year
    """

    text = open("generic.tex", 'r').read()
    year = options.year
    title = options.title

    substitutions = [["TITLE", title],
                     ["NUMBER", str(volume)],
                     ["RISBN", isbn(year=year, volume=volume,
                                    imprimeur=imprimeur)],
                     ["YEAR+1", str(year+1)],
                     ["YEAR", str(year)],
                     ["PEPPERCARROT", pepper(imprimeur)]]

    for s in substitutions:
        text = text.replace(s[0], s[1])
    return text


def make_5_pages(options):
    """
    This script creates the pdf of the firsts page for the
    commercialized Frido.
    - two withe pages
    - one with the title on the top (small)
    - one speaking about the numerous versions of the book
    - one with the copyright on the bottom

    @param {int} `tot_volumes`
            the number of volumes
    """

    for imprimeur in options.imprimeurs:
        for volume in range(1, options.n_volumes + 1):
            code = latex_code(options, volume, imprimeur)
            filename = first_filename(volume, imprimeur) + ".tex"
            with open(filename, 'w') as f:
                f.write(code)
            os.system("pdflatex " + filename)


def split_book(book: Book, options):
    """
    Split the book into some volumes

    @param  book (type Book)

    The 'book' parameter has to contain the pdf filename.
    """
    n_volumes = options.n_volumes

    # - 'front.pdf' contains thematic index, toc, indexes
    print("Title: ", book.get_chapter(n=1).title)
    print("Number of pages: ", book.tot_pages())
    print("Creating front matter")
    book.extract_sub_pdf(1,
                         book.volume_first_page(1, n_volumes) - 1,
                         "front.pdf")
    for volume in range(1, n_volumes + 1):
        pI = book.volume_first_page(volume, n_volumes)
        pF = book.volume_last_page(volume, n_volumes)
        filename = matter_filename(volume)
        print(f"Creating matter of volume {volume}: "
              f"{pI} -> {pF} = {pF-pI}")
        book.extract_sub_pdf(pI, pF, filename)


def concatenate(options):
    for imprimeur in options.imprimeurs:
        for v in range(1, options.n_volumes + 1):
            first = PdfReader(first_filename(v, imprimeur)+".pdf")
            front = PdfReader("front.pdf")
            matter = PdfReader(matter_filename(v))

            out_filename = options.out_dir \
                / f"book_{options.year}_{v}_{imprimeur}.pdf"
            print(f"Concatenating for {imprimeur}, "
                  f"volume {v} -> {out_filename}")
            outpdf = PdfWriter(out_filename)
            outpdf.addpages(first.pages)

            if v == 1:
                outpdf.addpages(front.pages)
            outpdf.addpages(matter.pages)

            outpdf.write()


def make_the_work():
    """Make the whole work."""
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    options = Options(n_volumes=4,
                      year=date.year, imprimeurs=["thebookedition"])
    pdf_filename = "0-book.pdf"
    toc_filename = f"Inter_{date.year}-mazhe_pytex.toc"

    pdf_path = dirmanage.frido_dir / pdf_filename
    toc_path = dirmanage.frido_dir / toc_filename

    # Creating the 5 first pages
    make_5_pages(options)

    # Creating the front and matter of the 4 books.
    book = Book(toc_path, pdf_path)
    split_book(book, options)

    # Concatenating the files
    concatenate(options)


make_the_work()
