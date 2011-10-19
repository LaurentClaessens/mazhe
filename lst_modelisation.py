#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("modelisation")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="modelisation.tex"

myRequest.ok_filenames_list=["e_modelisation"]
myRequest.ok_filenames_list.append("espaces_mesure")
myRequest.ok_filenames_list.append("lois_usuelles")
myRequest.ok_filenames_list.append("statistiques")
