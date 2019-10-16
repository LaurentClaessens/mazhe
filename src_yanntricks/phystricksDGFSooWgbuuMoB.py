# -*- coding: utf8 -*-

from __future__ import division
from yanntricks import *

def DGFSooWgbuuMoB():
    pspict,fig = SinglePicture("DGFSooWgbuuMoB")
    pspict.dilatation_X(5)

    N=3
    h=1/(N+1)
    x=var('x')
    f1=phyFunction((N+1)*x).graph(0,h)
    f2=phyFunction(-(N+1)*x+2).graph(h,2*h)
    f3=phyFunction((N+1)*x-1).graph(h,2*h)
    f4=phyFunction(-(N+1)*x+3).graph(2*h,3*h)

    f3.parameters.style="dashed"
    f4.parameters=f3.parameters

    pspict.DrawGraphs(f1,f2,f3,f4)

    pspict.axes.no_numbering()
    pspict.axes.single_axeX.Dx=h

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

