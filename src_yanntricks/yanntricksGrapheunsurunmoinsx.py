# -*- coding: utf8 -*-
from yanntricks import *

def Grapheunsurunmoinsx():
    pspict,fig = SinglePicture("Grapheunsurunmoinsx")
    
    x=var('x')
    f=phyFunction(1/(1-x))
    eps=0.21
    l=5
    f1=f.graph(1-l,1-eps)
    f2=f.graph(1+eps,1+l)
    f1.parameters.color="red"
    Ass=Segment( Point(1,f(1+eps)),Point(1,f(1-eps)) )
    Ass.parameters.style="dotted"

    pspict.DrawGraphs(f1,f2,Ass)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

