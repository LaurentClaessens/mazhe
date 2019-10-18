# -*- coding: utf8 -*-
from yanntricks import *
def ASHYooUVHkak():
    pspict,fig = SinglePicture("ASHYooUVHkak")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    delta=1.2
    t1=2
    t2=-1.5
    s1=Segment( Point(t2-0.4,delta),Point(t1+1,delta)  )
    s1.parameters.style="dashed"
    P=Point(0,delta)
    P.put_mark(0.2,45,"\( \delta\)",pspict=pspict,position="corner")

    v=Vector(0.3,-0.2)

    Q=Point(t1,delta)
    R=Point(t2,delta)

    m1=Segment(  P.translate(-v),P.translate(v)  )
    m2=Segment(  Q.translate(-v),Q.translate(v)  )
    m3=Segment(  R.translate(-v),R.translate(v)  )

    T=Point(t1,0)
    T.put_mark(0.2,text="\( t_1\)",pspict=pspict,position="N")
    U=Point(t2,0)
    U.put_mark(0.2,text="\( t_2\)",pspict=pspict,position="N")

    vert1=Segment(T,Q)
    vert1.parameters.style="dotted"
    vert2=Segment(U,R)
    vert2.parameters.style="dotted"

    pspict.DrawGraphs(s1,P,m1,m2,T,U,vert1,vert2,m3)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


