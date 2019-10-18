# -*- coding: utf8 -*-
from yanntricks import *
def FGWjJBX():
    pspict,fig = SinglePicture("FGWjJBX")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,0)
    C=Point(2,0)
    D=Point(3,0)
    E=Point(4,0.5)
    F=Point(4,-0.5)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CD=Segment(C,D)
    DE=Segment(D,E)
    DF=Segment(D,F)

    BC.parameters.style='dotted'

    A.put_mark(0.2,text="\( \\alpha_1\)",pspict=pspict,position="S")
    B.put_mark(0.2,text="\( \\alpha_2\)",pspict=pspict,position="S")
    D.put_mark(0.2,text="\( \\alpha_{l-2}\)",pspict=pspict,position="S")
    E.put_mark(0.2,text="\( \\alpha_{l-1}\)",pspict=pspict,position="S")
    F.put_mark(0.2,text="\( \\alpha_l\)",pspict=pspict,position="S")

    pspict.DrawGraphs(AB,BC,CD,DE,DF,A,B,C,D,E,F)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

