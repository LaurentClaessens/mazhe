#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("integrales_multiples")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="GeomAnal.tex"

myRequest.ok_filenames_list=["e_GeomAnal"]
myRequest.ok_filenames_list.append("Chap_trucs_integrales")
myRequest.ok_filenames_list.append("Chap_analyse_R")
myRequest.ok_filenames_list.append("Chap_autres")
myRequest.ok_filenames_list.append("Chap_espaces_vectoriels")
commun.CreateBibtexFile(myRequest)
