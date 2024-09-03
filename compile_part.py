#!venv/bin/python3

import sys
import datetime
from pathlib import Path

from pytex.src import PytexTools
from pytex.src.run_me import RunMe
from pytex.src.utilities import read_json_file
import commons
import plugins_agreg

from commons import has_to_be_printed


def print_future_reference(future_reference):
    """Print the future reference."""
    for filename in future_reference.concerned_files:
        if "front_back_matter" in filename:
            return
    future_reference.output()


config = read_json_file(sys.argv[1])
pdf_title = config["pdf_title"]

myRequest = PytexTools.Request()
myRequest.ok_hash = commons.ok_hash
myRequest.bibliography = config["bibliography"]
myRequest.prefix = pdf_title
myRequest.original_filename = Path('.').resolve() / "mazhe.tex"

is_frido_part: bool = config.get("is_frido_part", False)
is_giulietta_part: bool = config.get("is_giulietta_part", False)

bools: dict[str, bool] = config.get("bools", {})
is_giulietta: bool = bools.get("is_giulietta", False)
is_frido: bool = bools.get("is_frido", False)
is_book: bool = bools.get("is_book", False)

title_plugin = plugins_agreg.set_pdftitle(pdf_title)

if is_frido_part:
    frido_plugin = plugins_agreg.set_boolean("isFrido", 'true')
    giulietta_plugin = plugins_agreg.set_boolean("isGiulietta", 'false')
    myRequest.add_plugin(frido_plugin, "before_pytex")
    myRequest.add_plugin(giulietta_plugin, "before_pytex")
    myRequest.add_plugin(title_plugin, "before_pytex")

if is_giulietta_part:
    frido_plugin = plugins_agreg.set_boolean("isFrido", 'false')
    giulietta_plugin = plugins_agreg.set_boolean("isGiulietta", 'true')
    myRequest.add_plugin(frido_plugin, "before_pytex")
    myRequest.add_plugin(giulietta_plugin, "before_pytex")
    myRequest.add_plugin(title_plugin, "before_pytex")

if is_frido:
    n_volumes = config["n_volumes"]
    project_name = config["project_name"]
    split_toc_plug = plugins_agreg.split_toc(project_name, n_volumes)
    is_frido_plug = plugins_agreg.set_boolean("isFrido", "true")
    pdf_title_plug = plugins_agreg.set_pdftitle("Le Frido")
    commit_hexa_plug = plugins_agreg.set_commit_hexsha
    mon_cerveau_first_plug = plugins_agreg.assert_MonCerveau_first
    frido_mark_list = plugins_agreg.frido_mark_list
    frido_mark_plug = PytexTools.keep_script_marks(frido_mark_list)
    myRequest.add_plugin(split_toc_plug, "before_compilation")
    myRequest.add_plugin(is_frido_plug, "before_pytex")
    myRequest.add_plugin(pdf_title_plug, "before_pytex")
    myRequest.add_plugin(commit_hexa_plug, "after_pytex")
    myRequest.add_plugin(mon_cerveau_first_plug, "after_compilation")
    myRequest.add_plugin(PytexTools.accept_all_input, "options")
    myRequest.add_plugin(frido_mark_plug, "before_pytex")

if is_book:
    current_year = datetime.datetime.now().year
    myRequest.prefix = str(current_year)
    n_volumes = config["n_volumes"]
    project_name = config["project_name"]
    split_toc_plug = plugins_agreg.split_toc(project_name, n_volumes)
    is_book_plug = plugins_agreg.set_boolean("isBook", "true")
    pdf_title_plug = plugins_agreg.set_pdftitle("Le Frido")
    commit_hexa_plug = plugins_agreg.set_commit_hexsha
    mon_cerveau_first_plug = plugins_agreg.assert_MonCerveau_first
    book_mark_list = plugins_agreg.book_mark_list
    book_mark_plug = PytexTools.keep_script_marks(book_mark_list)
    myRequest.add_plugin(split_toc_plug, "before_compilation")
    myRequest.add_plugin(is_book_plug, "before_pytex")
    myRequest.add_plugin(pdf_title_plug, "before_pytex")
    myRequest.add_plugin(commit_hexa_plug, "after_pytex")
    myRequest.add_plugin(mon_cerveau_first_plug, "after_compilation")
    myRequest.add_plugin(PytexTools.accept_all_input, "options")
    myRequest.add_plugin(book_mark_plug, "before_pytex")


if is_giulietta:
    giu_mark_list = plugins_agreg.mazhe_mark_list
    giu_mark_plug = PytexTools.keep_script_marks(giu_mark_list)
    is_giulietta_plug = plugins_agreg.set_boolean("isGiulietta", "true")
    myRequest.add_plugin(plugins_agreg.set_commit_hexsha, "after_pytex")
    myRequest.add_plugin(PytexTools.accept_all_input, "options")
    myRequest.add_plugin(giu_mark_plug, "before_pytex")
    myRequest.add_plugin(is_giulietta_plug, "before_pytex")


myRequest.ok_filenames_list = ["e_mazhe"]

ok_filenames = config.get("tex_files", [])
ok_filenames.append("157_thematique")
ok_filenames.append("134_choses_finales")

myRequest.ok_filenames_list = ok_filenames

myRequest.new_output_filename = f"0-{pdf_title}.pdf"
myRequest.has_to_be_printed = has_to_be_printed
myRequest.print_future_reference = print_future_reference

RunMe(myRequest)
