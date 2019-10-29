# -*- coding: utf8 -*-
from yanntricks import *
def DynkinpWjUbE():
    pspict,fig = SinglePicture("DynkinpWjUbE")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,0)
    A.parameters.symbol="o"
    B.parameters.symbol="o"
    B.put_mark(0.2,90,"\( 1\)",pspict=pspict)
    seg=Segment(A,B)

    pspict.DrawGraphs(seg,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

