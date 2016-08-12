from phystricks import *
def TriangleUV():
    pspict,fig = SinglePicture("TriangleUV")

    x=var('x')
    l=3
    O=Point(0,0)
    A=Point(0,l)
    B=Point(l,0)

    u=Vector(Point(1,0))
    v=Vector(Point(0,1))
    u.parameters.color="green"
    v.parameters.color="red"
    u.put_mark(0.1,-90,"\( e_u\)",pspict=pspict)
    v.put_mark(0.1,180,"\( e_v\)",pspict=pspict)

    #P=Segment(A,B).center()
    #Q=P.translate( Segment(O,A).fix_length(0.2) )
    #t=AffineVector(B,A)

    d=Vector(Segment(B,A).center()).fix_size(0.3)
    n=Segment(B,A).get_normal_vector()
    t=Segment(B,A).get_tangent_vector()
    n=-n.translate(d)
    t=t.translate(d)
    n.parameters.color=u.parameters.color
    t.parameters.color=v.parameters.color

    
    n.put_mark(0.1,n.advised_mark_angle(pspict),"\( \\nu\)",pspict=pspict)
    t.put_mark(0.1,n.advised_mark_angle(pspict),"\( T\)",pspict=pspict)

    Trig=Polygon(O,A,B)
    Trig.parameters.style="none"
    Trig.parameters.hatched()
    Trig.parameters.hatch.color="blue"

    pspict.axes.no_graduation()
    pspict.DrawGraphs(Trig,u,v,n,t)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
