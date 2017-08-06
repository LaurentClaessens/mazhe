#! /usr/bin/python3
# -*- coding: utf8 -*-

starting_string="""\contentsline {chapter}{\\numberline {"""


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
    def hack(self,n):
        a=self.original.split("}")
        a[-4]=a[-4]+" (Vol {})".format(n)
        return "}".join(a)


        
def is_chapter_line(line):
    return line.startswith(starting_string)

def get_volume_pages(filename):
    with open(filename,'r') as f:
        init_toc=f.read()

    chapter_list=[ Chapter(line) for line in init_toc.split("\n") 
                        if is_chapter_line(line)    ]

    # Approximate the total page by the initial page of the last chapter
    tot_page=chapter_list[-1].page()   

    return 1,tot_page/3,2*tot_page/3


def hack_toc_file(filename):
    init_vol1, init_vol2,init_vol3= get_volume_pages(filename)
    with open(filename,'r') as f:
        text=f.read()

    new_toc=[]
    for line in text.split("\n") :
        if is_chapter_line(line):
            chapter=Chapter(line)
            n=1
            if chapter.page() > init_vol2 :
                n=2
            if chapter.page() > init_vol3 :
                n=3
            new_toc.append(chapter.hack(n))
        else :
            new_toc.append(line)

    new_text="\n".join(new_toc)

    with open(filename,'w') as f:
        f.write(new_text)
