# -*- coding: utf8 -*-
from yanntricks import *
def ZOCNoowrfvQXsr():
    pspict,fig = SinglePicture("ZOCNoowrfvQXsr")
    pspict.dilatation(1)

    mx=-3
    h1=1
    h2=2
    P1=Point(0,h1)
    P2=Point(0,h2)
    l1=Segment( Point(mx,h1),P1 )
    l2=Segment( Point(-mx,h2),P2+(0.07,0) )

    P2.parameters.symbol="o"

    pspict.DrawGraphs(l1,l2,P1,P2)
    pspict.axes.no_numbering()
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

