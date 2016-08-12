from phystricks import *
def CercleImplicite():
    pspict,fig = SinglePicture("CercleImplicite")

    x=var('x')
    R=2
    C=Circle(Point(0,0),R)
    P=C.get_point(45)
    Pp=C.get_point(-45)
    Q=C.get_point(180)

    X=P.projection(pspict.axes.single_axeX)
    P.put_mark(0.1,P.advised_mark_angle(pspict),"$P$",pspict=pspict)
    Pp.put_mark(0.1,Pp.advised_mark_angle(pspict),"\( P'\)",pspict=pspict)
    Q.put_mark(0.1,Q.advised_mark_angle(pspict),"\( Q\)",pspict=pspict)
    X.put_mark(0.1,-90,"\( x\)",pspict=pspict)

    vert=Segment(P,Pp)
    vert.parameters.style="dotted"
    vert.parameters.color="red"

    pspict.axes.no_graduation()
    pspict.DrawGraphs(C,P,Pp,Q,X,vert)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
