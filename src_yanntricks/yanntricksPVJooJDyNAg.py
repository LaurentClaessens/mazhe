# -*- coding: utf8 -*-
from yanntricks import *
def PVJooJDyNAg():
    pspict,fig = SinglePicture("PVJooJDyNAg")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.7)

    my=-5
    My=5

    x=var('x')
    f=phyFunction(tan(x)).graph(-5*pi/2,5*pi/2)
    f.parameters.plotpoints=1000
    f.cut_y(my,My)

    pspict.DrawGraphs(f)
    pspict.axes.single_axeX.axes_unit=AxesUnit(pi/2,'')

    for k in range(-3,3):
        seg=Segment(  Point(pi/2+k*pi,my),Point(pi/2+k*pi,My) )
        seg.parameters.style="dashed"
    pspict.DrawGraphs(seg)

    pspict.DrawDefaultAxes()
    #fig.no_figure()
    fig.conclude()
    fig.write_the_file()

