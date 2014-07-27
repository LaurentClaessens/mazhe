#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.original_filename="test_couleur.tex"
myRequest.ok_filenames_list=["e_mazhe"]
