# -*- coding: utf8 -*-
from yanntricks import *

"""
Une copie de ce fichier est dans les démonstrations de yanntricks sous le nom de PFCUoorQhitKoJ
"""

def TracerUn():
    pspicts,fig = MultiplePictures("TracerUn",4)
    pspicts[0].mother.caption=u"La fonction $y=ex$"
    pspicts[1].mother.caption=u"La fonction $y=| x |$"
    pspicts[2].mother.caption=u"La fonction $y=x^2+1$ à gauche et $(x+1)^2$ à droite."
    pspicts[3].mother.caption=u"La fonction $y=\log_2(2^{x-1})$"

    x=var('x')
    pspicts[0].dilatation(0.7)
    f1=phyFunction(2.718281*x).graph(-2,2)
    pspicts[0].DrawGraphs(f1)

    pspicts[1].dilatation(1)
    f2=phyFunction(abs(x)).graph(-2,2)
    pspicts[1].DrawGraphs(f2)

    pspicts[2].dilatation(0.7)
    f3a=phyFunction(x**2+1).graph(-2,0)
    f3b=phyFunction((x+1)**2).graph(0,2)
    pspicts[2].DrawGraphs(f3a,f3b)

    pspicts[3].dilatation(0.7)
    f4=phyFunction(x-1).graph(-2,2)
    pspicts[3].DrawGraphs(f4)

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

