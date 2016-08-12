# -*- coding: utf8 -*-
from phystricks import *
def EJRsWXw():
    pspict,fig = SinglePicture("EJRsWXw")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    S=Point(-1,1)
    A=S+(-1,1)
    B=S+(2,2)

    trig=Polygon(S,A,B)
    trig.parameters.hatched()
    trig.parameters.hatch.color="green"

    s1=Segment(A,B)
    t1=Segment(S,A)
    t2=Segment(S,B)

    s1.parameters.color="red"
    t1.parameters.color="green"
    t2.parameters.color="green"

    pspict.DrawGraphs(trig,t1,t2,s1)
    pspict.axes.no_graduation()
    pspict.axes.single_axeX.put_mark(0.2,-90,"\( x\)",pspict=pspict,position="N")
    pspict.axes.single_axeY.put_mark(0.2,0,"\( t\)",pspict=pspict,position="W")
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
