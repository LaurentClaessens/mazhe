from yanntricks import *
def TriangleRectangle():
    pspict,fig = SinglePicture("TriangleRectangle")
    pspict.dilatation(4)

    B=Point(0,0)
    C=Point(1,0)
    A=Point(0.5,0.5*sqrt(3))

    A.put_mark(0.3,90,"$A$",pspict=pspict)
    B.put_mark(0.3,180,"$B$",pspict=pspict)
    C.put_mark(0.3,0,"$C$",pspict=pspict)

    AB=Segment(A,B)
    AC=Segment(A,C)
    BC=Segment(C,B)

    H=BC.midpoint()
    hauteur=Segment(A,H)
    hauteur.parameters.style="dotted"
    hauteur.parameters.color="blue"
    H.put_mark(0.3,-90,"$H$",pspict=pspict)

    angleS=AngleAOB(A,C,H)
    angleT=AngleAOB(H,A,C)
    angleS.parameters.color="red"
    angleT.parameters.color="cyan"
    angleS.put_mark(text="$60$",pspict=pspict)
    angleT.put_mark(text="$30$",pspict=pspict)

    pspict.DrawGraphs(AB,AC,BC,hauteur,angleS,angleT,A,B,C,H)
    fig.conclude()
    fig.write_the_file()

