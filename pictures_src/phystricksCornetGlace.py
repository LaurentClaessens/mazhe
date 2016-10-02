from phystricks import *
def CornetGlace():
	pspict,fig = SinglePicture("CornetGlace")

	l=1.2
	x=var('x')
	f1=phyFunction(sqrt(1-x**2)).graph(-1,1)
	f2a=phyFunction(-x).graph(-l,0)
	f2b=phyFunction(x).graph(0,l)
	P = Intersection(f1,f2a)[0]
	Q = Intersection(f1,f2b)[0]
	c1=f1.graph(P.x,Q.x)
	c2a=f2a.graph(0,P.x)
	c2b=f2b.graph(0,Q.x)
	surf=CustomSurface(c2a,c1,c2b)
	surf.parameters.hatched()
	surf.parameters.hatch.color="lightgray"

	pspict.DrawGraphs(surf,f1,f2a,f2b)
	pspict.DrawDefaultAxes()
	fig.conclude()
	fig.write_the_file()
