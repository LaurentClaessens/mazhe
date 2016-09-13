# -*- coding: utf8 -*-
from phystricks import *
def TKXZooLwXzjS():
    pspict,fig = SinglePicture("TKXZooLwXzjS")
    pspict.dilatation(1)

    x,y=var('x,y')
    Fx=phyFunction(1/x)
    Fy=phyFunction(0)

    mx=1.6
    Mx=6
    my=-1
    My=1

    F=VectorField(Fx,Fy).graph(xvalues=(x,mx,Mx,7),yvalues=(y,my,My,7))

    cmx=F.pos_x[0]
    cMx=F.pos_x[2]
    rect=Rectangle( Point(cmx,My+0.2),Point(cMx,my-0.2) )
    rect.parameters.filled()
    rect.parameters.fill.color="cyan"
    rect.parameters.style="none"

    pspict.DrawGraphs(rect,F)
    fig.conclude()
    fig.write_the_file()
