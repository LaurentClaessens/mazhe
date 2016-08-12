#! /usr/bin/python3
# -*- coding: utf8 -*-

import sys
import shutil

filename=sys.argv[1]
other=filename+".tmp"

print(filename)

f1 = open(filename, 'r')
f2 = open(other, 'w')
for line in f1:
    newline=line
    newline=newline.replace('automatic_place=(pspict[1],"S")','pspict=pspict[1],position="S"')
    newline=newline.replace('automatic_place=(pspict[1],"E")','pspict=pspict[1],position="E"')
    newline=newline.replace('automatic_place=(pspict[1],"N")','pspict=pspict[1],position="N"')
    newline=newline.replace('automatic_place=(pspict[1],"W")','pspict=pspict[1],position="W"')
    f2.write(newline)
f1.close()
f2.close()

shutil.copy(other,filename)
