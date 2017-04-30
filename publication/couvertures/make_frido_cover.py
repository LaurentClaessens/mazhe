#! /usr/bin/env python3
# -*- coding: utf8 -*-

import os

def isbn(title,n):
    if title=="Le Frido":
        if n==1:
            return "978-2-9540936-5-9"
        if n==2:
            return "978-2-9540936-6-6"
        if n==3:
            return "978-2-9540936-7-3"       

    default = "No ISBN attributed for the title "+title
    print(default)
    return default

def latex_code(title,n):
    """
    Return the latex code to be compiled for volume 'n'
    """

    text=open("couverture_generic.tex",'r').read()
    text=text.replace("TITLE_N",title).replace("NUMBER_N",str(n)).replace("ISBN_N",isbn(title,n))
    return text


title="Le Frido 2016"

for i in [1,2,3]:
    code=latex_code(title,i)
    filename="couverture"+str(i)+".tex"
    with open(filename,'w') as f:
        f.write(code)

    os.system("pdflatex "+filename)
