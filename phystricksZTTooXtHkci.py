# -*- coding: utf8 -*-

from __future__ import unicode_literals

from phystricks import *
def ZTTooXtHkci():
    pspicts,fig = MultiplePictures("ZTTooXtHkci",2)
    pspicts[0].mother.caption="La région \( V\)"
    pspicts[1].mother.caption="La région \( U=\phi^{-1}(V)\)"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    A=Point(1,0)
    B=Point(2,0)
    C=Point(0,-2)
    D=Point(0,-1)

    regV=Polygon(A,B,C,D)
    regV.parameters.hatched()
    regV.parameters.hatch.color="red"

    K=Point(-2,2)
    L=Point(2,2)
    M=Point(1,1)
    N=Point(-1,1)

    regU=Polygon(K,L,M,N)
    regU.parameters.hatched()
    regU.parameters.hatch.color="blue"

    for psp in pspicts:
        psp.DrawDefaultAxes()

    pspicts[0].DrawGraphs(regV)
    pspicts[1].DrawGraphs(regU)

    fig.conclude()
    fig.write_the_file()
