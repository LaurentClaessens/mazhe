# -*- coding: utf8 -*-
from yanntricks import *
def KKLooMbjxdI():
    pspict,fig = SinglePicture("KKLooMbjxdI")
    pspict.dilatation(1)

    a=-pi/2
    b=2*pi
    x=var('x')
    f=phyFunction(sin(x)+2).graph(a,b)
    A=Point(a,0)
    B=Point(b,0)

    A.put_mark(0.2,text="$a$",pspict=pspict,position="N")
    B.put_mark(0.2,text="$b$",pspict=pspict,position="N")

    surface=SurfaceUnderFunction(f,a,b)
    surface.Isegment.parameters.style="dashed"
    surface.Fsegment.parameters.style="dashed"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="blue"
    surface.parameters.hatched()
    surface.parameters.hatch.color="red"

    pspict.DrawGraphs(A,B,surface,f)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

