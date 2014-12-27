# -*- coding: utf8 -*-
from phystricks import *
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
    P.put_mark(0.2,45,"\( \delta\)",automatic_place=(pspict,"corner"))

    v=Vector(0.3,-0.2)

    Q=Point(t1,delta)
    R=Point(t2,delta)

    m1=Segment(  P-v,P+v  )
    m2=Segment(  Q-v,Q+v  )
    m3=Segment(  R-v,R+v  )

    T=Point(t1,0)
    T.put_mark(0.2,-90,"\( t_1\)",automatic_place=(pspict,"N"))
    U=Point(t2,0)
    U.put_mark(0.2,-90,"\( t_2\)",automatic_place=(pspict,"N"))

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

