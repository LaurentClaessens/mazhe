from phystricks import *
def PartieEntiere():
	pspict,fig = SinglePicture("PartieEntiere")

	x=var('x')
	f=phyFunction(floor(x)).graph(-2,3)

	pspict.DrawGraphs(f)
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
