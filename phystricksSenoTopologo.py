from phystricks import *
def SenoTopologo():
	pspict,fig = SinglePicture("senotopologo")

	a=-0.5
	b=0.5
	x=var('x')
	f=phyFunction(x*sin(1/x))
	G=f.graph(a,b)
	G.plotpoints=2000
	pspict.DrawGraph(G)
	pspict.axes.Dx=0.3
	pspict.axes.Dy=0.3
	pspict.DrawDefaultAxes()

	pspict.dilatation(5)

	fig.conclude()
	fig.write_the_file()

