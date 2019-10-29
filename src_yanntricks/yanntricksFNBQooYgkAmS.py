# -*- coding: utf8 -*-
from yanntricks import *
def FNBQooYgkAmS():
    pspict,fig = SinglePicture("FNBQooYgkAmS")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    ellipse=ParametricCurve( 3*cos(x),1*sin(x)  ).graph(0,2*pi)

    theta=pi/4
    X=ellipse.get_point(theta)
    n=ellipse.get_normal_vector(theta)
    n.put_mark(0.2,n.advised_mark_angle(pspict),"\( \\nabla q(x)\)",pspict=pspict,position="corner")
    X.put_mark(0.2,added_angle=20,text="\( x\)",pspict=pspict)

    Ax=n.rotation(200)
    Ax.put_mark(0.2,Ax.advised_mark_angle(pspict),"\( Ax\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(ellipse,X,n,Ax)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


