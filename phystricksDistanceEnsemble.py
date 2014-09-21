from phystricks import *
def DistanceEnsemble():
	pspict,fig = SinglePicture("DistanceEnsemble")

	C=Point(0,0)
	Cercle=Circle(C,1)
	A=Cercle.get_point(45)
	A.put_mark(0.3,45,"$A$",automatic_place=pspict)
	A.parameters.symbol=""
	pspict.DrawGraph(A)
	P=Cercle.get_point(210)
	Q=Cercle.get_point(100)
	P.put_mark(0.5,-90,"$p$",automatic_place=pspict)
	R=Circle(C,0.7).get_point(-90)
	v=AffineVector(C,P)
	X=(v*2.3).F
	X.put_mark(0.3,180,"$x$",automatic_place=pspict)

	xP=Segment(X,P)
	xQ=Segment(X,Q)
	xR=Segment(X,R)
	xQ.parameters.style="dotted"
	xR.parameters.style="dotted"
	pspict.DrawGraph(xP)
	pspict.DrawGraph(xQ)
	pspict.DrawGraph(xR)

	pspict.DrawGraph(Cercle)
	pspict.DrawGraph(P)
	pspict.DrawGraph(R)
	pspict.DrawGraph(Q)
	pspict.DrawGraph(X)

	pspict.dilatation(2)
	fig.conclude()
	fig.write_the_file()
