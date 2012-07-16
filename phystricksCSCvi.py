from phystricks import *

def CSCvi():
	fig = GenericFigure("SubfiguresCSCvi")

	ssfig1 = fig.new_subfigure(r"Le graphique de $r(\theta)$","CSCviGr")
	pspict1 = ssfig1.new_pspicture("CSCviGraphe")

	x=var('x')
	epsilon=0.4
	limite=-pi/2
	llam=limite+epsilon
	Llam=pi/2
	r=phyFunction(cos(x)/(1+sin(x)))

	graphe=r.graph(llam,Llam)

	P=Point(limite,0)
	Q=Point(limite,graphe.bounding_box().N().y)
	assymp=Segment(P,Q)
	assymp.parameters.color="lightgray"
	assymp.parameters.style="dashed"
	pspict1.DrawGraphs(graphe,assymp)

	pspict1.DrawDefaultAxes()
	pspict1.dilatation(1)

	ssfig2 = fig.new_subfigure("La courbe polaire correspondante","CSCviCourbe")
	pspict2 = ssfig2.new_pspicture("CSCviCourbe")

	curve=PolarCurve(r).graph(llam,Llam)
	pspict2.DrawGraphs(curve)

	pspict2.DrawDefaultAxes()
	pspict2.dilatation(1)

	fig.conclude()
	fig.write_the_file()
