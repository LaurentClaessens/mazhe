from yanntricks import *
def CercleImplicite():
    pspict,fig = SinglePicture("CercleImplicite")

    x=var('x')
    R=2
    C=Circle(Point(0,0),R)
    P=C.get_point(45)
    Pp=C.get_point(-45)
    Q=C.get_point(180)

    X=P.projection(pspict.axes.single_axeX)
    X.put_mark(0.3,180+45,"\( x\)",pspict=pspict)

    P.put_mark(0.3,P.advised_mark_angle(pspict),"$P$",pspict=pspict)
    Pp.put_mark(0.3,Pp.advised_mark_angle(pspict),"\( P'\)",pspict=pspict)

    Q.put_mark(0.3,180-45,"\( Q\)",pspict=pspict)

    vert=Segment(P,Pp)
    vert.parameters.style="dotted"
    vert.parameters.color="red"

    pspict.axes.no_graduation()
    pspict.DrawGraphs(C,P,Pp,Q,X,vert)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

