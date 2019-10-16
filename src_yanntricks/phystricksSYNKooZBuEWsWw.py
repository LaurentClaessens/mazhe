# -*- coding: utf8 -*-
from sage.all import sinh,cosh
from yanntricks import *
def SYNKooZBuEWsWw():
    pspict,fig = SinglePicture("SYNKooZBuEWsWw")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(0.5)

    x=var('x')
    mx=-2.5
    Mx=2.5
    f=phyFunction(sinh(x)).graph(mx,Mx)
    g=phyFunction(cosh(x)).graph(mx,Mx)
    f.parameters.color="red"

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

