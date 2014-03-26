#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

script_mark_list=[]
script_mark_list.append("% SCRIPT MARK -- DECLARATIVE PART")
script_mark_list.append("% SCRIPT MARK -- GARDE ENSEIGNEMENT")
script_mark_list.append("% SCRIPT MARK -- TOC")
script_mark_list.append("% SCRIPT MARK -- INTRO SAGE")
#script_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUE")
#script_mark_list.append("% SCRIPT MARK -- MATLAB")
script_mark_list.append("% SCRIPT MARK -- EXERCICES")
script_mark_list.append("% SCRIPT MARK -- FINAL")

myRequest.medicament_plugin=plugins_agreg.accept_all_input
myRequest.plugin_list=[plugins_agreg.keep_script_marks(script_mark_list)]

myRequest.original_filename="mazhe.tex"

