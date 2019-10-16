# -*- coding: utf8 -*-
from yanntricks import *
def TIMYoochXZZNGP():
    pspict,fig = SinglePicture("TIMYoochXZZNGP")
    pspict.dilatation(0.7)

    h=1
    mx=-3
    seg=Segment( Point(mx,h),Point(-mx,h)  )
    e1=Point(0,0)
    e2=Point(1,h)
    e1.put_mark(0.2,angle=-90,added_angle=0,text="\( \\pi(e_1)\)",pspict=pspict)
    e2.put_mark(0.2,angle=90,added_angle=0,text="\( \\pi(e_2)\)",pspict=pspict)

    pspict.DrawGraphs(seg,e1,e2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

