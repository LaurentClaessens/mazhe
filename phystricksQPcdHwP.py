# -*- coding: utf8 -*-
from phystricks import *
def QPcdHwP():
    pspict,fig = SinglePicture("QPcdHwP")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,0)
    B.parameters.symbol="o"
    A.put_mark(0.2,-90,"\( \\alpha_2\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"\( \\alpha_4\)",automatic_place=(pspict,"N"))

    AB=Segment(A,B)

    AB.options.DicoOptions["doubleline"]="true"

    pspict.DrawGraphs(AB,A,B)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

