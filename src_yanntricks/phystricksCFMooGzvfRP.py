# -*- coding: utf8 -*-
from yanntricks import *
def CFMooGzvfRP():
    pspict,fig = SinglePicture("CFMooGzvfRP")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(2)

    x=var('x')
    angle=degree(pi/6)
    O=Point(0,0)
    cer=Circle(   O,1 )

    A=cer.get_point(angle)
    B=cer.get_point(180-angle)

    seg1=Segment(O,A)
    seg2=Segment(O,B)

    X1=cer.get_point(0)
    X2=cer.get_point(180)
    angle1=AngleAOB(X1,O,A)
    angle2=AngleAOB(B,O,X2)

    angle1.put_mark(text="\( \pi/6\)",pspict=pspict)
    angle2.put_mark(text="\( \pi/6\)",pspict=pspict)

    pspict.DrawGraphs(cer,seg1,seg2,A,B,angle1,angle2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.comment="Regarder si les marques des angles sont correctes."
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


