# -*- coding: utf8 -*-
from yanntricks import *
def SFdgHdO():
    pspict,fig = SinglePicture("SFdgHdO")
    pspict.dilatation(1)

    x=var('x')
    f = phyFunction(sqrt(1-x**2))
    g = phyFunction(-sqrt(1-x**2))

    dx = 0.1
    dy = 0.05
    eps = 0.001

    F1 = f.graph(0+eps,1-eps)
    F2 = f.graph(-1+eps,0-eps)
    G1 = g.graph(0+eps,1-eps)
    G2 = g.graph(-1+eps,0-eps)

    F1.parameters.color = "black"
    F2.parameters.color = "green"
    G1.parameters.color = F2.parameters.color
    G2.parameters.color = F1.parameters.color
    F1.wave(dx,dy)
    F2.wave(dx,dy)
    G1.wave(dx,dy)
    G2.wave(dx,dy)

    pspict.DrawGraphs(F1)
    pspict.DrawGraphs(F2)
    pspict.DrawGraphs(G1)
    pspict.DrawGraphs(G2)

    A = Point(1,0)
    B = Point(-1,0)
    C = Point(0,1)
    D = Point(0,-1)

    A.parameters.color = "red"
    B.parameters.color = A.parameters.color
    C.parameters.color = "brown"
    D.parameters.color = C.parameters.color
    A.add_option("dotscale=1.3")
    B.add_option("dotscale=1.3")
    C.add_option("dotscale=1.3")
    D.add_option("dotscale=1.3")

    pspict.DrawGraphs(A)
    pspict.DrawGraphs(B)
    pspict.DrawGraphs(C)
    pspict.DrawGraphs(D)

    pspict.axes.no_graduation()
    pspict.axes.single_axeX.put_mark(0.3,-45,"$K_H$",pspict=pspict)
    pspict.DrawDefaultAxes()


    fig.conclude()
    fig.write_the_file()

