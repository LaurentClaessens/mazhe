# -*- coding: utf8 -*-
from yanntricks import *
def QSKDooujUbDCsu():
    pspict,fig = SinglePicture("QSKDooujUbDCsu")
    pspict.dilatation(0.7)

    h=1
    mx=-3
    seg=Segment( Point(mx,h),Point(-mx,h)  )
    b1=Point(0,0)
    b2=Point(1,h)
    b1.put_mark(0.2,angle=-90,added_angle=0,text="\( \\pi(b_1)\)",pspict=pspict)
    b2.put_mark(0.2,angle=90,added_angle=0,text="\( \\pi(b_2)\)",pspict=pspict)

    pspict.DrawGraphs(seg,b1,b2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

