# -*- coding: utf8 -*-
from yanntricks import *
def HNxitLj():
    pspict,fig = SinglePicture("HNxitLj")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    pspict.specific_needs=r"\newcommand{\sA}{\mathcal{A}}\newcommand{\sH}{\mathcal{H}}"

    for pos in [  (1,0),(1,1),(1,-1),(0,1)  ]:
        P=Point(pos[0],pos[1])
        P.options.DicoOptions["dotscale"]="2"
        pspict.DrawGraphs(P)

    for pos in [  (-1,0),(-1,1),(-1,1),(-1,-1)  ]:
        P=Point(pos[0],pos[1])
        P.parameters.symbol="diamond"
        P.options.DicoOptions["dotscale"]="2"
        pspict.DrawGraphs(P)

    pspict.axes.single_axeX.put_mark(0.2,text=r"\( \sA^*_{\sH}\)",pspict=pspict,position="N")

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

