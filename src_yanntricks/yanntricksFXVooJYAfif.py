# -*- coding: utf8 -*-
from yanntricks import *
def FXVooJYAfif():
    pspict,fig = SinglePicture("FXVooJYAfif")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    mx=-4
    Mx=4

    x=var('x')
    f=phyFunction(2*arctan(x)/pi).graph(mx,Mx)

    s1=Segment( Point(mx,1),Point(Mx,1) )
    s2=Segment( Point(mx,-1),Point(Mx,-1) )

    s1.parameters.color="red"
    s2.parameters.color="red"

    pspict.DrawGraphs(f,s1,s2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

