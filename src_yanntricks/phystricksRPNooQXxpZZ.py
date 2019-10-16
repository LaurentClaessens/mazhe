# -*- coding: utf8 -*-
from yanntricks import *
def RPNooQXxpZZ():
    pspict,fig = SinglePicture("RPNooQXxpZZ")
    pspict.dilatation_X(0.3)
    pspict.dilatation_Y(2)

    x=var('x')
    f=phyFunction(   (cos(x)-1)/x ).graph(-20,20)

    pspict.DrawGraphs(f)
    pspict.axes.single_axeX.axes_unit=AxesUnit(pi,'')
    pspict.axes.single_axeX.Dx=2
    pspict.axes.single_axeY.Dx=0.5
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


