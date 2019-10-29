# -*- coding: utf8 -*-
from yanntricks import *
def XJMooCQTlNL():
    pspict,fig = SinglePicture("XJMooCQTlNL")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(x*ln(abs(x))).graph(-3,3)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

