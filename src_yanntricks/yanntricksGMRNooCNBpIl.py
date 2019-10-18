# -*- coding: utf8 -*-
from yanntricks import *
def GMRNooCNBpIl():
    pspict,fig = SinglePicture("GMRNooCNBpIl")
    pspict.dilatation(1)

    matrix=phyMatrix(6,6)
    matrix.set_matrix_environment("matrix")
    for el in matrix.getElements() :
        el.text="\cdot"

    for i in range(2,6):
        for j in range(2,6):
            matrix.elements[i,j].text="*"


    I4=matrix.square(   (2,2) , (2,5),pspict )
    I1=matrix.square(   (2,2) , (5,2),pspict )
    I2=matrix.square(   (2,5) , (5,5),pspict )
    I3=matrix.square(   (5,2) , (5,5),pspict )

    S=matrix.square( (3,3),(4,4),pspict  )
    S.edges_parameters.style="dashed"

    Ny=matrix.elements[1,1].central_point
    Ny.put_mark(0.2,angle=90+45,added_angle=0,text="\( N_y\)",pspict=pspict)

    Z=matrix.elements[6,1].central_point
    Z.put_mark(0.2,angle=180,added_angle=0,text="\( 0\)",pspict=pspict)
    Z.put_mark(0.2,angle=-90,added_angle=0,text="\( 0\)",pspict=pspict)

    Nx=matrix.elements[6,6].central_point
    Nx.put_mark(0.2,angle=-45,added_angle=0,text="\( N_x\)",pspict=pspict)

    pspict.DrawGraphs(matrix,I1,I2,I3,I4,S,Ny,Z,Nx)
    
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
