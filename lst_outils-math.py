#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("OutilsMath")
myRequest.original_filename="OutilsMath.tex"

myRequest.ok_filenames_list=["e_OutilsMath"]
myRequest.ok_filenames_list.append("SystemeCoord")
