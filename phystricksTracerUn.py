# -*- coding: utf8 -*-
from phystricks import *

def TracerUn():
	x=var('x')
	fig = GenericFigure("SubfiguresTracerUn")

	ssfig1 = fig.new_subfigure(u"La fonction $y=ex$","Fnex")
	pspict1 = ssfig1.new_pspicture("Fnex")
	f1=phyFunction(2.718281*x).graph(-2,2)
	pspict1.DrawGraph(f1)
	pspict1.DrawDefaultAxes()
	pspict1.dilatation(0.7)

	ssfig3 = fig.new_subfigure(u"La fonction $y=x^2+1$ à gauche et $(x+1)^2$ à droite.","Compo")
	pspict3 = ssfig3.new_pspicture("Compo")
	f3a=phyFunction(x**2+1).graph(-2,0)
	f3b=phyFunction((x+1)**2).graph(0,2)
	pspict3.DrawGraphs(f3a,f3b)
	pspict3.DrawDefaultAxes()
	pspict3.dilatation(0.7)

	ssfig2 = fig.new_subfigure(u"La fonction $y=| x |$","ValAbs")
	pspict2 = ssfig2.new_pspicture("ValAbs")
	f2=phyFunction(abs(x)).graph(-2,2)
	pspict2.DrawGraph(f2)
	pspict2.DrawDefaultAxes()
	pspict2.dilatation(1)

	ssfig4 = fig.new_subfigure(u"La fonction $y=\log_2(2^{x-1})$","Logxmu")
	pspict4 = ssfig4.new_pspicture("logxmu")
	f4=phyFunction(x-1).graph(-2,2)
	pspict4.DrawGraph(f4)
	pspict4.DrawDefaultAxes()
	pspict4.dilatation(0.7)

	fig.conclude()
	fig.write_the_file()
