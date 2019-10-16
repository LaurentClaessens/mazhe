from yanntricks import *
def CSCii():
    pspict,fig = SinglePicture("CSCii")

    x=var('x')
    f=sin(2*x)
    curve=PolarCurve(f)
    c1=curve.graph(0,pi/2)
    c2=curve.graph(pi,3*pi/2)

    P=Point(1,1)
    Q=Point(1,0)
    R=Point(0,1)
    l1=Segment(P,Q)
    l2=Segment(P,R)
    l1.parameters.color="lightgray"
    l2.parameters=l1.parameters

    pspict.DrawGraphs(c1,c2,l1,l2,P)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

