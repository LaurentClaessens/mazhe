#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("statistiques")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="mes_notes.tex"

myRequest.ok_filenames_list=["e_mes_notes"]
#myRequest.ok_filenames_list.append("espaces_mesure")
myRequest.ok_filenames_list.append("lois_usuelles")
myRequest.ok_filenames_list.append("statistiques")
myRequest.ok_filenames_list.append("vars_al_proba")

