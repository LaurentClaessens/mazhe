# -*- coding: utf8 -*-
from phystricks import *
def GVDJooYzMxLW():
    pspict,fig = SinglePicture("GVDJooYzMxLW")
    B=Point(0,0)
    C=Point(1,0)
    A=Point(0.5,0.5*sqrt(3))

    A.put_mark(0.3,90,"$A$",automatic_place=pspict)
    B.put_mark(0.3,180,"$B$",automatic_place=pspict)
    C.put_mark(0.3,0,"$C$",automatic_place=pspict)

    AB=Segment(A,B)
    AC=Segment(A,C)
    BC=Segment(C,B)

    H=BC.center()
    hauteur=Segment(A,H)
    hauteur.parameters.style="dotted"
    hauteur.parameters.color="blue"
    H.put_mark(0.3,-90,"$H$",automatic_place=pspict)

    angleS=Angle(A,C,H)
    angleT=Angle(H,A,C)
    angleS.parameters.color="red"
    angleT.parameters.color="cyan"
    angleS.put_mark(0.3,None,"$60$",automatic_place=pspict)
    angleT.put_mark(0.3,None,"$30$",automatic_place=pspict)

    pspict.DrawGraphs(AB,AC,BC,hauteur,angleS,angleT,A,B,C,H)
    pspict.dilatation(4)
    fig.conclude()
    fig.write_the_file()
