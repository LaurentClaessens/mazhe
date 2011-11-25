from phystricks import *
def ProjectionScalaire():
	pspict,fig = SinglePicture("ProjectionScalaire")

	x=1.5
	y=2
	l=2.5
	O=Point(0,0)
	X=Vector(x,y)
	Y=Vector(l,0)
	P=X.projection(Y).F
	X.put_mark(0.3,45,"$X$",automatic_place=pspict)
	Y.put_mark(0.2,90,"$Y$",automatic_place=pspict)
	X.parameters.color="blue"
	Y.parameters.color="blue"
	h=Segment(X.F,P)
	h.parameters.style="dotted"
	measure=MeasureLength(Segment(O,P),0.3)
	measure.put_mark(0.3,-90,"$x$")

	pspict.DrawGraphs(X,Y,P,O,measure,h)
	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
