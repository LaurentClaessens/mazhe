#! /usr/bin/python3
# -*- coding: utf8 -*-

import os

class UnicodeCouple(object):
    def __init__(self,iec,utf):
        self.iec="\IeC {{{}}}".format(iec)
        self.utf=utf

def IeC_remove(s):
    IeC_couples=[]
    IeC_couples.append(UnicodeCouple("\\^\\i ","î") );
    IeC_couples.append(UnicodeCouple("\\'e","é"));
    IeC_couples.append(UnicodeCouple("\\^e ","ê"));
    IeC_couples.append(UnicodeCouple("\\^o ","ô"));
    IeC_couples.append(UnicodeCouple("\\\"o ","ö"));
    IeC_couples.append(UnicodeCouple("\\\"u ","ü"));
    IeC_couples.append(UnicodeCouple("\\`e","è")  );
    IeC_couples.append(UnicodeCouple("\\`A ","Á")  );
    IeC_couples.append(UnicodeCouple("\\`u ","ù")  );
    IeC_couples.append(UnicodeCouple("\\`a","à")  );
    IeC_couples.append(UnicodeCouple("\\'E","É")  );

    for c in IeC_couples:
        s=s.replace(c.iec,c.utf)
    return s

def is_chapter_line(line):
    """
    Return 'true' is 'line' is a line defining a chapter
    in the toc file.
    """
    starting_string="""\contentsline {chapter}{\\numberline {"""
    return line.startswith(starting_string)

class Chapter(object):
    """
    A chapter is defined from its TOC line which looks like
\contentsline {chapter}{\numberline {36}Cha\IeC {\^\i }nes de Markov \IeC {\`a} temps discret}{1731}{chapter.36}

    We use some string manipulations in order to extract the informations :
    - chapter title
    - starting page
    - chapter number
    """
    def __init__(self,original):
        self.original=original
        self.noIeC=IeC_remove(original)

    def number(self):
        a=self.noIeC.split("{")
        sn=a[3][0:a[3].find("}")]
        return int(sn)
    def title(self):
        a=self.noIeC.split("{")
        b=a[3].split("}")
        t=b[1]
        if "IeC" in t :
            print(t)
            raise ValueError 
        return(t)
    def first_page(self):
        a=self.noIeC.split("{")
        b=a[4].split("}")
        return int(b[0])
    def hack(self,i):
        """
        Append "(vol i)" at the end of the chapter's title.
        """
        a=self.original.split("}")
        a[-4]=a[-4]+" (Vol {})".format(i)
        return "}".join(a)

class Book(object):
    """
    Represents a book, from the TOC point of view.

    This is a wrapper around a list of chapters.
    """
    def __init__(self,toc_filename,pdf_filename=None):
        self.toc_filename=toc_filename
        self.pdf_filename=pdf_filename
    def splitlines(self):
        """
        Return a list of lines.
        """
        with open(self.toc_filename,'r') as f:
            text=f.read()
        return text.split("\n")
    def chapter_list(self):
        """
        Return a list of chapters
        """
        return [ Chapter(line) for line in self.splitlines() 
                            if is_chapter_line(line)    ]
    def first_pages(self) :
        return [x.first_page() for x in self.chapter_list]
    def tot_pages(self):
        """
        Approximate the total page by the initial page of the last chapter
        """
        return self.chapter_list()[-1].first_page()   
    def volume_first_theoretical_page(self,v,n):
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
        if v>n:
            return self.tot_pages()*3
        return (v-1)*self.tot_pages()/n
    def volume_first_page(self,v,n):
        """
        Return the first page of volume 'v' if we divide into 'n' volumes

        @param v,n integers
        @return integer 

        The returned integer is guaranteed to be the first page 
        of a chapter.
        """
        for chap in self.chapter_list():
            if chap.first_page() > self.volume_first_theoretical_page(v,n):
                return chap.first_page()
    def volume_number(self,chap,n):
        """
        Return the volume number of the given chapter

        @param chap : a chapter (type Chapter)
        @param n (integer) : the number of volumes we want
        @return : an integer
        """
        for v in range(1,n+2):
            if chap.first_page()<self.volume_first_theoretical_page(v,n):
                return v-1
        print("The first page of this chapter has a number which is larger then the last page of the book ???")
        print("chapter : ",chap.title())
        print("first page : ",chap.first_page())
        raise

    def rewrite_toc(self,n):

        # Print a summary
        print("Volumes :")
        for v in range(1,n+1):
            print(v," -> ",self.volume_first_page(v,n))

        print("Chapitres : ")
        for chap in self.chapter_list():
            print("Titre : ",chap.title())
            print("Première page :",chap.first_page())
            print("Volume : ",self.volume_number(chap,n))

        # Makes the work
        new_toc=[]
        for line in self.splitlines():
            if is_chapter_line(line):
                chapter=Chapter(line)
                vn=self.volume_number(chapter,n)
                new_toc.append(chapter.hack(vn))
            else :
                new_toc.append(line)

        new_text="\n".join(new_toc)
    
        with open(self.toc_filename,'w') as f:
            f.write(new_text)

def split_book(book,n):
    """
    Split the book in 'v' volumes
    
    @param book (type Book)
    @param n (integer) the number of volumes

    The 'book' parameter has to contain the pdf filename.
    """
