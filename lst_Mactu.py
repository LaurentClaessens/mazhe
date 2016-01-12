#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("futur")

myRequest.original_filename="mazhe.tex"

myRequest.ok_hash=commons.ok_hash
myRequest.ok_filenames_list.append("142_CFT")
myRequest.ok_filenames_list.append("109_helga")
myRequest.ok_filenames_list.append("143_Lie_gp_and_subgp")
myRequest.ok_filenames_list.append("110_algebre")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("106_fibre_bundle")

myRequest.new_output_filename="0-Mactu.pdf"
