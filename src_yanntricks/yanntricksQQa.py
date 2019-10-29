# -*- coding: utf8 -*-

from yanntricks import *
def QQa():
    pspict,fig = MultiplePictures("QQa",6)

    x=var('x')
    
    a=2
    O=Point(0,0)
    N=Point(0,a)
    S=Point(0,-a)
    W=Point(-a,0)
    E=Point(a,0)
    NE=Point(a,a)
    SW=Point(-a,-a)

    lSN=Segment(S,N)
    lWE=Segment(W,E)
    lSWNE=Segment(SW,NE)
    lOE=Segment(O,E)
    lON=Segment(O,N)
    f=phyFunction(ln(x)).graph(0.1,a)

    for el in [lSN,lWE,lSWNE,lOE,lON,f]:
        el.wave(0.1,0.07)
        el.parameters.color="red"

    pspict[0].DrawGraphs(lSN)
    pspict[1].DrawGraphs(lON)
    pspict[1].DrawGraphs(lOE)
    pspict[2].DrawGraphs(lSWNE)
    pspict[3].DrawGraphs(f)
    pspict[4].DrawGraphs(lSN,lWE)
    pspict[5].DrawGraphs(lSN,lWE)

    for i in range(len(pspict)):
        pspict[i].mother.caption=u"Exercice numéro~{0}".format(i+1)
        pspict[i].axes.no_graduation()
        pspict[i].DrawDefaultAxes()
        pspict[i].dilatation(1)

    fig.conclude()
    fig.write_the_file()

