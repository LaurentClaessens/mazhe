#! /usr/bin/python
# -*- coding: utf8 -*-

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


myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])
myRequest.ok_filenames_list.extend(["<++>"])

myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("64_analyseR.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("64_analyseR.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("67_analyseR.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("181_espace_vecto_norme.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("181_espace_vecto_norme.tex") 
myRequest.ok_filenames_list.append("140_EspacesAffines.tex") 
myRequest.ok_filenames_list.append("175_trigono.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("140_EspacesAffines.tex") 
myRequest.ok_filenames_list.append("153_representations.tex") 
myRequest.ok_filenames_list.append("140_EspacesAffines.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("181_espace_vecto_norme.tex") 
myRequest.ok_filenames_list.append("61_representations.tex") 
myRequest.ok_filenames_list.append("181_espace_vecto_norme.tex") 

myRequest.ok_filenames_list.extend(["134_choses_finales"])
myRequest.ok_filenames_list.extend(["157_thematique"])


myRequest.new_output_filename="0-actu.pdf"
