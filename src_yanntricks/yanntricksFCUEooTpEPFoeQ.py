# -*- coding: utf8 -*-
from yanntricks import *
def FCUEooTpEPFoeQ():
    pspict,fig = SinglePicture("FCUEooTpEPFoeQ")
    pspict.dilatation(1)

    matrix=phyMatrix(5,5)
    for el in matrix.getElements() :
        el.text="*"
    matrix.elements[2,1].text="0"
    matrix.elements[3,1].text="0"
    matrix.elements[3,2].text="0"
    matrix.elements[4,1].text="0"
    matrix.elements[4,2].text="0"
    matrix.elements[5,1].text="0"
    matrix.elements[5,2].text="0"

    squareDelta=matrix.square(   (1,1) , (2,2),pspict )
    squareDelta.edges_parameters.color="red"
    hD=squareDelta.edges[0].midpoint()
    hD.parameters.symbol=""
    hD.put_mark(0.1,angle=70,text="\( \Delta_k(A_2)\)",pspict=pspict)

    squareOmega=matrix.square(   (3,3) , (5,5),pspict )
    squareOmega.edges_parameters.color="blue"
    hO=squareOmega.edges[2].midpoint()
    hO.parameters.symbol=""
    hO.put_mark(0.1,angle=-90,text="\( \Omega_{k+1}(A_2)\)",pspict=pspict)

    pspict.DrawGraphs(matrix,squareDelta,squareOmega,hD,hO)
    
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

