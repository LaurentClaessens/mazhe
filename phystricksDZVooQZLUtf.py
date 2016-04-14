# -*- coding: utf8 -*-

from phystricks import *
def DZVooQZLUtf():

    x=var('x')
    F=[]
    F.append(   phyFunction(  abs(ln(x)) ).graph(0.01,5)  )
    F.append(   phyFunction(  ln(x) ).graph(0.01,5)  )
    F.append(   phyFunction(  ln(x)+1 ).graph(0.01,5)  )
    F.append(   phyFunction(  sqrt(ln(x)) ).graph(1,5)  )
    F.append(   phyFunction(  ln(x+1) ).graph(-0.99,5)  )

    F.append(   phyFunction(  ln(x**2) ).graph(-3,3)  )
    F[-1].addPlotPoint(0)

    F.append(   phyFunction(  ln( abs(x) ) ).graph(-3,3)  )
    F[-1].addPlotPoint(0)
    F[-1].cut_y(-3,3)

    n_fun=len(F)

    pspicts,fig = MultiplePictures("DZVooQZLUtf",n_fun)
    for i in range(n_fun) :
        pspicts[i].mother.caption=""

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(0.7)

    for i,psp in enumerate(pspicts):
        print(i+1,"sur ",len(pspicts))
        f=F[i]
        f.cut_y(-5,5)
        psp.DrawGraphs(f)
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
