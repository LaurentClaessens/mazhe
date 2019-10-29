# -*- coding: utf8 -*-
from yanntricks import *

def ExoCUd():
    pspict,fig = SinglePicture("ExoCUd")
    
    x=var('x')
    f=phyFunction(x**2-2*x+1)
    a=1
    l=2
    f1=f.graph(a-l,a)
    f2=f.graph(a,a+l)
    f1.parameters.color="red"

    P=f.get_point(a)
    Ass=Segment(Point(a,P.y-0.5),Point(a,f(a+l)))
    Ass.parameters.color="gray"
    Ass.parameters.style="dashed"

    s=1.6
    xx=[a+s,a-s]
    yy=f(xx[0])
    A=Point(0,yy)
    A.put_mark(0.3,45,"$y$",pspict=pspict)
    r=[f.get_point(k) for k in xx]
    p=[Point(p.x,0) for p in r]
    seg=[ Segment(r[i],p[i]) for i in [0,1] ]
    for s in seg:
        s.parameters.style="dashed"
    p[0].put_mark(0.3,-90,r"$x_+$",pspict=pspict)
    p[1].put_mark(0.3,-90,r"$x_-$",pspict=pspict)
    horizontal=Segment(r[0],r[1])
    horizontal.parameters.style="dotted"

    pspict.axes.no_numbering()

    pspict.DrawGraphs(f1,f2,Ass,A,r,p,seg,horizontal)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

