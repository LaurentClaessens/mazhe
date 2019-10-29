# -*- coding: utf8 -*-
from yanntricks import *
def JSLooFJWXtB():
    pspict,fig = SinglePicture("JSLooFJWXtB")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    mx=-1.5*pi
    Mx=1.5*pi
    f=phyFunction(sin(x)).graph(mx,Mx)
    g=phyFunction(0).graph(mx,Mx)

    pts=Intersection(f,g,mx,Mx,numerical=True)

    xx=[mx]
    xx.extend([P.x for P in pts])
    xx.append(Mx)

    for i in range(len(xx)-1):
        a=xx[i]
        b=xx[i+1]
        surf=SurfaceUnderFunction(f,a,b)
        surf.parameters.hatched()
        surf.parameters.hatch.color='red'
        if i%2==0 :
            surf.parameters.hatch.color='blue'
    pspict.DrawGraphs(surf)

    pspict.DrawGraphs(f)
    pspict.axes.single_axeX.axes_unit=AxesUnit(pi/2,'')
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


