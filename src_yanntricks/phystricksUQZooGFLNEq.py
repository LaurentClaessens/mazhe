# -*- coding: utf8 -*-
from yanntricks import *
def UQZooGFLNEq():
    pspict,fig = SinglePicture("UQZooGFLNEq")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    mx=-5
    Mx=5

    x=var('x')
    f=phyFunction( arctan(x) ).graph(mx,Mx)

    seg1=Segment( Point(mx,pi/2),Point(Mx,pi/2) )
    seg2=Segment( Point(mx,-pi/2),Point(Mx,-pi/2) )

    seg1.parameters.color="red"
    seg2.parameters.color="red"
    seg1.parameters.style="dashed"
    seg2.parameters.style="dashed"

    pspict.DrawGraphs(f,seg1,seg2)
    pspict.axes.single_axeY.axes_unit=AxesUnit(pi/2,'')
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

