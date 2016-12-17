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
    raise ValueError("No ISBN attributed for the title "+title)

def latex_code(title,n):
    """
    Return the latex code to be compiled for volume 'n'
    """

    text=open("couverture_generic.tex",'e').read()
    text=text.replace(TITLE,title).replace(NUMBER,str(n)).replace("ISBN_N",isbn(title,n))
    return text


title="Le Frido"

for i in [1,2,3]:
    code=latex_code(title,i)
    filename="couverture"+str(i)+".tex"
    with open(filename,'w') as f:
        f.write(code)

    os.system("pdflatex "+filename)
