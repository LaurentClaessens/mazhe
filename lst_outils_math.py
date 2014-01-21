#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def Prerequiste(medicament):
	medicament.Compil.verif=True

myRequest = LaTeXparser.PytexTools.Request("groupes")
#myRequest.prerequiste_list.append(Prerequiste)
myRequest.original_filename="outils.tex"

myRequest.ok_filenames_list=["e_mazhe"]
myRequest.ok_filenames_list.append("SystemeCoordOM")
myRequest.ok_filenames_list.append("calcul_differentiel")
myRequest.ok_filenames_list.append("plusieurs_variables")
myRequest.ok_filenames_list.append("champs_vecteurs")
myRequest.ok_filenames_list.append("curviligne")
myRequest.ok_filenames_list.append("integrales")
myRequest.ok_filenames_list.append("Stokes_et_co")
myRequest.ok_filenames_list.append("theorie_generale")
myRequest.ok_filenames_list.append("liste_exos_outils_math")
myRequest.ok_filenames_list.append("0450_choses_finales")
