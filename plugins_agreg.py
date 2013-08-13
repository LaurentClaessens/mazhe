# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools

def accept_input(filename):
    return True

def set_isAgreg(A):
    u="\setcounter{isAgreg}{0}"
    A = A.replace(u,u.replace("0","1"))
    return A

def up_to_text(liste,text):
    for i,l in enumerate(liste):
        if l.startswith(text):
            return i

def accept_all_input(medicament):
    medicament.accept_input=accept_input

def remove_parts(A):
    B=[]
    lignes=A.splitlines()
    a=up_to_text(lignes,"\part{Pour l'agrégation}")
    b=up_to_text(lignes,"\part{Outils mathématiques}")
    B=lignes[0:a]
    B.extend(lignes[a+1:b])
    B.append("\input{0450_choses_finales} ")
    B.append("\end{document}")
    new_texte= "\n".join(B)
    return LaTeXparser.CodeLaTeX(new_texte,oldLaTeX=A)
