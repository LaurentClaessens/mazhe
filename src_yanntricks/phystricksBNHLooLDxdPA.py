# -*- coding: utf8 -*-
from yanntricks import *
def BNHLooLDxdPA():
    pspict,fig = SinglePicture("BNHLooLDxdPA")
    O=Point(0,0)

    a=Vector(3,0)
    b=Vector(2,2)
    a.put_mark(0.3,-45,"$a$",pspict=pspict)
    b.put_mark(0.3,90,"$b$",pspict=pspict)

    C=(a+b).F

    l1=Segment(b.F,C)
    l2=Segment(a.F,C)
    l1.parameters.style="dotted"
    l1.parameters.color="blue"
    l2.parameters=l1.parameters

    D=b.F.projection(a)

    h=Segment(b.F,D)
    h.parameters.style="dashed"
    h.put_mark(0.2,0,"$h$",pspict=pspict)

    theta=AngleAOB(D,O,b.F)
    theta.put_mark(0.37,text=r"$\theta$",pspict=pspict)

    pspict.DrawGraphs(a,b,C,l1,l2,h,theta,D)
    fig.conclude()
    fig.write_the_file()

