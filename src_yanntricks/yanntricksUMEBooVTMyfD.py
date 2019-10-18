# -*- coding: utf8 -*-
from yanntricks import *

class expo(object):
    def __init__(self,l):
        self.l=l
    def __call__(self,x):
        return self.l*exp(-self.l*x)

def UMEBooVTMyfD():
    pspict,fig = SinglePicture("UMEBooVTMyfD")
    pspict.dilatation_Y(3)

    l=2
    f=phyFunction(expo(l)).graph(0,10)
    pspict.DrawGraphs(f)

    pspict.comment="One curve is drawn"
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

