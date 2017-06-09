#! /usr/bin/python3
# -*- coding: utf8 -*-

# The directory passed as argument is the main directory of the
# mazhe project.
#
# So, relative to the passed argument 
# - '.pstricks' files to be checked are in `auto/pictures_tex`
# - '.recall' files to be checked against are in `src_phystricks`

import sys
from TestRecall import wrong_file_list

directory=sys.argv[1]

try:
    mfl,wfl=wrong_file_list(directory)
except NotADirectoryError :
    print("[test_recall.py] the passed directory does not exist")
    raise


for f in mfl:
    print("missing recall : ",f)
for f in wfl:
    print("Wrong : ",f)

