#! /usr/bin/env python3
# -*- coding: utf8 -*-

# This script creates the pdf of the firsts page for the commercialized Frido.
# - two withe pages
# - one with the title on the top (small)
# - one speaking about the numerous versions of the book
# - one with the copyright on the bottom (do not forget David for the thebookedition's version)

import os

def isbn(title,year,v,imprimeur=None):
    if title=="Le Frido":
        if v==1:
            return "978-2-9540936-5-9"
        if v==2:
            return "978-2-9540936-6-6"
        if v==3:
            return "978-2-9540936-7-3"       

    # En attente de réponse de la part de l'AFNIL
    # Ais-je besoin d'ISBN différents pour Lulu et thebookedition ?
    if title=="Le Frido" and year==2017:
        if imprimeur == "lulu":
            if v==1:
                return "ISBN-lulu1"
            if v==2:
                return "ISBN-lulu2"
            if v==3:
                return "ISBN-lulu3"
            if v==4:
                return "ISBN-lulu4"
        if imprimeur == "thebookedition":
            if v==1:
                return "ISBN-thebookedition1"
            if v==2:
                return "ISBN-thebookedition2"
            if v==3:
                return "ISBN-thebookedition3"
            if v==4:
                return "ISBN-thebookedition4"


    default = "No ISBN attributed for the title "+title
    print(default)
    return default

def pepper(imprimeur):
    if imprimeur=="lulu":
        return ""
    if imprimeur=="thebookedition":
        return "(c) 2015 David Revoy  pour les illustrations de couverture CC-BY, \\url{https://www.peppercarrot.com/}"


def latex_code(title,year,v,imprimeur):
    """
    Return the LaTeX code to be compiled.

    @param 'v' (integer), the volume number.
    @param 'imprimeur' (string) 'lulu' or 'thebookedition'
    @param 'year' (integer) the year
    """

    text=open("generic.tex",'r').read()

    substitutions=[  ["TITLE",title],["NUMBER",str(v)],["RISBN",isbn(title,v,imprimeur)],["YEAR+1",str(year+1)],["YEAR",str(year)],["PEPPERCARROT",pepper(imprimeur)]  ]

    for s in substitutions:
        text=text.replace(s[0],s[1])
    return text


title="Le Frido"
year=2017

for imprimeur in ["lulu","thebookedition"]:
    for v in range(1,5):
        code=latex_code(title,year,v,imprimeur)
        filename="firsts_5_"+imprimeur+"_"+str(v)+".tex"
        with open(filename,'w') as f:
            f.write(code)

        os.system("pdflatex "+filename)
