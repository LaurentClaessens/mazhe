# -*- coding: utf8 -*-
from yanntricks import *
def CELooGVvzMc():
    pspict,fig = SinglePicture("CELooGVvzMc")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')

    mx=0
    Mx=2.3

    O=Point(0,0)

    f=phyFunction(x**2).graph(mx,Mx)
    g=phyFunction(sqrt(x)).graph(0,f(Mx))

    F=Point(  f.Mx,f(f.Mx)  )
    G=Point(  g.Mx,g(g.Mx)  )
    seg=Segment(  O,Segment(F,G).midpoint()  )
    seg.parameters.style="dashed"

    pspict.DrawGraphs(f,g,seg)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

