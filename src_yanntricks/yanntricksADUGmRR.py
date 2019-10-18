# -*- coding: utf8 -*-
from yanntricks import *

def ADUGmRRA():
    pspict,fig = SinglePicture("ADUGmRRA")

    A=Point(0,0)
    B=Point(1,0)

    A.put_mark(0.1,text=r"\( \alpha_i\)",pspict=pspict,position="S")
    B.put_mark(0.1,text=r"\( \alpha_{i+1}\)",pspict=pspict,position="S")
    A.parameters.symbol="o"
    B.parameters.symbol="o"

    l=Segment(A,B)

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def ADUGmRRB():
    pspict,fig = SinglePicture("ADUGmRRB")

    A=Point(0,0)
    B=Point(1,0)

    A.put_mark(0.1,text=r"\( \alpha_i\)",pspict=pspict,position="S")
    B.put_mark(0.1,text=r"\( \alpha_{i+1}\)",pspict=pspict,position="S")
    #A.parameters.symbol="o"
    #B.parameters.symbol="o"

    l=Segment(A,B)

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def ADUGmRRC():
    pspict,fig = SinglePicture("ADUGmRRC")

    A=Point(0,0)
    B=Point(1,0)

    A.put_mark(0.1,text=r"\( \alpha_i\)",pspict=pspict,position="S")
    B.put_mark(0.1,text=r"\( \alpha_{i+1}\)",pspict=pspict,position="S")
    #A.parameters.symbol="o"
    B.parameters.symbol="o"

    l=Segment(A,B)
    l.parameters.add_option("doubleline","true")

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

