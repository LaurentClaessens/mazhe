# -*- coding: utf8 -*-
from yanntricks import *
def DynkinNUtPJx():
    pspicts,fig = MultiplePictures("DynkinNUtPJx",5)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=""
    pspicts[3].mother.caption=""
    pspicts[4].mother.caption=""

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    l=1
    h=0.5
    A=Point(0,0)
    B=Point(l,0)
    C=Point(2*l,0)
    D=Point(3*l,-h)
    E=Point(3*l,h)

    pts=[A,B,C,D,E]
    for P in pts:
        P.parameters.symbol="o"
    segs=[ Segment(A,B),Segment(B,C),Segment(C,D),Segment(C,E)  ]

    angle=[90,90,90,45,45]

    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(segs)
        psp.DrawGraphs(pts)
        P=pts[i].copy()
        P.put_mark(0.2,angle[i],"\(1\)",pspict=psp)
        P.parameters.symbol="o"
        psp.DrawGraphs(P)


    fig.conclude()
    fig.write_the_file()


