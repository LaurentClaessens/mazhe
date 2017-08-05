#! /usr/bin/python3
# -*- coding: utf8 -*-

starting_string="""\contentsline {chapter}{\\numberline {"""

init_vol1=1
init_vol2=2
init_vol3=3

class ChapterLine(object):
    def __init__(self,original):
        self.original=original

    def number(self):
        a=self.original.split("{")
        sn=a[3][0:a[3].find("}")]
        return int(sn)
    def page(self):
        a=self.original.split("{")
        b=a[3].split("}")
        return(b[1])

        


def is_chapter_line(line):
    return line.startswith(starting_string)


with open("Inter_frido-mazhe_pytex.toc") as f:
    init_toc=f.read()

for line in init_toc.split("\n"):
    if is_chapter_line(line):
        chapter_line=ChapterLine(line)
        print(line)
        print(chapter_line.number())
        print(chapter_line.page())
