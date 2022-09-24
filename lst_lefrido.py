#!venv/bin/python3

from pytex.src import PytexTools
from pytex.src.run_me import RunMe
import commons
import plugins_agreg

from commons import has_to_be_printed


myRequest = PytexTools.Request("mesure")
myRequest.ok_hash = commons.ok_hash
myRequest.original_filename = "mazhe.tex"
myRequest.bibliography = {"json_bib": "bib_mazhe.json",
                          "template_bbl": "bbl_template.tex"
                          }

# L'ordre dans les plugin est important parce que set_<boolean>
# retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(PytexTools.accept_all_input, "options")
plugin = PytexTools.keep_script_marks(plugins_agreg.frido_mark_list)
myRequest.add_plugin(plugin, "before_pytex")


# the plugin "split_doc" should better be of type "medicament"
# because the "Traitement" object can find the toc filename
# by himself instead of hard-code it in the function.

# If you change the '4' here, you have to change it also in 'split_book.py'
myRequest.add_plugin(plugins_agreg.split_toc("frido", 4),
                     "before_compilation")

myRequest.add_plugin(plugins_agreg.set_boolean("isFrido", "true"),
                     "before_pytex")
myRequest.add_plugin(plugins_agreg.set_pdftitle("Le Frido"),
                     "before_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,
                     "after_pytex")
myRequest.add_plugin(plugins_agreg.assert_MonCerveau_first,
                     "after_compilation")
myRequest.prefix = "lefrido"

myRequest.new_output_filename = "0-lefrido.pdf"
myRequest.has_to_be_printed = has_to_be_printed

RunMe(myRequest)
