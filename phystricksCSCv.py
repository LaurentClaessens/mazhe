from phystricks import *

def CSCv():
	fig = GenericFigure("CSCv")

	ssfig1 = fig.new_subfigure(r"Le graphique de $r(\theta)$","CSCvGr")
	pspict1 = ssfig1.new_pspicture("CSCvGraphe")

	x=var('x')
	r=phyFunction(cos(x)-cos(2*x)).graph(0,2*pi)
	pspict1.DrawGraph(r)

	pspict1.DrawDefaultAxes()
	pspict1.dilatation(1)

	ssfig2 = fig.new_subfigure("La courbe polaire correspondante","CSCvCourbe")
	pspict2 = ssfig2.new_pspicture("CSCvCourbe")

	curve1=PolarCurve(r).graph(0,2*pi/3)
	curve2=PolarCurve(r).graph(4*pi/3,2*pi)
	pspict2.DrawGraphs(curve1,curve2)

	pspict2.DrawDefaultAxes()
	pspict2.dilatation(1)

	fig.conclude()
	fig.write_the_file()
