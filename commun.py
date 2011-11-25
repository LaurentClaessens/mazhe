# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools as PytexTools

def CreateBibtexFile(myRequest):
	LaTeXparser.CreateBibtexFile("mazhe.bib","CdI1.bib",myRequest.ok_filenames_list)
