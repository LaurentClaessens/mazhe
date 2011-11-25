from phystricks import *
def Refraction():
    pspict,fig = SinglePicture("Refraction")

    O=Point(0,0)
    plan=Segment(Point(-3,0),Point(3,0))
    N=AffineVector(Point(0,-2),Point(0,2))
    N.put_mark(0.3,0,"$\overline{ N }$")

    A=Point(1,1)    
    B=Point(-2,-1)    
    a=AffineVector(A,O)
    b=AffineVector(O,B).normalize(a.length())
    a.parameters.color="red"
    b.parameters.color="blue"

    theta1=Angle(A,O,N.F)
    theta2=Angle(B,O,N.I)
    theta1.put_mark(0.3,theta1.advised_mark_angle,r"$\theta_1$")
    theta2.put_mark(0.3,theta2.advised_mark_angle,r"$\theta_2$")

    pspict.DrawGraphs(plan,N,theta1,theta2,a,b)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
