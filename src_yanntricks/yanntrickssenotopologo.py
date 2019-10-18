# -*- coding: utf8 -*-

from __future__ import division

from yanntricks import *
def senotopologo():
    pspict,fig = SinglePicture("senotopologo")
    pspict.dilatation(1.8)

    x=var('x')
    f=phyFunction(x*sin(1/x**2)).graph(-4,4)
    f.linear_plotpoints=2000

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

