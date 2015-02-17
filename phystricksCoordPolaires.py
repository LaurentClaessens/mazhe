from phystricks import *
def CoordPolaires():
	pspict,fig = SinglePicture("CoordPolaires")

	X=Point(1,0)
	M=Point(1,2)
	O=Point(0,0)
	vecteur=Vector(M)

	angle=Angle(X,O,M)

	angle.put_mark(0.3,None,r"$\theta$",automatic_place=pspict)

	milieu=vecteur.center()
	milieu.put_mark(0.2,milieu.advised_mark_angle(pspict),"$r$",automatic_place=pspict)

	milieu.parameters.symbol=""
	M.parameters.symbol=""
	M.put_mark(0.1,0,"$(x,y)$",automatic_place=(pspict,"W"))

	pspict.DrawGraphs(M,vecteur,angle,milieu)
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
