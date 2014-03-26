#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

myRequest.medicament_plugin=plugins_agreg.accept_all_input
myRequest.plugin_list=[plugins_agreg.keep_script_marks(["% SCRIPT MARK -- DECLARATIVE PART","% SCRIPT MARK -- OUTILS MATHÉMATIQUE","% SCRIPT MARK -- MATLAB","% SCRIPT MARK -- EXERCICES","% SCRIPT MARK -- FINAL"])]

myRequest.original_filename="mazhe.tex"

#myRequest.ok_filenames_list.extend(["0450_choses_finales"])
#myRequest.ok_filenames_list.extend(["0720_matlab"])
#myRequest.ok_filenames_list.extend(["<++>"])
#myRequest.ok_filenames_list.extend(["<++>"])
#myRequest.ok_filenames_list.extend(["<++>"])
#myRequest.ok_filenames_list.extend(["<++>"])
#myRequest.ok_filenames_list.extend(["Chap_exercices"])
