# -*- coding: utf8 -*-
from phystricks import *
def DTIYKkP():
    pspict,fig = SinglePicture("DTIYKkP")
    pspict.dilatation_Y(2)

    x=var('x')
    f = phyFunction( -(x+2)**2/3+3 )
    mx = -5
    Mx = -2
    F = f.graph(mx,Mx)

    ptO = f.get_point(mx+1)
    ptB = f.get_point(Mx)
    ptP = f.get_point(-4.5)
    V = AffineVector(ptP,Point(ptP.x+2,ptP.y+0.25))

    ptO.parameters.color = "blue"
    ptO.put_mark(0.8,0,"$o=[\mtu]$")
    ptB.parameters.symbol = "none"
    ptB.put_mark(0.7,0,"$[\SO(2)]$")
    #pspict.DrawBoundingBox(B)
    ptP.parameters.color = "blue"
    ptP.parameters.symbol = "none"
    ptP.put_mark(0.7,135,"$[ e^{xq_0}]$")

    pspict.DrawGraph(F)
    # See phystricks.PspictureToOtherOutputs.specific_needs
    pspict.specific_needs="\usepackage{bbm}\n  \usepackage{latexsym}\n\usepackage{amsfonts}\n\usepackage[reqno]{amsmath}\n\usepackage{amsthm}\n\usepackage{amssymb}\n\usepackage{amssymb}\n  \\newcommand{\mtu}{\mathbbm{1}}\n \DeclareMathOperator{\SO}{SO}"

    pspict.DrawGraph(ptO)
    pspict.DrawGraph(ptB)

    V.parameters.color = "cyan"
    V.put_mark(0.5,-45,"$[ e^{sE(w)} e^{xq_0}]$")

    pspict.DrawGraph(V)
    pspict.DrawGraph(ptP)           # Drawn after by purpose.
    #pspict.TraceBB()

    fig.conclude()
    fig.write_the_file()
