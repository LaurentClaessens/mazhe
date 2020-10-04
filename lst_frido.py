# -*- coding: utf8 -*-

from pytex.src import PytexTools
import commons
import plugins_agreg


def print_future_reference(future_reference):
    """Print the future reference."""
    for filename in future_reference.concerned_files:
        if "front_back_matter" in filename:
            return
    future_reference.output()


myRequest = PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash
myRequest.original_filename="mazhe.tex"

# L'ordre dans les plugin est important parce que set_boolean retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(PytexTools.accept_all_input, "options")
myRequest.add_plugin(PytexTools.keep_script_marks(plugins_agreg.frido_mark_list),"before_pytex")


# the plugin "split_doc" should better be of type "medicament"
# because the "Traitement" object can find the toc filename
# by himself instead of hard-code it in the function.

# If you change the '4' here, you have to change it also in 'split_book.py'
myRequest.add_plugin(plugins_agreg.split_toc("frido",4),
                                             "before_compilation")

myRequest.add_plugin(plugins_agreg.set_boolean("isFrido","true"),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_pdftitle("Le Frido"),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,"after_pytex")
myRequest.add_plugin(plugins_agreg.assert_MonCerveau_first,"after_compilation")

myRequest.new_output_filename="0-lefrido.pdf"
myRequest.print_future_reference = print_future_reference
