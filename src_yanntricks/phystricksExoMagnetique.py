from yanntricks import *
def ExoMagnetique():
    pspict,fig = SinglePicture("ExoMagnetique")

    fil=Segment(Point(0,-2),Point(0,2))
    fil.parameters.style="dashed"
    I=Vector(0,1)
    I.parameters.color="red"
    I.put_mark(0.3,0,"$I$",pspict=pspict)

    P=Point(-2,1)
    P.put_mark(0.2,135,r"$(r,\theta,z)$",pspict=pspict)
    d=AffineVector(P.projection(I),P)
    d.put_mark(0.2,-45,"$d$",pspict=pspict)
    d.parameters.color="blue"

    pspict.DrawGraphs(fil,I,d,P)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

