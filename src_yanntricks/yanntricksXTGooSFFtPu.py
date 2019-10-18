# -*- coding: utf8 -*-
from yanntricks import *
def XTGooSFFtPu():
    pspict,fig = SinglePicture("XTGooSFFtPu")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')

    fun=phyFunction(x+1)

    f=phyFunction(x+1).graph(-5,-1)
    g=phyFunction(2*x).graph(-1,1)
    h=phyFunction(4-x).graph(1,5)

    P=g.get_point(-1)
    Q=g.get_point(1)

    P.parameters.color="blue"
    Q.parameters.color="blue"

    x1=g.inverse(1)[0]
    x2=h.inverse(1)[0]

    Z1=g.get_point(x1)
    Z2=h.get_point(x2)

    Z1.put_mark(0.2,-45,"\( Z_1\)",pspict=pspict,position="corner")
    Z2.put_mark(0.2,45,"\( Z_2\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(f,g,h,P,Q,Z1,Z2)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


