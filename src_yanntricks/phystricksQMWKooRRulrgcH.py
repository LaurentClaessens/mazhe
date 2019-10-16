# -*- coding: utf8 -*-
from yanntricks import *
def QMWKooRRulrgcH():
    pspict,fig = SinglePicture("QMWKooRRulrgcH")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    R=3
    l=1

    A=Point(-l,0)
    B=Point(l,0)
    C1=Circle(A,R)
    C2=Circle(B,R)

    O=Point(0,0)
    I=Intersection(C1,C2)[1]

    Q=Point(-0.7,1)

    I.put_mark(0.2,angle=45,added_angle=0,text="\( I\)",pspict=pspict)
    A.put_mark(0.2,angle=-90,added_angle=0,text="\( A\)",pspict=pspict)
    B.put_mark(0.2,angle=-90,added_angle=0,text="\( B\)",pspict=pspict)
    Q.put_mark(0.2,angle=90+45,added_angle=0,text="\( Q\)",pspict=pspict)
    O.put_mark(0.2,angle=-45,added_angle=0,text="\( O\)",pspict=pspict)


    pspict.DrawGraphs(A,B,O,I,C1,C2,Q)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

