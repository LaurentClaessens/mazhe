from phystricks import *
def ArcCercleAngle():
    pspict,fig = SinglePicture("ArcCercleAngle")

    R=2
    theta=-10
    sigma=60
    O=Point(0,0)
    cercle=Circle(O,R)
    cercle.parameters.style="dashed"
    
    arc=cercle.graph(theta,sigma)
    arc.parameters.color="blue"

    P=cercle.get_point(theta)
    Q=cercle.get_point(sigma)
    P.put_mark(0.3,P.advised_mark_angle,r"$\theta_0$",automatic_place=pspict)
    Q.put_mark(0.3,Q.advised_mark_angle,r"$\theta_1$",automatic_place=pspict)
    P.parameters.symbol=""
    Q.parameters.symbol=""
    M=cercle.get_point((sigma+theta)/2)
    M.put_mark(0.3,M.advised_mark_angle,"$\sigma(t)$",automatic_place=pspict)

    angle=Angle(P,O,Q,r=0.5)
    angle.put_mark(0.2,angle.advised_mark_angle,r"$\theta$",automatic_place=pspict)
    seg_theta=Segment(O,P)
    seg_sigma=Segment(O,Q)
    
    seg_sigma.put_mark(0.3,seg_sigma.advised_mark_angle,r"$R$",automatic_place=pspict)

    pspict.DrawGraphs(cercle,arc,angle,seg_theta,seg_sigma,P,Q)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
