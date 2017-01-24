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
myRequest.ok_filenames_list.extend(["179_edp"])
myRequest.ok_filenames_list.extend(["89_Equations_diff"])
myRequest.ok_filenames_list.extend(["90_Equations_diff"])
myRequest.ok_filenames_list.extend(["78_inversion_locale"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["134_choses_finales"])


myRequest.new_output_filename="0-actu.pdf"
