#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def remove_exercice_part(A):
    u="\setcounter{isAgreg}{0}"
    A = A.replace(u,u.replace("0","1"))
    return A

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.plugin_list=[remove_exercice_part]
myRequest.original_filename="mes_notes.tex"

myRequest.ok_filenames_list=["e_mes_notes"]
myRequest.ok_filenames_list.append("liste_developpements")

myRequest.ok_filenames_list.append("gardeMesNotes")
myRequest.ok_filenames_list.append("questionsMesNotes")
myRequest.ok_filenames_list.append("introAgreg")
myRequest.ok_filenames_list.append("0010_groupes")
myRequest.ok_filenames_list.append("0015_groupes")
myRequest.ok_filenames_list.append("0020_StructAnneaux")
myRequest.ok_filenames_list.append("0030_StructCorps")
myRequest.ok_filenames_list.append("0035_StructCorps")
myRequest.ok_filenames_list.append("0036_StructCorps")
myRequest.ok_filenames_list.append("0040_topologieR")
myRequest.ok_filenames_list.append("topologie")
myRequest.ok_filenames_list.append("EspacesAffines")
myRequest.ok_filenames_list.append("007_espace_vecto_norme")
myRequest.ok_filenames_list.append("0080_VectoMatrice")
myRequest.ok_filenames_list.append("0085_VectoMatrice")
myRequest.ok_filenames_list.append("0087_VectoMatrice")
myRequest.ok_filenames_list.append("0090_EspacesVecto")
myRequest.ok_filenames_list.append("0095_EspacesVecto")
myRequest.ok_filenames_list.append("0100_representations")
myRequest.ok_filenames_list.append("EspacesProjectifs")
myRequest.ok_filenames_list.append("0130_Chap_analyse_R")
myRequest.ok_filenames_list.append("0140_Chap_calcul_differentiel")
myRequest.ok_filenames_list.append("0145_Chap_courbes_parametre")
myRequest.ok_filenames_list.append("0143_Chap_calcul_differentiel")
myRequest.ok_filenames_list.append("Chap_courbes_parametre")
myRequest.ok_filenames_list.append("0170_Chap_integrales_multiples")
myRequest.ok_filenames_list.append("0175_Chap_integrales_multiples")
myRequest.ok_filenames_list.append("0180_suites_series_fonctions")
myRequest.ok_filenames_list.append("0185_Series_entieres")
myRequest.ok_filenames_list.append("0190_pts_fixes")
myRequest.ok_filenames_list.append("0200_Brouwer")
myRequest.ok_filenames_list.append("astuces")
myRequest.ok_filenames_list.append("0230_Hilbert")
myRequest.ok_filenames_list.append("0240_analyse_fonctionnelle")
myRequest.ok_filenames_list.append("0250_AnalyseComplexe")
myRequest.ok_filenames_list.append("0255_AnalyseComplexe")
myRequest.ok_filenames_list.append("0260_Fourier")
myRequest.ok_filenames_list.append("0265_Fourier")
myRequest.ok_filenames_list.append("0270_Equations_diff")
myRequest.ok_filenames_list.append("theorie")
myRequest.ok_filenames_list.append("0290_vars_al")
myRequest.ok_filenames_list.append("0295_vars_al")
myRequest.ok_filenames_list.append("0297_vars_al")
myRequest.ok_filenames_list.append("0300_statistiques")
myRequest.ok_filenames_list.append("0310_Markov")
myRequest.ok_filenames_list.append("Science")
myRequest.ok_filenames_list.append("liste_developpements")
myRequest.ok_filenames_list.append("SystemeCoordOM")
myRequest.ok_filenames_list.append("calcul_differentiel")
myRequest.ok_filenames_list.append("plusieurs_variables")
myRequest.ok_filenames_list.append("champs_vecteurs")
myRequest.ok_filenames_list.append("curviligne")
myRequest.ok_filenames_list.append("integrales")
myRequest.ok_filenames_list.append("Stokes_et_co")
myRequest.ok_filenames_list.append("theorie_generale")
myRequest.ok_filenames_list.append("ExercicesAgreg")

myRequest.refute_linenames_list=["Exercices"]
