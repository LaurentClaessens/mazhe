#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("mesure")
myRequest.original_filename="test_couleur.tex"
myRequest.ok_filenames_list=["e_mazhe"]
myRequest.new_output_filename="0-test_couleur.pdf"
