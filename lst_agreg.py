#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

def remove_exercice_part(A):
    #s="\part{Exercices}"
    #t="\corrChapitre{Corrigés systématiques}"
    u="\setcounter{isAgreg}{0}"
    return A.replace(u,u.replace("0","1"))

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.plugin_list=[remove_exercice_part]
myRequest.original_filename="mes_notes.tex"

myRequest.ok_filenames_list=["e_mes_notes"]
myRequest.ok_filenames_list.append("questionsMesNotes")
myRequest.ok_filenames_list.append("gardeMesNotes")
myRequest.ok_filenames_list.append("groupes")
myRequest.ok_filenames_list.append("topologie")
myRequest.ok_filenames_list.append("StructAnneaux")
myRequest.ok_filenames_list.append("StructCorps")
myRequest.ok_filenames_list.append("VectoMatrice")
myRequest.ok_filenames_list.append("EspacesVecto")
myRequest.ok_filenames_list.append("EspacesAffines")
myRequest.ok_filenames_list.append("EspacesProjectifs")
myRequest.ok_filenames_list.append("representations")
myRequest.ok_filenames_list.append("Chap_analyse_R")
myRequest.ok_filenames_list.append("DeEcha")
myRequest.ok_filenames_list.append("Chap_calcul_differentiel")
myRequest.ok_filenames_list.append("Chap_courbes_parametre")
myRequest.ok_filenames_list.append("Chap_integrales_multiples")
myRequest.ok_filenames_list.append("espaces_mesure")
myRequest.ok_filenames_list.append("suites_series_fonctions")
myRequest.ok_filenames_list.append("Series_entieres")
myRequest.ok_filenames_list.append("pts_fixes")
myRequest.ok_filenames_list.append("Brouwer")
myRequest.ok_filenames_list.append("astuces")
myRequest.ok_filenames_list.append("Chap_trucs_integrales")
myRequest.ok_filenames_list.append("fautes")
myRequest.ok_filenames_list.append("analyse_fonctionnelle")
myRequest.ok_filenames_list.append("AnalyseComplexe")
myRequest.ok_filenames_list.append("Equations_diff")
myRequest.ok_filenames_list.append("theorie")
myRequest.ok_filenames_list.append("Hilbert")
myRequest.ok_filenames_list.append("Hilbert_Fourier")
myRequest.ok_filenames_list.append("vars_al_proba")
myRequest.ok_filenames_list.append("lois_usuelles")
myRequest.ok_filenames_list.append("statistiques")
myRequest.ok_filenames_list.append("Markov")
myRequest.ok_filenames_list.append("Chafai")
myRequest.ok_filenames_list.append("SystemeCoordOM")
myRequest.ok_filenames_list.append("calcul_differentiel")
myRequest.ok_filenames_list.append("plusieurs_variables")
myRequest.ok_filenames_list.append("champs_vecteurs")
myRequest.ok_filenames_list.append("curviligne")
myRequest.ok_filenames_list.append("integrales")
myRequest.ok_filenames_list.append("Stockes_et_co")
myRequest.ok_filenames_list.append("theorie_generale")
myRequest.ok_filenames_list.append("ExercicesAgreg")
myRequest.ok_filenames_list.append("liste_developpements")

myRequest.refute_linenames_list=["Exercices"]
