# -*- coding: utf8 -*-
from yanntricks import *
def DynkinqlgIQl():
    pspict,fig = SinglePicture("DynkinqlgIQl")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,0)
    A.parameters.symbol="o"
    B.parameters.symbol="o"
    seg=Segment(A,B)

    B.put_mark(0.2,90,"\( 2\)",pspict=pspict)

    pspict.DrawGraphs(seg,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

