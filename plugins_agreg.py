# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools


# Replaced by a lambda, March, 26, 2014
#def accept_input(filename):
#    return True


agreg_script_mark_list=[]
agreg_script_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
agreg_script_mark_list.append("% SCRIPT MARK -- GARDE MES NOTES")
agreg_script_mark_list.append("% SCRIPT MARK -- TOC")
agreg_script_mark_list.append("% SCRIPT MARK -- AGRÉGATION")
agreg_script_mark_list.append("% SCRIPT MARK -- FINAL")

mazhe_mark_list=[]
mazhe_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
mazhe_mark_list.append("% SCRIPT MARK -- GARDE MAZHE")
mazhe_mark_list.append("% SCRIPT MARK -- TOC")
mazhe_mark_list.append("% SCRIPT MARK -- ENGLISH INTRODUCTION")
mazhe_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
mazhe_mark_list.append("% SCRIPT MARK -- AGRÉGATION")
mazhe_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUE")
mazhe_mark_list.append("% SCRIPT MARK -- RESEARCH PART")
mazhe_mark_list.append("% SCRIPT MARK -- MATLAB")
mazhe_mark_list.append("% SCRIPT MARK -- EXERCICES")
mazhe_mark_list.append("% SCRIPT MARK -- FINAL")


def set_isAgreg(A):
    u="\setcounter{isAgreg}{0}"
    A = A.replace(u,u.replace("0","1"))
    return A

def up_to_text(liste,text):
    for i,l in enumerate(liste):
        if l.startswith(text):
            return i

def set_commit_hexsha(A):
    print("set_commit_hexsha plugin")
    import git
    repo=git.Repo("")
    hexsha=repo.commit().hexsha
    if repo.is_dirty():
        hexsha=hexsha+" -- and slighty more"
    u="\\newcommand{\GitCommitHexsha}{\info{missing information}}"
    print(hexsha)
    A = A.replace(u,u.replace("missing information",hexsha))
    return A


def accept_all_input(medicament):
    medicament.accept_input=lambda x: True

class keep_script_marks(object):
    """
    The file "mazhe.tex" has some "SCRIPT MARK" lines that give the structure of the document.

    Notice that whatever the order of the marks is in the given list, it will respect the order of mazhe.tex
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
        # Select the usefull marks and sort them
        marks=[  x for x in script_mark_dict.keys() if x in self.keep_mark_list ]
        marks.sort(key=lambda a:script_mark_dict[a][0])
        for mark in marks :
            a=script_mark_dict[mark][0]
            b=script_mark_dict[mark][1]
            B.extend(  lignes[a:b] )
        new_texte= "\n".join(B)
        return LaTeXparser.CodeLaTeX(new_texte,oldLaTeX=A)
