"""Represent a LaTeX book."""

from typing import Any

from pathlib import Path

from pdfrw import PdfReader, PdfWriter
from pdfrw import PdfDict

from .dirmanage import base_dir
from src.chapter import Chapter
from src.splittoc import is_chapter_line
from src.utilities import dprint
from src.utilities import ciao


_:Any = dprint, ciao, base_dir


class Book(object):
    """
    Represents a book, from the TOC point of view.

    This is a wrapper around a list of chapters.
    """

    def __init__(self, toc_filename: Path, pdf_filename: Path):
        self.toc_filename = toc_filename.resolve()
        self.pdf_filename = pdf_filename.resolve()

        if not self.toc_filename.is_file():
            self.toc_filename.touch()

        self.pdf_reader: PdfReader
        if self.pdf_filename.is_file():
            self.pdf_reader = PdfReader(self.pdf_filename)

    def splitlines(self):
        """Return a list of lines."""
        with open(self.toc_filename, 'r') as f:
            text = f.read()
        return text.split("\n")

    def chapter_list(self):
        """Return a list of chapters."""
        return [Chapter(line) for line in self.splitlines()
                if is_chapter_line(line)]

    def get_chapter(self, n=2, title=None):
        """
        Return the requested chapter

        @param n integer : the number of the requested chapter
        @param title (string) : the title of the requested chapter

        @return a chapter (class Chapter)

        If 'n' is given, the title is ignored.
        """
        if n is not None:
            return self.chapter_list()[n-1]
        for chap in self.chapter_list():
            if chap.title == title:
                return chap
        raise ValueError(f"Unknkown chapter : {n}")

    def first_pages(self):
        return [x.first_page for x in self.chapter_list()]

    def tot_pages(self):
        """
        If no actual pdf is given, approximate the total
        page by the initial page of the last chapter.

        If a pdf filename is given, provides an exact answer.
        """
        pages = self.pdf_reader.pages
        # Probably a lack of stub for PdfReader
        assert isinstance(pages, list)
        return len(pages)

    def volume_first_theoretical_page(self, v, n):
        """
        Return the theoretical first page number of the volume

        @param v the volume number for which we are requesting the first
                  theoretical page.
        @param  n The total number of volumes
        @return number

        The returned number is not guaranteed to be integer.

        - Approximate the number of pages by the starting page number
          of the last chapter (which is the GNU FLD)
        - Let N be that number
        - Return 1->1, 2->N/n, 3-> 2N/n ... n->(n-1)N/n

        For a given chapter, we decide its volume number on the basis
        of its first page number.
        See position 1140726388
        """
        # A chapter is assigned to the (i-1)th volume when
        # the first page number of the ith part is larger
        # than the first page of the chapter.
        # Thus we need a 'fake' (n+1)th volume whose
        # first page number is for sure larger then any
        # chapter's first page.
        if v > n:
            return self.tot_pages() * 3
        return (v-1)*self.tot_pages()/n

    def volume_first_page(self, vol_no, num_vol):
        """
        Return the first page of volume 'vol_no' if we divide
        into 'num_vol' volumes

        @param v,n integers
        @return integer

        The returned integer is guaranteed to be the first page
        of a chapter.
        """
        for chap in self.chapter_list():
            fp = self.volume_first_theoretical_page(vol_no, num_vol)
            if chap.first_page > fp:
                return chap.first_page
        raise ValueError(f"Cannot find first pas of volume {vol_no}")

    def volume_last_page(self, v, n):
        """
        Return the last page of a volume.

        This is the same (-1) of the first page of the next one,
        but for the last volume for which the last page is the last
        page of the book.
        """
        if v == n:
            return self.tot_pages()
        return self.volume_first_page(v+1, n)-1

    def volume_number(self, chap, n):
        """
        Return the volume number of the given chapter

        @param chap : a chapter (type Chapter)
        @param n (integer) : the number of volumes we want
        @return : an integer
        """
        for v in range(1, n+2):
            if chap.first_page() < self.volume_first_theoretical_page(v, n):
                return v-1
        print("The first page of this chapter has a number which is larger then the last page of the book ???")
        print("chapter : ", chap.title())
        print("first page : ", chap.first_page())
        raise

    def get_pages(self) -> list[PdfDict]:
        """Return a list of pages"""
        pages = self.pdf_reader.pages
        assert isinstance(pages, list)
        return pages

    def extract_sub_pdf(self, first_page, last_page, filename):
        """
        copy the pages first_page -> last_page into the file 'filename'

        @param first_page, last_page : integers, the page numbers
        @param filename : string

        'first_page' and 'last_page' are the pdf numbers
        (the ones you see in the document),
        not the numbers in the python's list of pages
        (which begins at 0).
        """
        output = PdfWriter(filename)
        pages = self.get_pages()
        for k in range(first_page-1, last_page):
            output.addpage(pages[k])
        output.write()

    def rewrite_toc(self, n):
        if self.toc_filename.is_file():
            return
        # Print a summary
        print("Volumes :")
        for vol in range(1, n+1):
            print(vol, " -> ", self.volume_first_page(vol, n))

        print("Chapitres : ")
        for chap in self.chapter_list():
            print("Titre : ", chap.title)
            print("Première page :", chap.first_page)
            print("Volume : ", self.volume_number(chap, n))

        # Makes the work
        new_toc = []
        for line in self.splitlines():
            if is_chapter_line(line):
                chapter = Chapter(line)
                volume_number = self.volume_number(chapter, n)
                new_toc.append(chapter.hack(volume_number))
            else:
                new_toc.append(line)

        new_text = "\n".join(new_toc)

        with open(self.toc_filename, 'w') as toc_file:
            toc_file.write(new_text)
