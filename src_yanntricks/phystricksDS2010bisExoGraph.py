# -*- coding: utf8 -*-
from yanntricks import *

def DS2010bisExoGraph():
    pspict,fig=MultiplePictures("DS2010bisExoGraph",10)

    #ssfig1 = fig.new_subfigure("", "cosinus")
    #pspict1 = ssfig1.new_pspicture("cosinus")
    #ssfig2 = fig.new_subfigure("", "valabsoluecosinus")
    #pspict2 =ssfig2.new_pspicture("valabsoluecosinus")
    #ssfig3 = fig.new_subfigure("", "cosxplusun")
    #pspict3 = ssfig3.new_pspicture("cosxplusun")
    #    ssfig4 = fig.new_subfigure("","sinus" )
    #pspict4 = ssfig4.new_pspicture("sinus")
    #ssfig5 = fig.new_subfigure("", "cosex")
    #pspict5 = ssfig5.new_pspicture("cosex")
    #    #ssfig6 = subfigure(" ")
    ##pspict6 = pspicture("ecosx")
    #    ssfig7 = fig.new_subfigure("","sqrtcos" )
    #pspict7 = ssfig7.new_pspicture("sqrtcos")
    #    #ssfig8 = subfigure(" ")
    ##pspict8 = pspicture("cossqrt")
    #    ssfig9 = fig.new_subfigure("","cosquattrox" )
    #pspict9 = ssfig9.new_pspicture("cosquattrox")
    #    #ssfig10 = subfigure(" ")
    ##pspict10 = pspicture("cosxquadro")

    r=1
    eps=exp(-2)
    # Fonctions
    x=var('x')
        
    f1=cos(x)
    f2=abs(cos(x))
    f3=cos(x)+1
    f4=cos(x+pi/2)
    f5=cos(exp(x))
    f6=exp(cos(x))
    f7=sqrt(cos(x))
    f8=cos(sqrt(x))
    f9=cos(4*x)
    f10=cos(x**2)

        # Graphes
        
    F1=phyFunction(f1).graph(-pi, 3*pi/2)
    F2=phyFunction(f2).graph(-pi, 3*pi/2)
    F3=phyFunction(f3).graph(-pi,3*pi/2)
    F4=phyFunction(f4).graph(-pi,3*pi/2)
    F5=phyFunction(f5).graph(-pi,3*pi/2)
    F6=phyFunction(f6).graph(-pi, 3*pi/2)
    F7a=phyFunction(f7).graph(-pi/2, pi/2)
    F7b=phyFunction(f7).graph(3*pi/2, 2*pi)
    F8=phyFunction(f8).graph(0,3*pi/2)
    F9=phyFunction(f9).graph(-pi, 3*pi/2)
    F10=phyFunction(f10).graph(-pi, 3*pi/2)

        # Figures
        # pspict1ss.DrawGraphs(F0)
    
    pspict[0].DrawGraphs(F1)
    pspict[0].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[0].axes.Dx=0.5
    #pspict[0].BB.addX(-0.5)
    #pspict[0].BB.addY(3.5)
    pspict[0].DrawDefaultAxes()
    pspict[0].dilatation(.7)

    pspict[1].DrawGraphs(F2)
    pspict[1].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[1].axes.Dx=0.5
    #pspics[1].DrawGraphs(F2b)
    #pspict[1].BB.addX(-2)
    #pspict[1].BB.addY(3)
    pspict[1].DrawDefaultAxes()
    pspict[1].dilatation(.7)

    pspict[2].DrawGraphs(F3)
    pspict[2].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[2].axes.Dx=0.5
    #pspict[2].BB.addX(-2)
    #pspict[2].BB.addY(3)
    pspict[2].DrawDefaultAxes()
    pspict[2].dilatation(.5)

    pspict[3].DrawGraphs(F4)
    pspict[3].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[3].axes.Dx=0.5
    #pspict[3].BB.addX(-1)
        #pspict[3].BB.addY(3)
    pspict[3].DrawDefaultAxes()
    pspict[3].dilatation(.7)

    F5.linear_plotpoints=1000
    pspict[4].DrawGraphs(F5)
    pspict[4].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[4].axes.Dx=0.5
    #pspict[4].BB.addX(-2)
    #pspict[4].BB.addY(3)
    #pspict[4].BB.addY(-3)
    pspict[4].DrawDefaultAxes()
    pspict[4].dilatation(.7)
    
    #Celle-ci est à enlever
    pspict[5].DrawGraphs(F6)
    pspict[5].BB.addX(-2)
    pspict[5].BB.addY(3)
    pspict[5].BB.addY(-3)
    pspict[5].DrawDefaultAxes()
    pspict[5].dilatation(.5)

    pspict[6].DrawGraphs(F7a)
    pspict[6].DrawGraphs(F7b)  
    pspict[6].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[6].axes.Dx=0.5
    #pspict[6].BB.addX(-2)
    #pspict[6].BB.addY(3)
    pspict[6].DrawDefaultAxes()
    pspict[6].dilatation(.7)

    # Celle-ci est à enlever
    pspict[7].DrawGraphs(F8)
    pspict[7].BB.addX(-3)
    pspict[7].BB.addY(3.5)
    pspict[7].DrawDefaultAxes()
    pspict[7].dilatation(.5)

    pspict[8].DrawGraphs(F9)
    pspict[8].axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict[8].axes.Dx=0.5
    #pspict[8].BB.addX(-2)
    #pspict[8].BB.addY(3)
    pspict[8].DrawDefaultAxes()
    pspict[8].dilatation(.7)

    pspict[9].DrawGraphs(F10)
    pspict[9].BB.addX(-2)
    pspict[9].BB.addY(3)
    pspict[9].DrawDefaultAxes()
    pspict[9].dilatation(.5)

    new_pspict,new_fig = SubsetFigures(pspict,fig,[0,1,2,3,4,6,8,9])

    new_fig.conclude()
    new_fig.write_the_file()


