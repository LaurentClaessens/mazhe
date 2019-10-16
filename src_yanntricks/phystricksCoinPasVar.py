from __future__ import division

from yanntricks import *
def CoinPasVar():
    pspict,fig = SinglePicture("CoinPasVar")

    x=var('x')
    l=2
    N=Point(0,l)
    A=Point(-l,0)
    B=Point(l,0)

    N.put_mark(0.1,90-45,"\( N\)",pspict=pspict)

    S=Segment(A,N)
    S.parameters.color="blue"
    T=Segment(B,N)
    T.parameters.color="blue"

    t1=S.get_point_proportion(1/2)
    t2=T.get_point_proportion(1/2)

    t1.put_mark(0.1,t1.advised_mark_angle(pspict),"\( t_1\)",pspict=pspict)
    t2.put_mark(0.1,t2.advised_mark_angle(pspict)+180,"\( t_2\)",pspict=pspict)

    pspict.axes.no_graduation()

    pspict.DrawGraphs(S,T,N,t1,t2)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

