from yanntricks import *
def DeuxCercles():
    pspict,fig = SinglePicture("DeuxCercles")
    pspict.dilatation(2)

    A=Point(0,0.5)
    B=Point(0.5,0)
    C1=Circle(A,0.5)
    C2=Circle(B,0.5)

    l1=C1.parametric_curve(-pi/2,0)
    l2=C2.parametric_curve(pi/2,-pi)
    l1.parameters.color="red"
    l2.parameters.color="red"

    surf=CustomSurface(l1,l2)
    surf.parameters.hatched()
    surf.parameters.hatch.color="lightgray"

    pspict.DrawGraphs(surf,C1,C2,l1,l2)

    pspict.axes.Dx=0.5
    pspict.axes.Dy=0.5
    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

