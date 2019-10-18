# -*- coding: utf8 -*-
from yanntricks import *
def JGuKEjH():
    pspict,fig = SinglePicture("JGuKEjH")
    pspict.dilatation(1)

    x=var('x')
    O=Point(0,0)
    r=1
    theta=50
    Cer=Circle( O,r  )

    a1=180-theta
    a2=180+theta

    P=Cer.get_point(a1)
    Q=Cer.get_point(a2)
    Z=Cer.get_point(0)

    l1=Segment(Z,P)
    l2=Segment(Z,Q)
    corde=Cer.graph(a1,a2)

    surf=CustomSurface(l1,corde,l2)
    surf.parameters.hatched()
    surf.parameters.hatch.color="lightgray"

    l1.parameters.color=surf.parameters.hatch.color
    l2.parameters.color=surf.parameters.hatch.color

    pspict.DrawGraphs(Cer,surf,Z,l1,l2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

