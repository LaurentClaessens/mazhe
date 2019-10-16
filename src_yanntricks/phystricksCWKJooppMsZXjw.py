# -*- coding: utf8 -*-
from yanntricks import *
def CWKJooppMsZXjw():
    pspict,fig = SinglePicture("CWKJooppMsZXjw")
    pspict.dilatation(1)

    a=-3
    b=-1
    O=Point(0,0)
    X=Point(1,0)
    Z=Point(a,b)
    Z.put_mark(0.2,angle=None,added_angle=0,text="\( -x+\lambda i\)",pspict=pspict)

    P=Point(a,0)
    v=AffineVector(Z,P)
    seg=Segment( O,Z  )

    ang=AngleAOB(Z,O,X)
    ang.put_mark(0.5,angle=None,added_angle=0,text="\( \\arg(z)\)",pspict=pspict)

    pspict.DrawGraphs(v,seg,Z,ang)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

