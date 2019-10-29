# -*- coding: utf8 -*-
from sage.all import arccos
from yanntricks import *
def GMIooJvcCXg():
    pspict,fig = SinglePicture("GMIooJvcCXg")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    g=phyFunction(arccos(x)).graph(-1,1)
    f=phyFunction(cos(x)).graph(0,pi)

    pspict.DrawGraphs(f,g)
    pspict.axes.single_axeY.axes_unit=AxesUnit(pi/2,'')
    pspict.grid.Dy=pi/2
    f.parameters.color="purple"

    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

