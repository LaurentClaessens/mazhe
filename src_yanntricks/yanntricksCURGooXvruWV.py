# -*- coding: utf8 -*-
from yanntricks import *
def CURGooXvruWV():
    pspict,fig = SinglePicture("CURGooXvruWV")
    x=var('x')
    f1=phyFunction(2).graph(0,2)
    f2=phyFunction(x).graph(0,2)
    f1.parameters.color="green"
    f2.parameters.color="green"

    surface=SurfaceBetweenFunctions(f1,f2,0,2)
    surface.parameters.hatched()
    surface.parameters.hatch.color="green"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(surface,f1,f2)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

