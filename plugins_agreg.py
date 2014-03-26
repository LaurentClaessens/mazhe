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

class keep_script_marks(object):
    """
    The file "mazhe.tex" has some "SCRIPT MARK" lines that give the structure of the document.
    """
    def __init__(self,keep_mark_list):
        self.keep_mark_list=keep_mark_list
    def script_mark_dict(self,C):
        dic={}
        dic["init"]=0
        lp="init"
        lignes=C.splitlines()
        for i,l in enumerate(lignes) :
            if l.startswith("% SCRIPT MARK"):
                dic[l]=i+1
                dic[lp]=(dic[lp],i+1)
                lp=l
        dic[lp]=(dic[lp],len(lignes))
        return dic
    def __call__(self,A):
        C=LaTeXparser.CodeLaTeX(A.given_text,keep_comments=True)   # I need the comments in order to see "SCRIPT MARK"
        script_mark_dict=self.script_mark_dict(C)
        B=[]
        lignes=A.splitlines()
        for mark in self.keep_mark_list :
            a=script_mark_dict[mark][0]
            b=script_mark_dict[mark][1]
            B.extend(  lignes[a:b] )
        new_texte= "\n".join(B)
        return LaTeXparser.CodeLaTeX(new_texte,oldLaTeX=A)
