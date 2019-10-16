# -*- coding: utf8 -*-
from yanntricks import *
def HasseAGdfdy():
    pspict,fig = SinglePicture("HasseAGdfdy")
    pspict.dilatation(1)

    h=2
    l=2

    A=Point(0,0)
    B=Point(l,0)
    C=Point(2*l,0)

    Ap=Point(0,h)
    Bp=Point(l,h)
    Cp=Point(2*l,h)

    A.put_mark(0.2,-90,"\( \\alpha\)",pspict=pspict)
    B.put_mark(0.2,-90,"\( \\beta\)",pspict=pspict)
    C.put_mark(0.2,-90,"\( \\gamma\)",pspict=pspict)

    Ap.put_mark(0.2,90,"\( a\)",pspict=pspict)
    Bp.put_mark(0.2,90,"\( b\)",pspict=pspict)
    Cp.put_mark(0.2,90,"\( c\)",pspict=pspict)

    v1=Segment(A,Ap)
    v2=Segment(B,Bp)
    v3=Segment(C,Cp)

    d1=Segment(Ap,B)
    d2=Segment(Bp,C)
    d3=Segment(A,Cp)

    pspict.DrawGraphs(A,B,C,Ap,Bp,Cp,v1,v2,v3,d1,d2,d3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

