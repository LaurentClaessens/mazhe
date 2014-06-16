# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def QIZooQNQSJj():
    pspict,fig = SinglePicture("QIZooQNQSJj")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    x=5
    cercle=Circle(  Point(0,0),x/2)
    theta=20
    C=cercle.get_point(theta)
    B=cercle.get_point(theta+180)
    BC=Segment(B,C)
    H=BC.get_point(1)

    h=BC.orthogonal_trough(H)
    A=Intersection(h,cercle)[1]

    AH=Segment(A,H)

    triangle=Polygon(A,B,C)

    A.put_mark(0.2,theta+90,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,theta+180,"\( B\)",automatic_place=(pspict,"corner"))
    H.put_mark(0.2,theta-90,"\( H\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,theta,"\( C\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(A,B,C,cercle,H,AH,triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
