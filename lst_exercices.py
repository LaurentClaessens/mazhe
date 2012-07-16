#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("exercices")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="GeomAnal.tex"

myRequest.ok_filenames_list=["e_GeomAnal"]
myRequest.ok_filenames_list.append("Chap_trucs_integrales")
myRequest.ok_filenames_list.extend(commun.lesExos)
commun.CreateBibtexFile(myRequest)
