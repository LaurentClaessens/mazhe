# -*- coding: utf8 -*-
from yanntricks import *
def TVXooWoKkqV():
    pspict,fig = SinglePicture("TVXooWoKkqV")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    f=LagrangePolynomial([Point(-1,-0),Point(0,0),Point(3,2),Point(6,-3)]).graph(-2,5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

