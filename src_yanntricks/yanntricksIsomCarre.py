from yanntricks import *
def IsomCarre():
    pspict,fig = SinglePicture("IsomCarre")
    pspict.dilatation(1)

    x=var('x')
    A=Point(-1,1)
    B=Point(1,1)
    C=Point(1,-1)
    D=Point(-1,-1)
    A.put_mark(0.1,135,"\( A\)",pspict=pspict)
    B.put_mark(0.1,45,"\( B\)",pspict=pspict)
    C.put_mark(0.1,-45,"\( C\)",pspict=pspict)
    D.put_mark(0.1,-135,"\( D\)",pspict=pspict)

    l=0.5
    S=Segment(Point(0,-1-l),Point(0,1+l))
    E=S.F
    E.put_mark(0.1,45,"\( s\)",pspict=pspict)
    E.parameters.symbol=""
    Carre=Rectangle(A,C)
    Carre.edges_parameters.color="blue"

    pspict.DrawGraphs(Carre,S,A,B,C,D,E)
    fig.conclude()
    fig.write_the_file()

