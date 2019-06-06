#! /usr/bin/python3
# -*- coding: utf8 -*-

# read a file containing lines like
#TKXZooLwXzjS
#GMIooJvcCXg
#DivergenceUn
# and prints a sequence of lines to be included in LaTeX for test.

import sys

skel="""
NAME
\\begin{center}
    \\newcommand{\CaptionFigNAME}{NAME}
    \input{auto/pictures_tex/Fig_NAME.pstricks}
\end{center}

\clearpage

"""

with open(sys.argv[1],'r') as f:
    for n in f.readlines() :
        name=n[:-1]
        print(skel.replace("NAME",name))
