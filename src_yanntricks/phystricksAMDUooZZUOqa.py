# -*- coding: utf8 -*-
from yanntricks import *
def AMDUooZZUOqa():
    pspict,fig = SinglePicture("AMDUooZZUOqa")

    R=2
    theta=-10
    sigma=60
    O=Point(0,0)
    cercle=Circle(O,R)
    cercle.parameters.style="dashed"
    
    arc=cercle.graph(theta,sigma)
    arc.parameters.style=""
    arc.parameters.color="blue"

    P=cercle.get_point(theta)
    Q=cercle.get_point(sigma)
    P.put_mark(0.3,P.advised_mark_angle(pspict),r"$\theta_0$",pspict=pspict)
    Q.put_mark(0.3,Q.advised_mark_angle(pspict),r"$\theta_1$",pspict=pspict)
    P.parameters.symbol=""
    Q.parameters.symbol=""
    M=cercle.get_point((sigma+theta)/2)
    M.put_mark(0.3,M.advised_mark_angle(pspict),"$\sigma(t)$",pspict=pspict)

    angle=AngleAOB(P,O,Q,r=0.5)
    #angle.put_mark(0.2,None,r"$\theta$",pspict=pspict)
    angle.put_mark(text=r"$\theta$",pspict=pspict)
    seg_theta=Segment(O,P)
    seg_sigma=Segment(O,Q)
    
    seg_sigma.put_mark(0.3,seg_sigma.advised_mark_angle(pspict),r"$R$",pspict=pspict)

    pspict.DrawGraphs(cercle,arc,angle,seg_theta,seg_sigma,P,Q)
    fig.conclude()
    fig.write_the_file()

