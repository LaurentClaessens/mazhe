# -*- coding: utf8 -*-
from yanntricks import *
def ALIzHFm():
    pspict,fig = SinglePicture("ALIzHFm")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    cercle=Circle( Point(0,0),1 )

    alpha=60
    P=cercle.get_point(alpha)
    Q=cercle.get_point(180+alpha)

    l1=cercle.get_tangent_segment(alpha).dilatation(2.5)
    l2=cercle.get_tangent_segment(180+alpha).dilatation(2.5)

    l3=l1.translate(AffineVector(P,Point(0,0)))
    l3.parameters.style="dotted"

    P.put_mark(0.2,P.advised_mark_angle(pspict),"\( z_1\)",pspict=pspict,position="corner")
    Q.put_mark(0.2,Q.advised_mark_angle(pspict),"\( z_2\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(cercle,P,Q,l1,l2,l3)
    fig.conclude()
    fig.write_the_file()

