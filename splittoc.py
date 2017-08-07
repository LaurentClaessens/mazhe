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
    def page(self):
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
    def __init__(self,toc_filename):
        self.toc_filename=toc_filename
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
    def tot_pages(self):
        """
        Approximate the total page by the initial page of the last chapter
        """
        return self.chapter_list()[-1].page()   
    def get_volume_pages(self,n):
        """
        Return the theoretical page number for the starting of 
        the volumes.

        @param  n The number of volumes
        @return list of numbers (not guaranteed to be integers)

        - Approximate the number of pages by the starting page number
          of the last chapter (which is the GNU FLD)
        - Let N be that number
        - Return [1,N/n,2N/n,\ldots (n-1)/N]

        For a given chapter, we decide its volume number on the basis
        of its first page number.
        See position 1140726388
        """

        # We need to add a 'fake' last volume whose first page
        # is for sure larger than any other pages in the book.
        # The reason is that a chapter whose first page in F will
        # be assigned to the (k-1)th volume where k is the first volume
        # whose first page is larger than F.
        a = [i*self.tot_pages()/n for i in range(0,n)]
        a.append( a[-1]*4  )
        return a

    def volume_number(self,chap,n):
        """
        Return the volume number of the given chapter

        @param chap : a chapter (type Chapter)
        @param n (integer) : the number of volumes we want
        @return : an integer
        """
        # position 1140726388
        for i,k in enumerate(self.get_volume_pages(n)):
            if k>chap.page():
                return i
        print("The first page of this chapter has a number which is larger then the last page of the book ???")
        raise ValueError

    def rewrite_toc(self,n):
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

def hack_toc_file(filename):
    if os.path.exists(filename):
        book=Book(filename)
        book.rewrite_toc()
    else :
        print("The given toc filename does not exist.")
