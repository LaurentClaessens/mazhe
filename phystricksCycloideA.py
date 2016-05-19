from phystricks import *
def CycloideA():
	pspict,fig = SinglePicture("CycloideA")

	a=1
	x=var('x')
	f1=a*(x-sin(x))
	f2=a*(1-cos(x))
	curve=ParametricCurve(f1,f2).graph(0,4*pi)

	pspict.DrawGraphs(curve)
	pspict.DrawDefaultAxes()

	pspict.dilatation(1)

	fig.conclude()
	fig.write_the_file()
	
