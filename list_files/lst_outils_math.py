#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools
import commons
import plugins_agreg

myRequest = latexparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

# L'ordre dans les plugin est important parce que set_isFrido retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(latexparser.PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(latexparser.PytexTools.keep_script_marks(plugins_agreg.outilsmath_mark_list),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_isFrido,"before_pytex")

myRequest.new_output_filename="0-outils_math.pdf"

myRequest.original_filename="mazhe.tex"
