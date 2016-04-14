# -*- coding: utf8 -*-
from phystricks import *
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
    angle1=Angle(X1,O,A)
    angle2=Angle(B,O,X2)

    angle1.put_mark(0.2,angle1.advised_mark_angle(pspict),"\( \pi/6\)",automatic_place=(pspict,"W"))
    angle2.put_mark(0.2,angle2.advised_mark_angle(pspict),"\( \pi/6\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(cer,seg1,seg2,A,B,angle1,angle2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

