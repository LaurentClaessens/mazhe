#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import LaTeXparser
import LaTeXparser.PytexTools
import commons
import plugins_agreg

myRequest = LaTeXparser.PytexTools.Request("mesure")
myRequest.ok_hash=commons.ok_hash

myRequest.medicament_plugin=plugins_agreg.accept_all_input
# L'ordre dans les plugin est important parce que set_isAgreg retourne un code latex sans les commentaires
# alors que keep_script_marks compte dessus pour faire sa sélection.
myRequest.plugin_list=[plugins_agreg.keep_script_marks(plugins_agreg.script_mark_list),plugins_agreg.set_isAgreg]
myRequest.original_filename="mazhe.tex"
