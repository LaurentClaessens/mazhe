# -*- coding: utf8 -*-
from yanntricks import *
def LLVMooWOkvAB():
    pspict,fig = SinglePicture("LLVMooWOkvAB")
    pspict.dilatation(3)

    x=var('x')
    f1=phyFunction(x)
    f2=phyFunction(x**2)

    surface=SurfaceBetweenFunctions(f1,f2,mx=0,Mx=1)
    surface.parameters.hatched()
    surface.parameters.color="green"
    surface.curve2.put_arrow(0.5)
    surface.curve1.put_arrow(0.5)
    surface.curve1.record_arrows[0]=-surface.curve1.record_arrows[0]

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

