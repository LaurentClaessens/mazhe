# -*- coding: utf8 -*-
from sage.all import arccos
from yanntricks import *
def SpiraleLimite():
    pspict,fig = SinglePicture("SpiraleLimite")
    pspict.dilatation(3)

    x=var('x')
    curve=PolarCurve(x,arccos(x**3)/2).graph(0,1)

    pspict.axes.Dx=0.1
    pspict.axes.Dy=0.1
    pspict.axes.no_numbering()
    pspict.DrawGraphs(curve)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

