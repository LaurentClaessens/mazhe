# -*- coding: utf8 -*-
from yanntricks import *
def VSZRooRWgUGu():
    pspict,fig = SinglePicture("VSZRooRWgUGu")
    pspict.dilatation(1.5)

    x=var('x')
    
    O = Point(0,0)
    mx = 1
    Mx = 5
    ms = 2
    Ms = 4
    f=phyFunction(3-2/x).graph(mx,Mx)
    f.parameters.color="red"
    A = f.get_point(ms)
    X = f.get_point(Ms)
    F = f.get_point(Mx)
    a = Point(ms,0)
    x = Point(Ms,0)
    N = Segment(X,x).midpoint()

    surface=SurfaceUnderFunction(f,ms,Ms)
    surface.parameters.hatched()
    surface.parameters.hatch.color="blue"
    surface.Isegment.parameters.style="dashed"
    surface.Fsegment.parameters.style="dashed"

    a.put_mark(0.3,-90,"$a$",pspict=pspict)
    x.put_mark(0.3,-90,"$x$",pspict=pspict)
    F.put_mark(0.5,0,"$f(x)$",pspict=pspict)
    N.put_mark(2,0,"$S=F(x)=\int_a^xf(t)dt$",pspict=pspict)
    a.parameters.symbol=""
    x.parameters.symbol=""
    F.parameters.symbol=""
    N.parameters.symbol=""

    pspict.axes.no_graduation()

    pspict.DrawGraphs(f,surface,a,x,F,N,surface)

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

