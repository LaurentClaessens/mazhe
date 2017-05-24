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

directory=sys.argv[0]

for f in wrong_file_list(directory):
    print("Wrong : ",f)

