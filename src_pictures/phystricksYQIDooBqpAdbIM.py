# -*- coding: utf8 -*-
from phystricks import *
def YQIDooBqpAdbIM():
    pspict,fig = SinglePicture("YQIDooBqpAdbIM")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,0)
    O=Segment(A,B).midpoint()+(0,4)

    trig=Polygon(A,B,O)
    trig.put_mark(0.4,points_names="ABO",pspict=pspict)

    a1=AngleAOB(B,A,O)

    pspict.DrawGraphs(trig,a1)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
