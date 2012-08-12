#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools


myRequest = LaTeXparser.PytexTools.Request("groupes")
myRequest.original_filename="mes_notes.tex"

myRequest.ok_filenames_list=["e_mes_notes"]
myRequest.ok_filenames_list.append("groupes")
myRequest.ok_filenames_list.append("liste_developpements")
