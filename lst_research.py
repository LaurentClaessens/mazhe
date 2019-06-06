# -*- coding: utf8 -*-

from pytex.src import PytexTools
import commons
import plugins_agreg

myRequest = PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash
myRequest.original_filename="mazhe.tex"

# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(PytexTools.accept_all_input,"medicament")
myRequest.add_plugin(PytexTools.keep_script_marks(plugins_agreg.research_mark_list),"before_pytex")

myRequest.new_output_filename="0-research.pdf"
