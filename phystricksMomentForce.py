from phystricks import *
def MomentForce():
    pspict,fig = SinglePicture("MomentForce")

    O=Point(0,0)
    O.put_mark(0.3,90,"$O$",automatic_place=pspict)
    origineF=Point(-1,-1)
    F=Vector(-2,-0.5).origin(origineF)
    R=AffineVector(O,origineF)

    F.put_mark(0.3,90,"$\overline{ F }$",automatic_place=pspict)
    R.put_mark(0.4,90,"$\overline{ R }$",automatic_place=pspict)

    D=O.projection(F)
    d=Segment(O,D)
    d.put_mark(0.3,d.advised_mark_angle(pspict),"$d$",automatic_place=pspict)
    d.parameters.style="dotted"
    d.parameters.color="blue"

    l=Segment(F.I,D).add_size(0,0.3)
    l.parameters.style="dashed"
    l.parameters.color="brown"

    pspict.DrawGraphs(O,R,F,d,l)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
