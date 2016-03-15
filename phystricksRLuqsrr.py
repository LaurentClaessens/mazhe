# -*- coding: utf8 -*-
from phystricks import *
def RLuqsrr():

    def n(u,v):
        x=var('x')
        fi = u*sin(2*x)-v*cos(2*x)+v
        return fi

    pspict,fig = SinglePicture("RLuqsrr")
    pspict.dilatation(1)

    u,v,x=var('u,v,x')

    f1 = phyFunction( n(1,1) )
    f2 = phyFunction( n(0,1) )

    mx = 0
    Mx = mx+2*math.pi

    F1 = f1.graph(mx,Mx)
    F2 = f2.graph(mx,Mx)
    F1.parameters.color="red"
    F2.parameters.color="blue"
    pspict.DrawGraph(F1)
    pspict.DrawGraph(F2)

    from phystricks.MathStructures import AxesUnit
    pspict.axes.single_axeX.axes_unit=AxesUnit(pi,"")
    pspict.axes.single_axeX.Dx=0.5
    pspict.DrawDefaultAxes()


    fig.conclude()
    fig.write_the_file()
