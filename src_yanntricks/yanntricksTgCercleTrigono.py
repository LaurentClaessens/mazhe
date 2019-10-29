from yanntricks import *
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

    theta=AngleAOB(X,O,P)
    theta.put_mark(text=r"$\theta$",pspict=pspict)
    theta.parameters.color=vP.parameters.color

    #phi=Angle(X,O,Q,theta.r+0.5)
    phi=AngleAOB(X,O,Q)
    phi.set_mark_angle(0.5*(90+phi.angleF.degree))
    phi.put_mark(text=r"$\varphi$",pspict=pspict)
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

    A.put_mark(0.2,text=r"$\tan(\theta)$",pspict=pspict,position="W")
    B.put_mark(0.2,text=r"$\tan(\varphi)$",pspict=pspict,position="W")
    A.parameters.color=vP.parameters.color
    B.parameters.color=vQ.parameters.color

    pspict.DrawGraphs(tg_theta,tg_phi,Cercle,theta,phi,vP,vQ,vertical,A,B)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

