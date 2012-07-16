from phystricks import *
def Differentielle():
	pspict,fig = SinglePicture("Differentielle")

	x=var('x')
	a=2
	x0=4
	mx=1
	Mx=x0+0.2
	f=phyFunction(2*log(x/2)+2).graph(mx,Mx)
	tangente=f.tangent_phyFunction(a).graph(mx,Mx)
	A=f.get_point(a)
	C=f.get_point(x0)
	B=Point(x0,A.y)
	D=tangente.get_point(x0)
	Ab=Point(A.x,0)
	Bb=Point(B.x,0)
	AB=Segment(A,B)
	BD=Segment(B,D)
	measureEps=MeasureLength(Segment(C,D),0.3)
	measureEps.put_mark(0.5,measureEps.advised_mark_angle,"$\epsilon(h)$")
	measureT=MeasureLength(Segment(B,D),1.5)
	measureT.put_mark(0.5,measureT.advised_mark_angle,"$T(h)$")

	AAb=Segment(A,Ab)
	ABb=Segment(B,Bb)
	measureAX=MeasureLength( Segment(A,B),0.5 )
	measureAX.put_mark(0.3,measureAX.advised_mark_angle,"$h$")

	Ab.put_mark(0.3,-90,"$a$")
	Bb.put_mark(0.3,-90,"$x$")
	A.put_mark(0.5,A.advised_mark_angle,"$f(a)$")
	C.put_mark(0.7,-45,"$f(x)$")
	tangente.parameters.color="red"
	AB.parameters.style="dotted"
	BD.parameters.style=AB.parameters.style
	AAb.parameters.style=AB.parameters.style
	ABb.parameters.style=AB.parameters.style

	pspict.DrawGraphs(AB,BD,tangente,f,measureEps,measureT,measureAX,A,B,C,D,Ab,Bb,AAb,ABb)
	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()

	pspict.dilatation(1)

	fig.conclude()
	fig.write_the_file()
