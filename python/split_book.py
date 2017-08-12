#! /usr/bin/python3
# -*- coding: utf8 -*-

from splittoc import split_book
from splittoc import Book

pdf_filename="0-book.pdf"
toc_filename="Inter_book-mazhe_pytex.toc"

book=Book(toc_filename,pdf_filename)
split_book(book,4)
