#!venv/bin/python3

from pytex.src import PytexTools
import commons
from pytex.src.run_me import RunMe
import plugins_agreg

from commons import has_to_be_printed

def print_future_reference(future_reference):
    """Print the future reference."""
    for filename in future_reference.concerned_files:
        if "front_back_matter" in filename:
            return
    future_reference.output()


myRequest = PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash
myRequest.bibliography = {"json_bib": "bib_mazhe.json",
                          "template_bbl": "bbl_template.tex"
                          }

# L'ordre dans les plugin est important parce que set_isFrido retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(PytexTools.accept_all_input, "options")
myRequest.add_plugin(PytexTools.keep_script_marks(plugins_agreg.mazhe_mark_list),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_boolean("isGiulietta","true"),"before_pytex")
myRequest.add_plugin(plugins_agreg.set_commit_hexsha,"after_pytex")

myRequest.prefix = "guilietta"
myRequest.new_output_filename="0-giulietta.pdf"

myRequest.original_filename="mazhe.tex"
myRequest.print_future_reference = print_future_reference
myRequest.has_to_be_printed = has_to_be_printed
RunMe(myRequest)
