# -*- coding: utf8 -*-
from yanntricks import *
def WJBooMTAhtl():
    pspict,fig = SinglePicture("WJBooMTAhtl")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    mx=-1.5*pi
    Mx=3*pi

    x=var('x')
    f=phyFunction(cos(x)).graph(mx,Mx)

    f1=phyFunction(   f.sage.taylor(x,0,4)    ).graph(mx,Mx)
    f2=phyFunction(   f.sage.taylor(x,3*pi/4,4)    ).graph(mx,Mx)

    f.parameters.color="black"
    f1.parameters.color="red"
    f2.parameters.color="blue"

    f1.parameters.style="dashed"
    f2.parameters.style="dashed"

    f1.cut_y(-3,3)
    f2.cut_y(-3,3)

    pspict.axes.single_axeX.axes_unit=AxesUnit(pi,'')
    pspict.DrawGraphs(f,f1,f2)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

