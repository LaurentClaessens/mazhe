from yanntricks import *
def DS2010exo1():
    pspict,fig = SinglePicture("DS2010exo1")

    mx=-1
    Mx=4
    x=var('x')
    droite=phyFunction(3-x).graph(mx,Mx)
    cercle=Circle(Point(0,0),3).graph(-20,110)
    horiz=phyFunction(1).graph(mx,Mx)

    cercle.parameters.color="red"
    droite.parameters.color="red"
    horiz.parameters.color="red"

    pts=Intersection(cercle,horiz)
    xA=Intersection(horiz,droite)[0].x
    xB=pts[1].x
    theta=pts[1].angle()
    surface=CustomSurface(horiz.graph(xA,xB),cercle.graph(theta,90),droite.graph(0,3))

    I1=Intersection(droite,horiz)[0]
    I2=Intersection(cercle,horiz)[1]
    I1.put_mark(0.3,220,"$A$",pspict=pspict)
    I2.put_mark(0.3,45,"$B$",pspict=pspict)

    surface.parameters.color="lightgray"
    surface.parameters.filled()

    pspict.DrawGraphs(surface,droite,cercle,horiz,I1,I2)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

