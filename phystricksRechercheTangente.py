# -*- coding: utf8 -*-
from phystricks import *



mx=0.7
Mx=5
x=var('x')
f=phyFunction(-3/x+5).graph(mx,Mx)
P=f.get_point(1.7)
Q=f.get_point(4)

P.put_mark(0.3,P.advised_mark_angle,"$P$")
Q.put_mark(0.3,Q.advised_mark_angle,"$Q$")

def TangenteQuestion():
    pspictQuestion,figQuestion = SinglePicture("TangenteQuestion",script_filename="RechercheTangente")

    pspictQuestion.DrawGraphs(f,P)
    pspictQuestion.axes.no_graduation()
    pspictQuestion.DrawDefaultAxes()
    pspictQuestion.dilatation(0.7)
    figQuestion.conclude()
    figQuestion.write_the_file()

def TangenteDetail():
    pspictDetail,figDetail = SinglePicture("TangenteDetail",script_filename="RechercheTangente")

    Px=Point(P.x,0)
    Py=Point(0,P.y)
    Qx=Point(Q.x,0)
    Qy=Point(0,Q.y)
    
    Py.put_mark(0.1,180,"$f(a)$",automatic_place=(pspictDetail,"E"))
    Qy.put_mark(0.1,180,"$f(x)$",automatic_place=(pspictDetail,"E"))
    Px.put_mark(0.2,-90,"$a$",automatic_place=(pspictDetail,"N"))
    Qx.put_mark(0.2,-90,"$x$",automatic_place=(pspictDetail,"N"))

    v1=Segment(Q,Qx)
    v2=Segment(P,Px)
    h1=Segment(Q,Qy)
    h2=Segment(P,Py)
    I=Intersection(v1,h2)[0]
    h3=Segment(P,I)
    v1.parameters.color="green"
    v1.parameters.style="dashed"
    v2.parameters=v1.parameters
    h1.parameters=v1.parameters
    h2.parameters=v1.parameters
    h3.parameters=v1.parameters

    corde=Segment(P,Q).dilatation(1.7)
    corde.parameters.color="cyan"

    Dx=MeasureLength(h3,0.2)
    Dx.put_mark(0.2,-90,"$x-a$",automatic_place=(pspictDetail,"N"))
    Dy=MeasureLength(Segment(Q,I),-0.2)
    Dy.put_mark(0.2,0,"$f(x)-f(a)$",automatic_place=(pspictDetail,"W"))

    pspictDetail.DrawGraphs(corde,v1,v2,h1,h2,h3,f,P,Px,Py,Q,Qx,Qy,Dx,Dy)

    pspictDetail.axes.no_graduation()
    pspictDetail.DrawDefaultAxes()
    pspictDetail.dilatation(1)
    figDetail.conclude()
    figDetail.write_the_file()

def LesSubFigures():
    fig=GenericFigure("LesSubFigures",script_filename="RechercheTangente")

    fixed_size=4
    tangente=f.get_tangent_segment(P.x).fix_size(fixed_size)
    tangente.parameters.color="red"

    n_ssfig=6
    for i in range(0,n_ssfig):
        text=u"\ldots de mieux en mieux\ldots"
        if i==0:
            text=u"Pas très bon \ldots"
        if i==n_ssfig-1:
            text=u"\ldots presque parfait."

        ssfig=fig.new_subfigure(text)
        pspict=ssfig.new_pspicture()
        Qi = f.get_point( Q.x-i*(Q.x-P.x)/(n_ssfig) )
        Qi.put_mark(0.3,Qi.advised_mark_angle+180,"$Q_{%s}$"%str(i))

        corde=Segment(P,Qi).fix_size(fixed_size)
        corde.parameters.color="cyan"

        pspict.DrawGraphs(corde,tangente,f,Qi,P)

        pspict.axes.no_graduation()
        pspict.DrawDefaultAxes()
        pspict.dilatation(0.7)

    fig.conclude()
    fig.write_the_file()
