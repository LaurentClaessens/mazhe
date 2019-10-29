# -*- coding: utf8 -*-
from yanntricks import *
def RQsQKTl():
    pspict,fig = SinglePicture("RQsQKTl")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,0)
    A.parameters.symbol="o"
    B.parameters.symbol="o"
    A.put_mark(0.2,text="\( 1\)",pspict=pspict,position="S")

    l=Segment(A,B)

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

