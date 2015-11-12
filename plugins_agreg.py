# -*- coding: utf8 -*-

# This is part of (almost) Everything I know in mathematics
# Copyright (c) 2014-2015   (et en fait sûrement plus)
#   Laurent Claessens
# See the file fdl-1.3.txt for copying conditions.


from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools

# Replaced by a lambda, March, 26, 2014
#def accept_input(filename):
#    return True

agreg_mark_list=[]
agreg_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
agreg_mark_list.append("% SCRIPT MARK -- GARDE MES NOTES")
agreg_mark_list.append("% SCRIPT MARK -- TOC")
agreg_mark_list.append("% SCRIPT MARK -- AGRÉGATION")
agreg_mark_list.append("% SCRIPT MARK -- FINAL")

mesnotes_mark_list=agreg_mark_list[:]
mesnotes_mark_list.append("% SCRIPT MARK -- DÉVELOPPEMENTS POSSIBLES")

outilsmath_mark_list=[]
outilsmath_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
outilsmath_mark_list.append("% SCRIPT MARK -- GARDE ENSEIGNEMENT")
outilsmath_mark_list.append("% SCRIPT MARK -- TOC")
outilsmath_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUES")
outilsmath_mark_list.append("% SCRIPT MARK -- FINAL")

enseignement_mark_list=[]
enseignement_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
enseignement_mark_list.append("% SCRIPT MARK -- GARDE ENSEIGNEMENT")
enseignement_mark_list.append("% SCRIPT MARK -- TOC")
enseignement_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
enseignement_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUES")
enseignement_mark_list.append("% SCRIPT MARK -- MATLAB")
enseignement_mark_list.append("% SCRIPT MARK -- EXERCICES")
enseignement_mark_list.append("% SCRIPT MARK -- CdI")
enseignement_mark_list.append("% SCRIPT MARK -- FINAL")

mazhe_mark_list=[]
mazhe_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
mazhe_mark_list.append("% SCRIPT MARK -- GARDE MAZHE")
mazhe_mark_list.append("% SCRIPT MARK -- TOC")
mazhe_mark_list.append("% SCRIPT MARK -- ENGLISH INTRODUCTION")
mazhe_mark_list.append("% SCRIPT MARK -- MOODLE")
mazhe_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
mazhe_mark_list.append("% SCRIPT MARK -- AGRÉGATION")
mazhe_mark_list.append("% SCRIPT MARK -- DÉVELOPPEMENTS POSSIBLES")
mazhe_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUES")
mazhe_mark_list.append("% SCRIPT MARK -- RESEARCH PART")
mazhe_mark_list.append("% SCRIPT MARK -- MATLAB")
mazhe_mark_list.append("% SCRIPT MARK -- EXERCICES")
mazhe_mark_list.append("% SCRIPT MARK -- CdI")
mazhe_mark_list.append("% SCRIPT MARK -- FINAL")

nonagreg_mark_list=[]
nonagreg_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
nonagreg_mark_list.append("% SCRIPT MARK -- GARDE MAZHE")
nonagreg_mark_list.append("% SCRIPT MARK -- TOC")
nonagreg_mark_list.append("% SCRIPT MARK -- ENGLISH INTRODUCTION")
nonagreg_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
nonagreg_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUE")
nonagreg_mark_list.append("% SCRIPT MARK -- RESEARCH PART")
nonagreg_mark_list.append("% SCRIPT MARK -- MATLAB")
nonagreg_mark_list.append("% SCRIPT MARK -- EXERCICES")
nonagreg_mark_list.append("% SCRIPT MARK -- CdI")
nonagreg_mark_list.append("% SCRIPT MARK -- FINAL")

class set_filename(object):
    def __init__(self,new_output_filename):
        self.new_output_filename=new_output_filename
    def __call__(self,medicament):
        raise DeprecationWarning
        medicament.new_output_filename=self.new_output_filename

def set_isAgreg(A):
    u="\setcounter{isAgreg}{0}"
    A = A.replace(u,u.replace("0","1"))
    return A

def up_to_text(liste,text):
    for i,l in enumerate(liste):
        if l.startswith(text):
            return i

def is_dirty(repo):
    import pygit2
    status = repo.status()
    for filepath, flags in status.items():
        if flags != pygit2.GIT_STATUS_CURRENT:
            if flags != 16384:
                return True
    return False;

def get_hexsha(repo):
    commit=repo.revparse_single('HEAD')
    return commit.id

def set_commit_hexsha(A):
    print("set_commit_hexsha plugin")
    import pygit2
    repo=pygit2.Repository(".")
    hexsha=str(get_hexsha(repo))
    if is_dirty(repo):
        hexsha=hexsha+" -- and slighty more"
    u="\\newcommand{\GitCommitHexsha}{\info{missing information}}"
    print(hexsha)
    raise
    A = A.replace(u,u.replace("missing information",hexsha))
    return A

def ultimate_git(a=None):
    """
    Fait un git commit des fichiers automatiques, uniquement si ils sont les seuls.
    """
    # Attention : les nom de fichiers à giter ici sont aussi donnés dans le README
    import git
    repo=git.Repo("")
    if repo.is_dirty():
        automated_files=["agreg-mazhe_pytex.tex","enseignement-mazhe_pytex.tex","everything-mazhe_pytex.tex"]
        mfiles=repo.git.ls_files(m="").split("\n")
        on=True
        for f in mfiles:
            if f not in automated_files:
                on=False
        if on :
            for f in automated_files:
                repo.git.add(f)
            repo.git.commit(m="automatic")
