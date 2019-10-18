from yanntricks import *
def DivergenceTrois():
    pspict,fig = SinglePicture("DivergenceTrois")

    O=Point(0,0)
    r1=1
    r2=2.2
    alphaI=0.5
    alphaF=180
    C1=Circle(O,r1).graph(alphaI,alphaF)
    C2=Circle(O,r2).graph(alphaI,alphaF)

    C1.parameters.filled()
    C1.parameters.fill.color="white"
    C2.parameters.filled()
    C2.parameters.fill.color="cyan"

    pspict.DrawGraphs(C2,C1)

    draw_points1=C1.get_regular_points(alphaI,alphaF,0.25,advised=False)
    draw_points2=C2.get_regular_points(alphaI,alphaF,0.25,advised=False)

    l=1
    x,y=var('x,y')
    F=VectorField(l*x/(x**2+y**2),l*y/(x**2+y**2))
    F1=F.graph(draw_points=draw_points1)
    F2=F.graph(draw_points=draw_points2)

    pspict.DrawGraphs(F1,F2)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

