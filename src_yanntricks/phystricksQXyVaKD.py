# -*- coding: utf8 -*-
from yanntricks import *
def QXyVaKD():
    pspict,fig = SinglePicture("QXyVaKD")
    pspict.dilatation(2)

    C=Point(0,0.5)
    alpha=0
    circle = Circle(C,0.5)

    c1=circle.graph(-90,alpha)
    c2=circle.graph(alpha,270)
    c1.parameters.color="red"
    c2.parameters.color="blue"
    P=circle.get_point(alpha)
    P.put_mark(0.3,-45,"$P$",pspict=pspict)

    s1=Segment(Point(0,0),P)
    segment=s1.dilatation(2)
    segment.parameters.color="red"

    surface=SurfaceBetweenParametricCurves( s1,circle, interval1=(0,s1.length) , interval2=(-pi/2,radian(alpha)) )
    surface.parameters.filled()
    surface.parameters.fill.color="cyan"
    surface.parameters.color="cyan"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(c1,c2,surface,segment,P)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.comment="Area filled in cyan"
    fig.conclude()
    fig.write_the_file()

