#! /usr/bin/python
# -*- coding: utf8 -*-

"""
This file compiles all but the agreg part.
"""

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

# L'ordre dans les plugin est important parce que set_isAgreg retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.add_plugin(plugins_agreg.accept_all_input,"medicament")
myRequest.add_plugin(plugins_agreg.keep_script_marks(plugins_nonagreg.agreg_mark_list),"after_pytex")

myRequest.original_filename="mazhe.tex"
