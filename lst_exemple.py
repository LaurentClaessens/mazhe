#! /usr/bin/python
# -*- coding: utf8 -*-


# Ce fichier est destiné à compiler des parties du Frido. Il sert d'exemple et il est donc suivit par Git et pas censé être modifié.
# - le copier sous le nom lst_<bla>.py
# - modifier la liste des fichiers à inclure (ok_filenames_list)
# - modifier le nom de fichier final (ici : 0-exemple.pdf).

# - compiler votre partie de Frido avec 'pytex lst_<bla>.py'

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools
import commons
import plugins_agreg

myRequest = latexparser.PytexTools.Request()
myRequest.ok_hash=commons.ok_hash

myRequest.add_plugin(plugins_agreg.set_isFrido,"before_pytex")
myRequest.original_filename="mazhe.tex"
myRequest.ok_filenames_list=["e_mazhe"]


myRequest.ok_filenames_list.extend(["81_Hilbert"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])

myRequest.ok_filenames_list.extend(["134_choses_finales"])
myRequest.ok_filenames_list.extend(["157_thematique"])


myRequest.new_output_filename="0-exemple.pdf"
