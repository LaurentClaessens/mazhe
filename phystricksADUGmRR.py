# -*- coding: utf8 -*-
from phystricks import *

def ADUGmRR_A():
    pspict,fig = SinglePicture("ADUGmRR_A")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,0)

    A.put_mark(0.1,90,r"\( \alpha_i\)",automatic_place=(pspict,"S"))
    B.put_mark(0.1,90,r"\( \alpha_{i+1}\)",automatic_place=(pspict,"S"))
    A.parameters.symbol="o"
    B.parameters.symbol="o"

    l=Segment(A,B)

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def ADUGmRR_B():
    pspict,fig = SinglePicture("ADUGmRR_B")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,0)

    A.put_mark(0.1,90,r"\( \alpha_i\)",automatic_place=(pspict,"S"))
    B.put_mark(0.1,90,r"\( \alpha_{i+1}\)",automatic_place=(pspict,"S"))
    #A.parameters.symbol="o"
    #B.parameters.symbol="o"

    l=Segment(A,B)

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def ADUGmRR_C():
    pspict,fig = SinglePicture("ADUGmRR_C")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,0)

    A.put_mark(0.1,90,r"\( \alpha_i\)",automatic_place=(pspict,"S"))
    B.put_mark(0.1,90,r"\( \alpha_{i+1}\)",automatic_place=(pspict,"S"))
    #A.parameters.symbol="o"
    B.parameters.symbol="o"

    l=Segment(A,B)
    l.parameters.add_option("doubleline","true")

    pspict.DrawGraphs(l,A,B)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
