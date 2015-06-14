from phystricks import *
def FonctionEtDerive():
	pspict,fig = SinglePicture("FonctionEtDeriveOM")

	x=var('x')
	mx=-5
	Mx=5
	f=phyFunction(x*cos(x)).graph(mx,Mx)
	g=f.derivative().graph(mx,Mx)

	g.parameters.color="red"

	pspict.axes.single_axeX.axes_unit=AxesUnit(pi,r"\pi")
	pspict.axes.single_axeX.Dx=0.5

	pspict.DrawGraphs(f,g)
	pspict.DrawDefaultAxes()
	pspict.dilatation(0.7)
	fig.conclude()
	fig.write_the_file()
