# -*- coding: utf8 -*-
from yanntricks import *
def WHCooNZAmYB():
    pspict,fig = SinglePicture("WHCooNZAmYB")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    theta=30
    R=3
    O=Point(0,0)

    cercle=Circle(O,R)
    A=cercle.get_point(theta)
    I=Point(R,0)
    B=cercle.get_point(2*theta)

    const=Circle(A, distance(A,I) )
    const.parameters.style="dashed"
    const.parameters.color="blue"

    r1=Segment(O,B)
    r2=Segment(O,I)
    r3=Segment(O,A)
    l1=Segment(B,I)

    A.put_mark(0.2,theta,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,2*theta,"\( B\)",pspict=pspict,position="corner")
    I.put_mark(0.2,-45,"\( I\)",pspict=pspict,position="corner")
    O.put_mark(0.2,text="\( O\)",pspict=pspict,position="N")

    pspict.DrawGraphs(O,B,A,I,cercle,const,r1,r2,r3,l1)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

