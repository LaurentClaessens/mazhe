from phystricks import *
def FonctionXtrois():
	pspict,fig = SinglePicture("FonctionXtrois")

	x=var('x')
	mx=-1.5
	Mx=1.5
	f=phyFunction(x**3).graph(mx,Mx)
	g=f.derivative().graph(mx,Mx)

	g.parameters.color="red"

	pspict.DrawGraphs(f,g)
	pspict.axes.single_axeY.Dx=2

	pspict.DrawDefaultAxes()
	pspict.dilatation(0.6)
	fig.conclude()
	fig.write_the_file()
