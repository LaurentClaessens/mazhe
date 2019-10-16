# -*- coding: utf8 -*-
from yanntricks import *
def KKJAooubQzgBgP():
    pspict,fig = SinglePicture("KKJAooubQzgBgP")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(x/sqrt(1+x**2)).graph(0,3)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

