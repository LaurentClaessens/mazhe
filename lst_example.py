"""
This is an example file for compiling only parts of Giulietta.
This file is not intended to be changed since it is git-tracked as
example.

- copy this file with another name, say `lst_foobar.py`.
- Modify the list of files to be included in your example: 
  add/remove files in `ok_filenames`.
- Change the `pdf` exit filename: `new_output_filename`.
- Compile `pytex lst_foobar.py`.
"""

from pytex.src import PytexTools
import commons
import plugins_agreg

myRequest = PytexTools.Request()
myRequest.ok_hash=commons.ok_hash

myRequest.add_plugin(plugins_agreg.set_pdftitle("example"),"before_pytex")

myRequest.original_filename="mazhe.tex"

myRequest.ok_filenames_list=["e_mazhe"]


myRequest.ok_filenames_list.append("108_mazhe.tex") 
myRequest.ok_filenames_list.extend(["117_Fibre_QFT"])

myRequest.ok_filenames_list.extend(["157_thematique"])
myRequest.ok_filenames_list.extend(["134_choses_finales"])


myRequest.new_output_filename="0-example.pdf"
