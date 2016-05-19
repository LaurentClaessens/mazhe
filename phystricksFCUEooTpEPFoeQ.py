# -*- coding: utf8 -*-
from phystricks import *
def FCUEooTpEPFoeQ():
    pspict,fig = SinglePicture("FCUEooTpEPFoeQ")
    pspict.dilatation(1)

    matrix=phyMatrix(5,5)
    for el in matrix :
        el.text="*"
    matrix.elements[1,1].text="$\lim_{x\\to \infty}f(x)$"
    matrix.elements[1,2].text="$B$"
    matrix.elements[1,3].text="$C$"
    #matrix.elements[2,1].text=""
    matrix.elements[2,2].text="\( \int_a^b \)"
    matrix.elements[2,3].text="$\sin(x)$"
    #matrix.elements[3,1].text=""
    matrix.elements[3,2].text="$\Delta_k(A_m)$"
    matrix.elements[3,3].text="$\\vdots$"

    square=matrix.square(   (1,1) , (2,2),pspict )
    square.parameters.color="red"
    h=square.edges[0].midpoint()
    h.parameters.symbol=""
    h.put_mark(0.1,angle=90,text="\( \Delta_2(A)\)",automatic_place=(pspict,""))
    pspict.DrawGraphs(matrix,square,h)
    
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
