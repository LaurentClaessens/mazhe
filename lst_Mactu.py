#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons

myRequest = LaTeXparser.PytexTools.Request("futur")
#myRequest.plugin_list=[plugins_agreg.remove_parts]
myRequest.original_filename="mazhe.tex"

myRequest.ok_hash=commons.ok_hash
myRequest.ok_filenames_list.append("e_mazhe.tex")

myRequest.ok_filenames_list.append("0180_suites_series_fonctions")
