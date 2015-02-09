# -*- coding: utf8 -*-
from phystricks import *
def FNBQooYgkAmS():
    pspict,fig = SinglePicture("FNBQooYgkAmS")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    ellipse=ParametricCurve( 3*cos(x),1*sin(x)  ).graph(0,2*pi)

    theta=pi/4
    X=ellipse.get_point(theta)
    n=ellipse.get_normal_vector(theta)
    n.put_mark(0.2,n.advised_mark_angle,"\( \\nabla q(x)\)",automatic_place=(pspict,"corner"))
    X.put_mark(0.2,90,"\( x\)",automatic_place=(pspict,"S"))

    Ax=n.rotation(200)
    Ax.put_mark(0.2,Ax.advised_mark_angle,"\( Ax\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(ellipse,X,n,Ax)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

