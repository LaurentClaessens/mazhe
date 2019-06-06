#! /usr/bin/python
# -*- coding: utf8 -*-

from pytex.src import PytexTools
import commons
import plugins_agreg

myRequest = PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

# L'ordre dans les plugin est important parce que set_isFrido retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(PytexTools.accept_all_input, "options")
myRequest.add_plugin(PytexTools.keep_script_marks(plugins_agreg.mazhe_mark_list),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_boolean("isGiulietta","true"),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,"after_pytex")

myRequest.new_output_filename="0-giulietta.pdf"


myRequest.original_filename="mazhe.tex"
