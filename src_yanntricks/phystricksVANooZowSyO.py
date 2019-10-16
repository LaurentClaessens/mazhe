# -*- coding: utf8 -*-
from yanntricks import *
def VANooZowSyO():
    pspicts,fig = MultiplePictures("VANooZowSyO",7)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=""
    pspicts[3].mother.caption=""
    pspicts[4].mother.caption=""
    pspicts[5].mother.caption=""
    pspicts[6].mother.caption=""


    for psp in pspicts:
        psp.dilatation_X(0.7)
        psp.dilatation_Y(1)

    x=var('x')

    F=[]
    F.append(   phyFunction(  cos(x) ).graph(-pi,pi)  )
    F.append(   phyFunction(  cos(x+pi/2) ).graph(-pi,pi)  )
    F.append(   phyFunction(  cos(exp(x)) ).graph(-pi,pi)  )
    F.append(   phyFunction(  cos(x)+2 ).graph(-pi,pi)  )
    F.append(   phyFunction(  cos(4*x) ).graph(-pi,pi)  )
    F.append(   phyFunction(  abs(cos(x)) ).graph(-pi,pi)  )
    F.append(   phyFunction(  sqrt(cos(x)) ).graph(-pi/2,pi/2)  )

    for i,psp in enumerate(pspicts):
        print(i,"sur ",len(pspicts))
        f=F[i]
        f.cut_y(-5,5)
        psp.DrawGraphs(f)
        psp.axes.single_axeY.axes_unit=AxesUnit(pi,'')
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

