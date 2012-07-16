#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("limite_continue")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="GeomAnal.tex"

myRequest.ok_filenames_list=["e_GeomAnal"]
myRequest.ok_filenames_list.append("Chap_courbes_parametre")
myRequest.ok_filenames_list.append("Emploi_courbes_parametre")
#myRequest.ok_filenames_list.append("listeExercices")
commun.CreateBibtexFile(myRequest)
