#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons

myRequest = LaTeXparser.PytexTools.Request("futur")
myRequest.original_filename="mazhe.tex"

myRequest.ok_hash=commons.ok_hash
myRequest.ok_filenames_list.append("e_mazhe")
myRequest.ok_filenames_list.append("TD_SVT")
myRequest.ok_filenames_list.append("0450_choses_finales")

