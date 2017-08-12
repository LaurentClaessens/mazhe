#! /usr/bin/python3
# -*- coding: utf8 -*-

from splittoc import Book
from make_first_5_pages import frido_2017

pdf_filename="0-book.pdf"
toc_filename="Inter_book-mazhe_pytex.toc"

def split_book(book,n):
    """
    Split the book in 'v' volumes
    
    @param book (type Book)
    @param n (integer) the number of volumes

    The 'book' parameter has to contain the pdf filename.
    """

    from pdfrw import PdfReader

    # - 'front.pdf' contains thematic index, toc, indexes
    print(book.get_chapter(n=1).title())
    print(book.tot_pages())
    print("Creating front matter")
    book.sub_pdf(2,book.volume_first_page(1,n)-1,"front.pdf")
    for v in range(1,n+1):
        pI=book.volume_first_page(v,n)
        pF=book.volume_last_page(v,n)
        filename="matter_{}.pdf".format(v)
        print("Creating matter of volume {} : {} -> {}".format( v, pI, pF ))
        book.sub_pdf(pI,pF,filename)

# Creating the 5 first pages
frido_2017()

# Creating the front and matter of the 4 books.
book=Book(toc_filename,pdf_filename)
split_book(book,4)
