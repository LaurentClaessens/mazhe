# -*- coding: utf8 -*-
from yanntricks import *
def EELKooMwkockxB():
    pspict,fig = SinglePicture("EELKooMwkockxB")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    s1=Point(0,0)
    s2=Point(8,2)
    droite=Segment(s1,s2)

    A=droite.get_point_proportion(0.2)
    B=droite.get_point_proportion(0.6)
    C=droite.get_point_proportion(0.8)
    A.put_mark(0.2,angle=None,added_angle=180,text="\( a\)",pspict=pspict)
    B.put_mark(0.2,angle=None,added_angle=180,text="\( b\)",pspict=pspict)
    C.put_mark(0.2,angle=None,added_angle=180,text="\( c\)",pspict=pspict)

    M=A+(1,3)
    M.put_mark(0.2,angle=None,added_angle=0,text="\( m\)",pspict=pspict)
    AM=Segment(A,M)

    BM=Segment(B,M)

    P=AM.get_point_proportion(0.6)
    L=Segment(C,P).dilatationF(1.3)
    Q=Intersection(BM,L)[0]

    P.put_mark(0.2,angle=None,added_angle=0,text="\( p\)",pspict=pspict)
    Q.put_mark(0.2,angle=None,added_angle=0,text="\( q\)",pspict=pspict)


    dig1=Segment(Q,A)
    dig2=Segment(P,B)
    N=Intersection(dig1,dig2)[0]
    N.put_mark(0.2,angle=None,added_angle=180,text="\( n\)",pspict=pspict)

    hauteur=Segment(M,N)
    X=Intersection(hauteur,droite)[0]
    X.put_mark(0.2,angle=droite.advised_mark_angle(),added_angle=180,text="\( x\)",pspict=pspict)
    MX=Segment(M,X)

    pspict.DrawGraphs(droite,A,B,C,X,AM,BM,P,Q,L,M,dig1,dig2,N,MX)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

