# -*- coding: utf8 -*-
from yanntricks import *
def LAfWmaN():
    pspict,fig = SinglePicture("LAfWmaN")

    x=var('x')
    f1=2*x**2+4*x+2
    f2=x
    g1=sqrt(4-x**2)
    g2=x
    my=0.6
    medy=0
    My=-2
    mx=-1
    Mx=5
    v1=ParametricCurve(f1,f2).graph(My, my)
    v12=ParametricCurve(f1,f2).graph(My,medy)
    v2=ParametricCurve(g1,g2).graph(My, my)
    v22=ParametricCurve(g1,g2).graph(My, medy)
    l1=phyFunction(0.5).graph(mx,Mx)
    l2=phyFunction(-1.5).graph(mx,Mx)

    B=v1.get_point(-1.5)
    C=v2.get_point(-1.5)
    sh=Segment(B,C)
    surf=CustomSurface(v12, v22, sh)
    surf.parameters.filled()
    surf.parameters.fill.color="blue"
    pspict.DrawGraphs(v1, v2, l1, l2)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    
    fig.conclude()
    fig.write_the_file()

