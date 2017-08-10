#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools
import commons
import plugins_agreg

myRequest = latexparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash
myRequest.original_filename="mazhe.tex"

# L'ordre dans les plugin est important parce que set_isFrido retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(latexparser.PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(latexparser.PytexTools.keep_script_marks(plugins_agreg.frido_mark_list),"before_pytex")


# the plugin "split_doc" should better be of type "medicament"
# because the "Traitement" object can find the toc filename
# by himself instead of hard-code it in the function.
myRequest.add_plugin(plugins_agreg.split_toc(4),"before_compilation")
myRequest.add_plugin(plugins_agreg.set_boolean("isBook","true"),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,"after_pytex")
myRequest.add_plugin(plugins_agreg.assert_MonCerveau_first,"after_compilation")

myRequest.new_output_filename="0-book.pdf"

