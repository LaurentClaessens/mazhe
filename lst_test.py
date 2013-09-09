#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def remove_exercice_part(A):
    #s="\part{Exercices}"
    #t="\corrChapitre{Corrigés systématiques}"
    u="\setcounter{isAgreg}{0}"
    A = A.replace(u,u.replace("0","1"))
    return A

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("mesure")
#myRequest.plugin_list=[remove_exercice_part]

#myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="mes_notes.tex"

myRequest.ok_filenames_list=["e_mes_notes","Exercices"]
