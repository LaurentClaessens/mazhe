# -*- coding: utf8 -*-
from yanntricks import *
def JOQVoolPTsYPZK():
    pspict,fig = SinglePicture("JOQVoolPTsYPZK")
    pspict.dilatation(2)

    S1 = Circle( Point(0,0), 1 )

    theta = 45

    B = S1.copy()

    B.angleI = -theta
    B.angleF = theta
    B.parameters.color = 'cyan'

    P = S1.get_point(0)
    P.put_mark(0.2,angle=None,added_angle=0,text="\( 1\)",pspict=pspict)

    Q1 = S1.get_point(-theta)
    Q2 = S1.get_point(theta)

    line = Segment(Q1, Q2).dilatation(1.5)
    line.parameters.style = 'dotted'

    pspict.DrawGraphs(S1, B, P, Q1, Q2, line)
    #fig.no_figure()
    fig.conclude()
    fig.write_the_file()
