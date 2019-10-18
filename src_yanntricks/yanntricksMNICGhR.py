# -*- coding: utf8 -*-
from yanntricks import *
def unDynkin(name,sym):
    pspict,fig = SinglePicture(name)
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,0)
    C=Point(2,0)
    D=Point(3,0)
    E=Point(4,0)
    A.parameters.symbol="o"
    B.parameters.symbol="o"
    C.parameters.symbol="o"
    D.parameters.symbol="o"
    A.put_mark(0.2,text=sym[0],pspict=pspict,position="S")
    B.put_mark(0.2,text=sym[1],pspict=pspict,position="S")
    C.put_mark(0.2,text=sym[2],pspict=pspict,position="S")
    D.put_mark(0.2,text=sym[3],pspict=pspict,position="S")
    E.put_mark(0.2,text=sym[4],pspict=pspict,position="S")

    AB=Segment(A,B)
    BC=Segment(B,C)
    CD=Segment(C,D)
    DE=Segment(D,E)

    CD.parameters.style="dotted"
    DE.options.DicoOptions["doubleline"]="true"

    pspict.DrawGraphs(AB,BC,CD,DE,A,B,C,D,E)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def MNICGhR():
    unDynkin("MNICGhR",["$\\alpha_1$","$\\alpha_2$","$\\alpha_3$","$\\alpha_{l-1}$","$\\alpha_l$"])
def LEJNDxI():    
    unDynkin("LEJNDxI",["","","","",""])
def RGjjpwF():
    unDynkin("RGjjpwF",["$1$","","","",""])
def STdyNTH():
    unDynkin("STdyNTH",["","","","","$1$"])

