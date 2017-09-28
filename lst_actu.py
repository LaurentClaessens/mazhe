#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools
import commons
import plugins_agreg

myRequest = latexparser.PytexTools.Request()
myRequest.ok_hash=commons.ok_hash

myRequest.add_plugin(plugins_agreg.set_isFrido,"before_pytex")
myRequest.original_filename="mazhe.tex"
myRequest.ok_filenames_list=["e_mazhe"]


myRequest.ok_filenames_list.extend(["56_EspacesVectos"])
myRequest.ok_filenames_list.extend(["55_EspacesVectos"])
myRequest.ok_filenames_list.extend(["42_nombres"])
myRequest.ok_filenames_list.extend(["53_topologie"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])

myRequest.ok_filenames_list.extend(["134_choses_finales"])
myRequest.ok_filenames_list.extend(["157_thematique"])


myRequest.new_output_filename="0-actu.pdf"
