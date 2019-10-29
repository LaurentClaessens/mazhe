# -*- coding: utf8 -*-
from yanntricks import *
def QPcdHwP():
    pspict,fig = SinglePicture("QPcdHwP")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,0)
    B.parameters.symbol="o"
    A.put_mark(0.2,text="\( \\alpha_2\)",pspict=pspict,position="N")
    B.put_mark(0.2,text="\( \\alpha_4\)",pspict=pspict,position="N")

    AB=Segment(A,B)

    AB.options.DicoOptions["doubleline"]="true"

    pspict.DrawGraphs(AB,A,B)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


