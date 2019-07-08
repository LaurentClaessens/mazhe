#! /usr/bin/python3

import sys
import os
import random
import string

from src.NoMathUtilities import SubdirectoryFilenames

def via_random(alphabet,n):
    a=""
    for k in range(0,n):
        a=a+random.choice(alphabet)
    return a

try:
    figure_name=sys.argv[1]
except IndexError:
    a=via_random(string.ascii_uppercase,4)
    b=via_random(string.ascii_letters,8)
    figure_name=a+"oo"+b

forbidden_symb=["_","1","2","3","4","5","6","7","8","9","0"]

for s in forbidden_symb :
    if s in figure_name:
        raise ValueError("You should not use '{0}' in the name.".format(s))

code_base="""# -*- coding: utf8 -*-
from phystricks import *
def XXXX():
    pspict,fig = SinglePicture("XXXX")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    x=var('x')
    P=Point(0,0)

    pspict.DrawGraphs(P)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

----------------
    pspicts,fig = MultiplePictures("XXXX",3)
    pspicts[0].mother.caption="<+caption1+>"
    pspicts[1].mother.caption="<+caption2+>"
    pspicts[2].mother.caption="<+caption3+>"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    <+Définition des objets+>

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

------------------------------

    pspicts,figs = IndependentPictures("XXXX",3)

    for psp in pspicts:
        psp.dilatation(1)

    <+Définition des objets+>

    for psp in pspicts:
        psp.DrawDefaultAxes()

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()

"""

def create_file(sfile,text):
    if not os.path.isfile(sfile.abspath()):
        with open(sfile.abspath(),"w") as f:
            f.write(text)
    else :
        print("Le fichier {} existe déjà. Je ne fais rien".format(filename))

code=code_base.replace("XXXX",figure_name)

filename=SubdirectoryFilenames("phystricks%s.py"%figure_name,"pictures_src")
pstricksfilename=SubdirectoryFilenames("Fig_{}.pstricks".format(figure_name),"pictures_tex")
pdffilename=SubdirectoryFilenames("tikzFIGLabelFig"+figure_name+"PICT"+figure_name+".pdf","pictures_tikz")
md5filename=SubdirectoryFilenames("tikzFIGLabelFig"+figure_name+"PICT"+figure_name+".md5","pictures_tikz")


for f in [filename,pstricksfilename,pdffilename]:
    create_file(f,code)
create_file(md5filename,"")

print("from phystricks{} import {}".format(figure_name,figure_name))
print("git add {} {} {} {}".format(filename.from_here(),pstricksfilename.from_here(),pdffilename.from_here(),md5filename.from_here()))
print("attach('{}');{}();exit()".format(filename.filename,figure_name)   )
