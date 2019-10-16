from __future__ import division
from yanntricks import *

def ExempleNonRang():
    pspict,fig = SinglePicture("ExempleNonRang")

    x=var('x')
    mx=0
    Mx=4
    f=phyFunction((x/2)**(3/2)).graph(mx,Mx)
    g=phyFunction(-(x/2)**(3/2)).graph(mx,Mx)

    pspict.axes.no_graduation()
    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

