# -*- coding: utf8 -*-
from yanntricks import *
def BIFooDsvVHb():
    pspict,fig = SinglePicture("BIFooDsvVHb")
    pspict.dilatation(2)

    O=Point(0,0)
    cercle=Circle(  O,1 )
    P=cercle.get_point(55)
    Y=Point(0,P.y)
    X=Point(P.x,0)

    X.put_mark(0.2,text="\( x\)",pspict=pspict,position="N")
    Y.put_mark(0.2,text="\( y\)",pspict=pspict,position="E")

    angle=AngleAOB(X,O,P)
    angle.put_mark(text="\( \\theta\)",pspict=pspict)

    seg=Segment(O,P)
    l1=Segment(P,X)
    l2=Segment(P,Y)

    l1.parameters.style="dashed"
    l2.parameters.style="dashed"

    pspict.DrawGraphs(cercle,angle,X,Y,seg,l1,l2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

