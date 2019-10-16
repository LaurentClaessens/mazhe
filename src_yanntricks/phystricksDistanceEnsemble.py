from yanntricks import *
def DistanceEnsemble():
    pspict,fig = SinglePicture("DistanceEnsemble")
    pspict.dilatation(2)

    C=Point(0,0)
    Cercle=Circle(C,1)
    A=Cercle.get_point(45)
    A.put_mark(0.3,45,"$A$",pspict=pspict)
    A.parameters.symbol=""
    pspict.DrawGraphs(A)
    P=Cercle.get_point(210)
    Q=Cercle.get_point(100)
    P.put_mark(0.5,-90,"$p$",pspict=pspict)
    R=Circle(C,0.7).get_point(-90)
    v=AffineVector(C,P)
    X=(v*2.3).F
    X.put_mark(0.3,180,"$x$",pspict=pspict)

    xP=Segment(X,P)
    xQ=Segment(X,Q)
    xR=Segment(X,R)
    xQ.parameters.style="dotted"
    xR.parameters.style="dotted"
    pspict.DrawGraphs(xP)
    pspict.DrawGraphs(xQ)
    pspict.DrawGraphs(xR)

    pspict.DrawGraphs(Cercle)
    pspict.DrawGraphs(P)
    pspict.DrawGraphs(R)
    pspict.DrawGraphs(Q)
    pspict.DrawGraphs(X)

    fig.conclude()
    fig.write_the_file()

