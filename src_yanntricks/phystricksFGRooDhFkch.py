# -*- coding: utf8 -*-
from sage.all import arcsin
from yanntricks import *
def FGRooDhFkch():
    pspict,fig = SinglePicture("FGRooDhFkch")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(arcsin(x)).graph(-1,1)

    pspict.DrawGraphs(f)
    pspict.axes.single_axeY.axes_unit=AxesUnit(pi/2,'')
    pspict.grid.Dy=pi/2

    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    #fig.no_figure()
    fig.conclude()
    fig.write_the_file()

