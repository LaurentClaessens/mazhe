#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("groupes")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="modelisation.tex"

myRequest.ok_filenames_list=["e_modelisation"]
myRequest.ok_filenames_list.append("groupes")
myRequest.ok_filenames_list.append("anneauxCorps")
myRequest.ok_filenames_list.append("EspacesVecto")
