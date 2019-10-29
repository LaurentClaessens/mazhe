# -*- coding: utf8 -*-
from yanntricks import *
def UEGEooHEDIJVPn():
    pspict,fig = SinglePicture("UEGEooHEDIJVPn")
    pspict.dilatation(1)

    xmax=5
    x=var('x')
    dig=Segment(  Point(0,0), Point(xmax,xmax)  )
    g=phyFunction( -ln(x/2)+2  ).graph(0.1,xmax)

    pspict.DrawGraphs(dig,g)

    X=5
    for i in range(0,3):
        S=Point(X,0)
        S.put_mark(0.2,angle=-90,added_angle=0,text="\( x_{{ {}  }}\)".format(i),pspict=pspict)
        h=g(X)
        P=Point( X,h  )
        Q=Point( h,h  )
        X=h
        P.put_mark(0.2,angle=None,added_angle=0,text="\( P_{{ {}  }}\)".format(i),pspict=pspict)
        Q.put_mark(0.2,angle=135,added_angle=0,text="\( Q_{{{}}}\)".format(i),pspict=pspict)
        segH=Segment(P,Q)
        segH.parameters.color="cyan"
        segH.parameters.style="dashed"
        segV=Segment(P,S)
        segV.parameters.color="red"
        segV.parameters.style="dashed"
    pspict.DrawGraphs(P,Q,S,segH,segV)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

