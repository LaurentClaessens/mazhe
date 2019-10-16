# -*- coding: utf8 -*-

from __future__ import division

from yanntricks import *

c=0.5
def small_box(X,Y,pspict,text=""):
    x=c*X
    y=c*Y
    A=Point(x-c/2,y-c/2)
    B=Point(x+c/2,y-c/2)
    C=Point(x+c/2,y+c/2)
    D=Point(x-c/2,y+c/2)
    P=Point(x,y)
    P.put_mark(0.0,0,text,pspict=pspict)
    P.parameters.symbol=""
    return [P,Polygon(A,B,C,D)]

def GBnUivi():
    pspict,fig = SinglePicture("GBnUivi")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Q=[]
    Q.append( small_box(0,2,pspict,"1") )
    Q.append( small_box(1,2,pspict,"2") )
    Q.append( small_box(2,2,pspict,"3") )
    Q.append( small_box(3,2,pspict,"4") )
    Q.append( small_box(4,2,pspict,"7") )
    Q.append( small_box(5,2,pspict,"8") )
    Q.append( small_box(0,1,pspict,"3") )
    Q.append( small_box(1,1,pspict,"5") )
    Q.append( small_box(2,1,pspict,"6") )
    Q.append( small_box(3,1,pspict,"9") )
    Q.append( small_box(0,0,pspict,"10") )

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
    Q.append( small_box(0,1,pspict,"1") )
    Q.append( small_box(1,1,pspict,"3") )
    Q.append( small_box(0,0,pspict,"2") )
    Q.append( small_box(1,0,pspict,"4") )

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
    Q.append( small_box(0,2,pspict) )
    Q.append( small_box(1,2,pspict) )
    Q.append( small_box(2,2,pspict) )
    Q.append( small_box(3,2,pspict) )
    Q.append( small_box(0,1,pspict) )
    Q.append( small_box(1,1,pspict) )
    Q.append( small_box(2,1,pspict) )
    Q.append( small_box(0,0,pspict) )

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
    Q.append( small_box(0,1,pspict) )
    Q.append( small_box(1,1,pspict) )
    Q.append( small_box(2,1,pspict) )
    Q.append( small_box(3,1,pspict) )
    Q.append( small_box(4,1,pspict) )
    Q.append( small_box(5,1,pspict) )
    Q.append( small_box(0,0,pspict) )
    Q.append( small_box(1,0,pspict) )
    Q.append( small_box(2,0,pspict) )

    for q in Q :
        pspict.DrawGraphs(q[0],q[1])
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

