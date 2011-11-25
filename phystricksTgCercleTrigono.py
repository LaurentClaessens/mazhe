from phystricks import *
def TgCercleTrigono():
	pspict,fig = SinglePicture("TgCercleTrigono")

	O=Point(0,0)
	X=Point(1,0)
	Cercle=Circle(O,2)
	P=Cercle.get_point(50)
	Q=Cercle.get_point(150)
	vP=Vector(P)
	vQ=Vector(Q)

	vP.parameters.color="red"
	vQ.parameters.color="cyan"

	theta=Angle(X,O,P)
	theta.put_mark(0.3,theta.advised_mark_angle,r"$\theta$")
	theta.parameters.color=vP.parameters.color

	phi=Angle(X,O,Q,theta.r+0.5)
	phi.set_mark_angle(0.5*(90+phi.angleF.degree))
	phi.put_mark(0.3,phi.advised_mark_angle,r"$\varphi$")
	phi.parameters.color=vQ.parameters.color

	tangente=Cercle.get_tangent_vector(0)

	A=Intersection(vP,tangente)[0]
	tg_theta=Segment(O,A)
	tg_theta.parameters.color=theta.parameters.color
	tg_theta.parameters.style="dashed"

	B=Intersection(vQ,tangente)[0]
	tg_phi=Segment(O,B)
	tg_phi.parameters.color=phi.parameters.color
	tg_phi.parameters.style="dashed"

	vertical=Segment(A,B).dilatation(1.5)

	A.put_mark(0.1,0,r"$\tan(\theta)$",automatic_place=(pspict,"W"))
	B.put_mark(0.1,0,r"$\tan(\varphi)$",automatic_place=(pspict,"W"))
	A.parameters.color=vP.parameters.color
	B.parameters.color=vQ.parameters.color

	pspict.DrawGraphs(tg_theta,tg_phi,Cercle,theta,phi,vP,vQ,vertical,A,B)
	pspict.axes.no_graduation()
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
