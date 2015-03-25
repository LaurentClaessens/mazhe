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
script_mark_list.append("% SCRIPT MARK -- OUTILS MATHÉMATIQUE")
script_mark_list.append("% SCRIPT MARK -- MATLAB")
script_mark_list.append("% SCRIPT MARK -- EXERCICES")
script_mark_list.append("% SCRIPT MARK -- CdI")
script_mark_list.append("% SCRIPT MARK -- FINAL")

myRequest.add_plugin(LaTeXparser.PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(LaTeXparser.PytexTools.keep_script_marks(script_mark_list),"before_pytex")

myRequest.add_plugin(plugins_agreg.set_filename("0-enseignement.pdf"),"medicament")

myRequest.original_filename="mazhe.tex"

