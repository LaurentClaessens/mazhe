#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools


def Prerequiste(medicament):
	medicament.Sortie.pdf=True
	medicament.Compil.tout=True

myRequest = LaTeXparser.PytexTools.Request("MesEssais")
myRequest.prerequiste_list.append(Prerequiste)

myRequest.original_filename="essais.tex"

myRequest.ok_filenames_list=[]
#myRequest.ok_filenames_list.append("<++>")
