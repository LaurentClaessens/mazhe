# -*- coding: utf8 -*-
import numpy
from phystricks import *
def SBTooEasQsT():
    pspict,fig = SinglePicture("SBTooEasQsT")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.1)

    x=var('x')
    for c in numpy.linspace(-5,5,15):
        f=phyFunction(c*exp(x)).graph(-4,2)
        pspict.DrawGraphs(f)

    pspict.axes.single_axeY.Dx=10
    pspict.grid.Dy=5
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    #fig.no_figure()
    fig.conclude()
    fig.write_the_file()

