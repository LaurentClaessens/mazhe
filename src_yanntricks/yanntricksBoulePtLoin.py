from yanntricks import *

dprint = print

def BoulePtLoin():
    pspict,fig = SinglePicture("BoulePtLoin")

    r=float(2)
    a=Point(0,0)
    a.put_mark(0.3,135,"$a$",pspict=pspict)
    cercle=Circle(a,r)
    x=cercle.get_point(45)
    x.put_mark(0.3,150,"$x$",pspict=pspict)
    v=AffineVector(a,x)
    delta=r/2
    N=4*(v.length/delta)/3

    P=x.translate(v/N)
    P.put_mark(0.3,-90,"$P$",pspict=pspict)
    B=Circle(x,delta)
    B.parameters.style="dotted"
    seg=Segment(x,P)
    seg.parameters.style="dashed"

    pspict.DrawGraphs(seg,a,x,v,B,P)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

