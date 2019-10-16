# -*- coding: utf8 -*-
from yanntricks import *
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

    ptO.parameters.color = "brown"
    ptO.put_mark(0.2,None,"$o=[\mtu]$",pspict=pspict)
    ptB.parameters.symbol = ""
    ptB.put_mark(0.2,0,"$[\SO(2)]$",pspict=pspict)
    #pspict.DrawBoundingBox(B)
    ptP.parameters.color = "blue"
    ptP.parameters.symbol = ""
    ptP.put_mark(0.2,None,"$[ e^{xq_0}]$",pspict=pspict)

    pspict.DrawGraphs(F)
    # See yanntricks.PspictureToOtherOutputs.specific_needs
    #pspict.specific_needs="\usepackage{bbm}\n  \usepackage{latexsym}\n\usepackage{amsfonts}\n\usepackage[reqno]{amsmath}\n\usepackage{amsthm}\n\usepackage{amssymb}\n\usepackage{amssymb}\n  \\newcommand{\mtu}{\mathbbm{1}}\n \DeclareMathOperator{\SO}{SO}"

    pspict.DrawGraphs(ptO)
    pspict.DrawGraphs(ptB)

    V.parameters.color = "cyan"
    V.put_mark(0.2,-45,"$[ e^{sE(w)} e^{xq_0}]$",pspict=pspict)

    pspict.DrawGraphs(V)
    pspict.DrawGraphs(ptP)           # Drawn after by purpose.
    #pspict.TraceBB()

    fig.conclude()
    fig.write_the_file()


