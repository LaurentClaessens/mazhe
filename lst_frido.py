#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools
import commons
import plugins_agreg

myRequest = latexparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

# L'ordre dans les plugin est important parce que set_boolean retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(latexparser.PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(latexparser.PytexTools.keep_script_marks(plugins_agreg.agreg_mark_list),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_boolean("isFrido","true"),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,"after_pytex")
myRequest.add_plugin(plugins_agreg.assert_MonCerveau_first,"after_compilation")
myRequest.add_plugin(plugins_agreg.check_recall,"before_compilation")

myRequest.new_output_filename="0-lefrido.pdf"

myRequest.original_filename="mazhe.tex"
