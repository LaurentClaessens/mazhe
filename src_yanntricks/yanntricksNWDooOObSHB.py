# -*- coding: utf8 -*-

from __future__ import division
from yanntricks import *

def NWDooOObSHB():
    pspict,fig = SinglePicture("NWDooOObSHB")
    pspict.dilatation_X(1.3)
    pspict.dilatation_Y(0.5)

    mx=-6
    Mx=5
    k=-2

    x=var('x')
    f=phyFunction((x/4)**2+x+6).graph(mx,Mx)

    surf1=SurfaceUnderFunction(f,mx,k)
    surf2=SurfaceUnderFunction(f,k,Mx)

    surf1.parameters.hatched()
    surf1.parameters.hatch.color="red"
    surf2.parameters.hatched()
    surf2.parameters.hatch.color="blue"

    a=Point(mx,0)
    b=Point(k,0)
    c=Point(Mx,0)

    a.put_mark(0.2,text="\( a\)",pspict=pspict,position="N")
    b.put_mark(0.2,text="\( b\)",pspict=pspict,position="N")
    c.put_mark(0.2,text="\( c\)",pspict=pspict,position="N")

    pspict.DrawGraphs(surf1,surf2,a,b,c)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

