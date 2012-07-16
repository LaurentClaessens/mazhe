#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("introdution")
myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="GeomAnal.tex"

myRequest.ok_filenames_list=["e_GeomAnal"]
myRequest.ok_filenames_list.append("introduction")
myRequest.ok_filenames_list.append("Emploi_appl_lin")
myRequest.ok_filenames_list.append("Emploi_courbes_parametre")
myRequest.ok_filenames_list.append("Emploi_exercices")
myRequest.ok_filenames_list.append("Emploi_integrales_multiples")
myRequest.ok_filenames_list.append("Emploi_calcul_differentiel")
myRequest.ok_filenames_list.append("Emploi_espace_vectoriel_norme")
myRequest.ok_filenames_list.append("Emploi_limite_continue")
commun.CreateBibtexFile(myRequest)
