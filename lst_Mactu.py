#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("futur")


mazhe_mark_list=[]
mazhe_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
mazhe_mark_list.append("% SCRIPT MARK -- GARDE MAZHE")
mazhe_mark_list.append("% SCRIPT MARK -- TOC")
mazhe_mark_list.append("% SCRIPT MARK -- ENGLISH INTRODUCTION")
mazhe_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
mazhe_mark_list.append("% SCRIPT MARK -- AGRÉGATION")
mazhe_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUE")
mazhe_mark_list.append("% SCRIPT MARK -- RESEARCH PART")
mazhe_mark_list.append("% SCRIPT MARK -- MATLAB")
mazhe_mark_list.append("% SCRIPT MARK -- EXERCICES")
mazhe_mark_list.append("% SCRIPT MARK -- FINAL")


myRequest.plugin_list=[plugins_agreg.keep_script_marks(mazhe_mark_list)]

myRequest.original_filename="mazhe.tex"

myRequest.ok_hash=commons.ok_hash
myRequest.ok_filenames_list.append("e_mazhe")
myRequest.ok_filenames_list.append("0530_Fibre_QFT")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("0450_choses_finales")
