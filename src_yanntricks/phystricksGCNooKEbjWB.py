# -*- coding: utf8 -*-

from __future__ import division
from yanntricks import *


def GCNooKEbjWB():
    pspict,fig = SinglePicture("GCNooKEbjWB")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(3)

    x=var('x')
    f=phyFunction(x).graph(0,1/2)
    g=phyFunction(1.5-x).graph(1/2,1)

    A=f.get_point(0)
    B=f.get_point(1/2)
    C=g.get_point(1/2)
    D=g.get_point(1)

    lin=Segment(B,C)
    lin.parameters.style='dashed'

    B.parameters.symbol='o'

    pspict.DrawGraphs(f,g,A,B,C,D,lin)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

