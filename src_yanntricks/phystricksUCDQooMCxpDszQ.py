# -*- coding: utf8 -*-
from yanntricks import *
def UCDQooMCxpDszQ():
    pspict,fig = SinglePicture("UCDQooMCxpDszQ")
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

