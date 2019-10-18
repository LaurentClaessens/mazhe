# -*- coding: utf8 -*-
from yanntricks import *
def SJAWooRDGzIkrj():
    pspict,fig = SinglePicture("SJAWooRDGzIkrj")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    O=Point(0,0)
    r=1
    Cir=Circle(O,r)
    mm=Cir.get_point(200)
    mm.put_mark(0.2,angle=None,added_angle=0,text="\( \mC\)",pspict=pspict)
    mm.parameters.symbol=""
    theta=70

    A=Cir.get_point(theta)
    B=Cir.get_point(-theta)
    A.put_mark(0.2,angle=None,added_angle=0,text="\( a\)",pspict=pspict)
    B.put_mark(0.2,angle=None,added_angle=0,text="\( b\)",pspict=pspict)

    Va=Cir.get_tangent_vector(theta)
    Vb=Cir.get_tangent_vector(-theta)

    M=Intersection(Va,Vb)[0]
    M.put_mark(0.4,angle=0,added_angle=0,text="\( m\)",pspict=pspict)

    Ta=Segment(A,M).dilatation(1.5)
    Tb=Segment(B,M).dilatation(1.5)

    X=Cir.get_point(30)
    X.put_mark(0.2,angle=None,added_angle=180,text="\( x\)",pspict=pspict)
    MX=Segment(M,X)
    C=Intersection(MX,Cir)[0]
    C.put_mark(0.2,angle=None,added_angle=0,text="\( c\)",pspict=pspict)
    MC=Segment(M,C).dilatation(1.3)

    pspict.DrawGraphs(Cir,A,B,M,Ta,Tb,X,C,MC,mm)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

