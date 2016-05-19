# -*- coding: utf8 -*-
from phystricks import *

def SuiteUnSurn():
    pspict,fig = SinglePicture("SuiteUnSurn")

    def suite(i):
        return SR(1)/i

    n=10
    for i in range(1,n+1):
        y=suite(i)
        P=Point(i,float(y))
        P.put_mark(0.3,90,"$%s$"%(repr(y)),automatic_place=pspict)
        pspict.DrawGraphs(P)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    pspict.dilatation_Y(3)

    fig.conclude()
    fig.write_the_file()
