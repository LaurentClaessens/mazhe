# -*- coding: utf8 -*-
from phystricks import *
def KKLooMbjxdI():
    pspict,fig = SinglePicture("KKLooMbjxdI")
    pspict.dilatation(1)

    a=-pi/2
    b=2*pi
    x=var('x')
    f=phyFunction(sin(x)+2).graph(a,b)
    A=Point(a,0)
    B=Point(b,0)

    A.put_mark(0.2,-90,"$a$",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"$b$",automatic_place=(pspict,"N"))

    surface=SurfaceUnderFunction(f,a,b)
    surface.Isegment.parameters.style="dashed"
    surface.Fsegment.parameters.style="dashed"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="blue"
    surface.parameters.hatched()
    surface.parameters.hatch.color="red"

    pspict.DrawGraphs(A,B,surface)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
