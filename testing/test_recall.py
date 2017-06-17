#! /usr/bin/python3
# -*- coding: utf8 -*-

# The directory passed as argument is the main directory of the
# mazhe project.
#
# So, relative to the passed argument 
# - '.pstricks' files to be checked are in `auto/pictures_tex`
# - '.recall' files to be checked against are in `src_phystricks`

import sys
import os
import importlib

# Get the directory name of 'phystricks'
pkg_loader = importlib.find_loader('phystricks')
phystricks_dir=os.path.split(pkg_loader.path)[0]

# Append to 'sys.path' the name of the directory in which is 'TestRecall.py'
test_recall_file=os.path.join(phystricks_dir,"testing/recall_tests/TestRecall.py")
sys.path.append(os.path.dirname(test_recall_file))

# Import 'TestRecall'
TestRecall = importlib.import_module("TestRecall")

directory=sys.argv[1]

pstricks_directory=os.path.join(directory,"auto/pictures_tex")
recall_directory=os.path.join(directory,"src_phystricks")

TestRecall.check_pictures(pstricks_directory,recall_directory)
