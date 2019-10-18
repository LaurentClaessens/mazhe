# -*- coding: utf8 -*-
from yanntricks import *
def YHJYooTEXLLn():
    pspict,fig = SinglePicture("YHJYooTEXLLn")
    h=3
    R=2
    x=var('x')
    f=phyFunction((SR(h)/R)*x).graph(0,R)

    pspict.axes.single_axeX.axes_unit=AxesUnit(R,"R")
    pspict.axes.single_axeY.axes_unit=AxesUnit(h,"h")

    P=Point(R,h)
    P.put_mark(0.1,45,"$(R,h)$",pspict=pspict)

    angle = AngleAOB(Point(1,0),Point(0,0),P)
    angle.parameters.color="red"
    angle.put_mark(0.3,None,"$\\alpha$",pspict=pspict)

    pspict.DrawGraphs(f,P,angle)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

