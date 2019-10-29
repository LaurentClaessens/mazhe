# -*- coding: utf8 -*-

from __future__ import division
from yanntricks import *

def HLJooGDZnqF():
    pspict,fig = SinglePicture("HLJooGDZnqF")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f1=phyFunction(x/2).graph(-5,0)
    f2=phyFunction(3*(1-x)).graph(0,1)
    f3=phyFunction(3*x).graph(1,2)

    A=f2.get_point(0)
    B=f2.get_point(1)

    C=f1.get_point(0)
    D=f3.get_point(1)

    C.parameters.symbol='o'
    D.parameters.symbol='o'

    pspict.DrawGraphs(f1,f2,f3,A,B,C,D)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

