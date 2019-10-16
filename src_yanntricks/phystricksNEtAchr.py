# -*- coding: utf8 -*-
from yanntricks import *
def NEtAchr():
    pspict,fig = SinglePicture("NEtAchr")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    pts=[Point(  c[0],c[1]  ) for c in[ (-1.5,-0.5),(0.5,-0.3),(2,1),(3.5,1.5),(5,2.7),(5.8,2.7)]]
    for P in pts:
        P.put_mark(0.2,text="\( +\)",pspict=pspict,position="S")

    curve=InterpolationCurve(pts)

    pspict.DrawGraphs(curve,pts)
    fig.conclude()
    fig.write_the_file()

