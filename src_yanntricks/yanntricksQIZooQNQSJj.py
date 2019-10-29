# -*- coding: utf8 -*-

from __future__ import division

from yanntricks import *
def QIZooQNQSJj():
    pspict,fig = SinglePicture("QIZooQNQSJj")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    x=5
    cercle=Circle(  Point(0,0),x/2)
    theta=20
    C=cercle.get_point(theta)
    B=cercle.get_point(theta+180)
    BC=Segment(C,B)
    H=BC.get_point_proportion(0.7)

    h=BC.orthogonal_trough(H)
    A=Intersection(h,cercle)[0]


    AH=Segment(A,H)
    rh=RightAngle(AH,BC,0,0)


    triangle=Polygon(A,B,C)

    A.put_mark(0.2,theta+90,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,theta+180,"\( B\)",pspict=pspict,position="corner")
    H.put_mark(0.2,theta-90,"\( H\)",pspict=pspict,position="corner")
    C.put_mark(0.2,theta,"\( C\)",pspict=pspict,position="corner")

    no_symbol(triangle.vertices,H)

    pspict.DrawGraphs(A,B,C,cercle,H,AH,triangle,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

