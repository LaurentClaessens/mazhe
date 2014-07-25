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
myRequest.ok_filenames_list.append("e_mazhe")
myRequest.ok_filenames_list.append("part_exercices")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
myRequest.ok_filenames_list.append("<++>")
