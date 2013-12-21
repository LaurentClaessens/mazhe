# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

c=0.5
def small_box(X,Y,text=""):
    x=c*X
    y=c*Y
    A=Point(x-c/2,y-c/2)
    B=Point(x+c/2,y-c/2)
    C=Point(x+c/2,y+c/2)
    D=Point(x-c/2,y+c/2)
    P=Point(x,y)
    P.put_mark(0.0,0,text)
    P.parameters.symbol="none"
    return [P,Polygon(A,B,C,D)]

def GBnUivi():
    pspict,fig = SinglePicture("GBnUivi")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Q=[]
    Q.append( small_box(0,2,"1") )
    Q.append( small_box(1,2,"2") )
    Q.append( small_box(2,2,"3") )
    Q.append( small_box(3,2,"4") )
    Q.append( small_box(4,2,"7") )
    Q.append( small_box(5,2,"8") )
    Q.append( small_box(0,1,"3") )
    Q.append( small_box(1,1,"5") )
    Q.append( small_box(2,1,"6") )
    Q.append( small_box(3,1,"9") )
    Q.append( small_box(0,0,"10") )

    for q in Q :
        pspict.DrawGraphs(q[0],q[1])
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def IYAvSvI():
    pspict,fig = SinglePicture("IYAvSvI")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Q=[]
    Q.append( small_box(0,1,"1") )
    Q.append( small_box(1,1,"3") )
    Q.append( small_box(0,0,"2") )
    Q.append( small_box(1,0,"4") )

    for q in Q :
        pspict.DrawGraphs(q[0],q[1])
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def TGdUoZR():
    pspict,fig = SinglePicture("TGdUoZR")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Q=[]
    Q.append( small_box(0,2) )
    Q.append( small_box(1,2) )
    Q.append( small_box(2,2) )
    Q.append( small_box(3,2) )
    Q.append( small_box(0,1) )
    Q.append( small_box(1,1) )
    Q.append( small_box(2,1) )
    Q.append( small_box(0,0) )

    for q in Q :
        pspict.DrawGraphs(q[0],q[1])
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

    
def AIFsOQO():
    pspict,fig = SinglePicture("AIFsOQO")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Q=[]
    Q.append( small_box(0,1) )
    Q.append( small_box(1,1) )
    Q.append( small_box(2,1) )
    Q.append( small_box(3,1) )
    Q.append( small_box(4,1) )
    Q.append( small_box(5,1) )
    Q.append( small_box(0,0) )
    Q.append( small_box(1,0) )
    Q.append( small_box(2,0) )

    for q in Q :
        pspict.DrawGraphs(q[0],q[1])
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
