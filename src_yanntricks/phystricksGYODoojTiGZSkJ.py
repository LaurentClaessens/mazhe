# -*- coding: utf8 -*-
from yanntricks import *
def GYODoojTiGZSkJ():
    pspict,fig = SinglePicture("GYODoojTiGZSkJ")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(6,4)

    trig=Polygon(A,B,C)
    trig.put_mark(0.3,pspict=pspict)

    P=Segment(B,C).get_point_proportion(0.6)
    N=Segment(A,P).get_point_proportion(0.8)

    P.put_mark(0.2,angle=None,added_angle=180,text="\( P\)",pspict=pspict)
    N.put_mark(0.2,angle=None,added_angle=180,text="\( N\)",pspict=pspict)

    AP=Segment(A,P)

    pspict.DrawGraphs(trig,AP,N,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

