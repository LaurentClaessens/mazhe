# -*- coding: utf8 -*-
from yanntricks import *
def OQTEoodIwAPfZE():
    pspict,fig = SinglePicture("OQTEoodIwAPfZE")
    pspict.dilatation_Y(0.1)
    pspict.dilatation(1)

    x=var("x")
    f=phyFunction(2*x**2-4*x+2-exp(-x)).graph(-4.4,5)

    pspict.DrawGraphs(f)
    pspict.axes.single_axeY.Dx=10

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

