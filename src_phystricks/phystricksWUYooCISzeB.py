# -*- coding: utf8 -*-

from __future__ import unicode_literals

from phystricks import *
def WUYooCISzeB():
    num=4
    pspicts,fig = MultiplePictures("WUYooCISzeB",num)
    for i in range(0,num):
        pspicts[i].mother.caption="Polyôme d'ordre {}".format(i+1)

    for psp in pspicts:
        psp.dilatation_X(1.2)
        psp.dilatation_Y(0.5)

    mx=-0.7
    Mx=3

    x=var('x')
    f=phyFunction(3*(x+1)**(1/3)+exp(-2*x)).graph(mx,Mx)

    for i in range(1,num+1):
        g=phyFunction(f.sage.taylor(x,0,i)).graph(mx,Mx)
        g.parameters.color="red"
        g.cut_y(-1,7)
        pspicts[i-1].DrawGraphs(g)


    for psp in pspicts:
        psp.axes.single_axeY.Dx=2
        psp.DrawGraphs(f)
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
