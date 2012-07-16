# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools as PytexTools

def CreateBibtexFile(myRequest):
	LaTeXparser.CreateBibtexFile("mazhe.bib","GeomAnal.bib",myRequest.ok_filenames_list)

lesExos=["Chap_exercices","Emploi_exercices"]

# TODO: étant donné qu'il ne crée la bibliographie qu'à partir des éléments de ok_filenames_list, elle est mal créée lorqu'on fait --all.
