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
myRequest.ok_filenames_list.extend(["155_suites_series_fonctions"])
myRequest.ok_filenames_list.extend(["71_suites_series_fonctions"])
myRequest.ok_filenames_list.extend(["70_suites_series_fonctions"])
myRequest.ok_filenames_list.extend(["169_suites_series_fonctions"])
myRequest.ok_filenames_list.extend(["72_suites_series_fonctions"])
myRequest.ok_filenames_list.extend(["155_suites_series_fonctions"])
myRequest.ok_filenames_list.extend(["73_Chap_integrales_multiples"])
myRequest.ok_filenames_list.extend(["38_Chap_integrales_multiples"])
myRequest.ok_filenames_list.extend(["2_calcul_integral"])
myRequest.ok_filenames_list.extend(["69_Chap_calcul_differentiel"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["134_choses_finales"])


myRequest.new_output_filename="0-actu.pdf"
