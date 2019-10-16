# -*- coding: utf8 -*-
from yanntricks import *
def CMMAooQegASg():
    pspict,fig = SinglePicture("CMMAooQegASg")
    r=2
    x=var('x')
    f1=phyFunction(sqrt(r**2-x**2)).graph(-r,r)
    f2=phyFunction(-sqrt(r**2-x**2)).graph(-r,r)
    f2.parameters.color="red"

    pspict.DrawGraphs(f1,f2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

