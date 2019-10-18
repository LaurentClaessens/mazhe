# -*- coding: utf8 -*-
from yanntricks import *
def TZCISko():
    pspict,fig = SinglePicture("TZCISko")
    pspict.dilatation_X(10)
    pspict.dilatation_Y(2)

    x=var('x')
    f=phyFunction(sin(1/x)).graph(0.01,1)
    f.linear_plotpoints=2000

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

