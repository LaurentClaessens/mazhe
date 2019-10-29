# -*- coding: utf8 -*-
from yanntricks import *
def IntTrois():
    fig = GenericFigure("IntTrois")

    O=Point(0,0)
    C=Circle(O,1)
    arc=C.parametric_curve(0,pi/2)
    arc.parameters.color="red"
    h=Segment(Point(0,1),Point(1,1))
    v=Segment(Point(1,1),Point(1,0))
    h.parameters.color=arc.parameters.color
    v.parameters=h.parameters

    P=C.get_point(30)
    Q=Point(P.x,1)
    seg=Segment(P,Q)
    surf=CustomSurface(arc,h,v)
    surf.parameters.filled()
    surf.parameters.fill.color="lightgray"

    ss_fig1=fig.new_subfigure(r"Int\'egrer en cart\'esiennes.","LabelMauvais")
    pspict1=ss_fig1.new_pspicture("mauvais")
    pspict1.dilatation(2)
    pspict1.DrawGraphs(surf,arc,seg,h,v,P,Q)

    pspict1.DrawDefaultAxes()

    ss_fig2=fig.new_subfigure(r"Int\'egrer en polaires.","LabelBon")
    pspict2=ss_fig2.new_pspicture("Bon")
    pspict2.dilatation(2)
    A=C.get_point(35)
    pC=C.get_point(55)
    B =Intersection(Segment(O,A),v)[0]
    D =Intersection(Segment(O,pC),h)[0]
    s1=Segment(A,B)
    s2=Segment(pC,D)
    t1=Segment(O,A)
    t2=Segment(O,pC)
    t1.parameters.style="dotted"
    t2.parameters=t1.parameters
    pspict2.DrawGraphs(t1,t2,surf,h,v,arc,s1,A,B,pC,D,s2)
    pspict2.DrawDefaultAxes()
    
    fig.conclude()
    fig.write_the_file()

