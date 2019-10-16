# -*- coding: utf8 -*-
from yanntricks import *
def UZGooBzlYxr():
    pspict,fig = SinglePicture("UZGooBzlYxr")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')

    cercle=Circle(   Point(0,0),3  )
    d1=Segment( Point(-1,1),Point(4,1) )
    d2=phyFunction(3-x).graph(-1,4)
    K=Point(0,3)
    A=Intersection( d1,d2  )[0]
    B=Intersection(  cercle,d1  )[1]
    
    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")

    t1=B.polar_coordinates().degree
    arc=cercle.graph(t1,90)

    arc.parameters.color="blue"

    surf=CustomSurface(arc, Segment(K,A),Segment(A,B) )
    surf.parameters.filled()
    surf.parameters.fill.color="lightgray"

    pspict.DrawGraphs(surf,cercle,A,B,d1,d2)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

