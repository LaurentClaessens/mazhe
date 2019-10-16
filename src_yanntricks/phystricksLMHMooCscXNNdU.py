# -*- coding: utf8 -*-
from yanntricks import *
def LMHMooCscXNNdU():
    pspict,fig = SinglePicture("LMHMooCscXNNdU")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    x=var('x')
    mx=-5
    Mx=5
    f1=phyFunction(2+1/(x-2)).graph(mx,1)
    f2=phyFunction(1/x).graph(1,Mx)

    ass=Segment( Point(mx,2),Point(Mx,2)  )
    ass.parameters.style="dashed"

    pspict.DrawGraphs(f1,f2,ass)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

