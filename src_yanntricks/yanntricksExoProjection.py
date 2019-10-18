# -*- coding: utf8 -*-
from yanntricks import *
def ExoProjection():
    pspict,fig = SinglePicture("ExoProjection")

    def point(l):
        return Point(2,1)*l
    def vect(l):
        return AffineVector(A,point(l))

    w=Vector(point(0.7))
    w.parameters.color="blue"
    w.put_mark(0.3,130,"$w$",pspict=pspict)

    A=Point(1.5,3)
    A.put_mark(0.3,90,"$A$",pspict=pspict)
    B=A.projection(w)
    pspict.specific_needs=r"""
    \usepackage{latexsym}
    \usepackage{amsfonts}
    \usepackage{amsmath}
    \usepackage{amsthm}
    \usepackage{amssymb}
    \usepackage{bbm}
    \usepackage{mathrsfs}           
    \DeclareMathOperator{\pr}{\texttt{proj}}"""       # Un de ces paquets est demandé par \DeclareMathOperator
    B.put_mark(0.1,-45,"$\pr_w(A)$",pspict=pspict)

    v1=AffineVector(A,B)
    v1.parameters.color="red"

    droite=Segment(2*w.F,-1.5*w.F)
    droite.parameters.style="dashed"

    Pl=point(-0.5)
    Pl.put_mark(0.1,-90,"$P(\lambda)$",pspict=pspict,position="corner")
    #Pl.parameters.symbol=""
    Vl=vect(-0.5)
    Vl.parameters.color="cyan"

    pspict.DrawGraphs(droite,B,v1,w,Pl,Vl,A)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

