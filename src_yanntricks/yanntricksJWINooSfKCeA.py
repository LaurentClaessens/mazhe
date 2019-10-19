# -*- coding: utf8 -*-
from yanntricks import *
def JWINooSfKCeA():
    pspict,fig = SinglePicture("JWINooSfKCeA")
    X=Point(1,0)
    M=Point(1,2)
    O=Point(0,0)
    vecteur=Vector(M)

    angle=AngleAOB(X,O,M)

    angle.put_mark(0.3,None,r"$\theta$",pspict=pspict)

    milieu=vecteur.midpoint()
    milieu.put_mark(0.2,milieu.advised_mark_angle(pspict),"$r$",pspict=pspict)

    milieu.parameters.symbol=""
    M.parameters.symbol=""
    M.put_mark(0.1,text="$(x,y)$",pspict=pspict,position="W")

    pspict.DrawGraphs(M,vecteur,angle,milieu)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

