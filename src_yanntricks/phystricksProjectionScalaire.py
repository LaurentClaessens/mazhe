from phystricks import *
def ProjectionScalaire():
	pspict,fig = SinglePicture("ProjectionScalaire")
	pspict.dilatation(1)

	x=1.5
	y=2
	l=2.5
	O=Point(0,0)
	X=Vector(x,y)
	Y=Vector(l,0)
	P=X.projection(Y).F
	X.put_mark(0.3,45,"$X$",pspict=pspict)
	Y.put_mark(0.2,90,"$Y$",pspict=pspict)
	X.parameters.color="blue"
	Y.parameters.color="blue"
	h=Segment(X.F,P)
	h.parameters.style="dotted"
	measure=MeasureLength(Segment(O,P),0.3)
	measure.put_mark(0.3,-90,"$x$",pspict=pspict)

	pspict.DrawGraphs(X,Y,P,O,measure,h)
	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()
	fig.conclude()
	fig.write_the_file()

