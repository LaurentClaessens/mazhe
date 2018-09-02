#! /usr/bin/python3
# -*- coding: utf8 -*-

import os
from pdfrw import PdfReader,PdfWriter
from splittoc import Book

pdf_filename = "../0-book.pdf"
toc_filename = "../Inter_book-mazhe_pytex.toc"

def first_filename(v,imprimeur):
    """
    return the filename in which to write the pdf containing
    the 5 first pages.
    """
    return "firsts_5_"+imprimeur+"_"+str(v)

def matter_filename(v):
    """
    Return the filename in which to write the pdf containing
    the matter of volume 'v'.
    """
    return "matter_{}.pdf".format(v)


def isbn(title,year,v,imprimeur=None):
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


def make_5_pages(n):
    """
    This script creates the pdf of the firsts page for the commercialized Frido.
    - two withe pages
    - one with the title on the top (small)
    - one speaking about the numerous versions of the book
    - one with the copyright on the bottom

    @param n (integer) the number of volumes
    """
    title = "Le Frido"
    year = 2017

    for imprimeur in ["lulu","thebookedition"]:
        for v in range(1,n+1):
            code = latex_code(title,year,v,imprimeur)
            filename = first_filename(v,imprimeur)+".tex"
            with open(filename,'w') as f:
                f.write(code)
            os.system("pdflatex "+filename)

def split_book(book,n):
    """
    Split the book in 'v' volumes

    @param book (type Book)
    @param n (integer) the number of volumes

    The 'book' parameter has to contain the pdf filename.
    """

    # - 'front.pdf' contains thematic index, toc, indexes
    print(book.get_chapter(n=1).title())
    print(book.tot_pages())
    print("Creating front matter")
    book.sub_pdf(2,book.volume_first_page(1,n)-1,"front.pdf")
    for v in range(1,n+1):
        pI = book.volume_first_page(v,n)
        pF = book.volume_last_page(v,n)
        filename = matter_filename(v)
        print("Creating matter of volume {} : {} -> {}".format( v, pI, pF ))
        book.sub_pdf(pI,pF,filename)

def concatenate(n):
    for imprimeur in ["lulu","thebookedition"]:
        for v in range(1,n+1):
            print("Concatenating for {}, volume {}".format(imprimeur,str(v)))
            first = PdfReader(first_filename(v,imprimeur)+".pdf")
            front = PdfReader("front.pdf")
            matter = PdfReader(matter_filename(v))

            out_filename = "book_{}_{}.pdf".format(str(v),imprimeur)
            outpdf = PdfWriter(out_filename)
            outpdf.addpages(first.pages)
            outpdf.addpages(front.pages)
            outpdf.addpages(matter.pages)

            outpdf.write(out_filename)

n = 4

# Creating the 5 first pages
make_5_pages(n)

# Creating the front and matter of the 4 books.
book = Book(toc_filename,pdf_filename)
split_book(book,n)

# Concatenating the files
concatenate(n)
