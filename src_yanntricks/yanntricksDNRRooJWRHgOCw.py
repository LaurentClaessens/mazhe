# -*- coding: utf8 -*-

from __future__ import division
from yanntricks import *

def DNRRooJWRHgOCw():
    pspict,fig = SinglePicture("DNRRooJWRHgOCw")
    pspict.dilatation(2)

    C1=Point(2,0)
    C2=Point(1,0)
    C3=Point(3,0)
    r1=1
    r2=0.5
    r3=1

    Cer1=Circle(C1,r1)
    Cer2=Circle(C2,r2)
    Cer3=Circle(C3,r3)

    vps=[ Point(1,0),Point(5/2,sqrt(3)/2),Point(5/2,-sqrt(3)/2) ]
    vps[0].put_mark(0.2,angle=90+45,added_angle=0,text="\( \lambda_1\)",pspict=pspict)
    vps[1].put_mark(0.2,angle=90,added_angle=0,text="\( \lambda_2\)",pspict=pspict)
    vps[2].put_mark(0.2,angle=-90,added_angle=0,text="\( \lambda_3\)",pspict=pspict)

    pspict.DrawGraphs(Cer1,Cer2,Cer3,vps)

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

