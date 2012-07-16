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
myRequest.ok_filenames_list.append("Chap_limite_continue")
myRequest.ok_filenames_list.append("Emploi_limite_continue")
myRequest.ok_filenames_list.append("Chap_analyse_R")
commun.CreateBibtexFile(myRequest)
