# -*- coding: utf8 -*-
from phystricks import *
def ratrap():
    pspict,fig = SinglePicture("ratrap")
    pspict.dilatation(1)

    a=1
    b=2
    O=Point(0,0)

    c1 = Circle(O,a).parametric_curve(0,pi/2)
    c2 = Circle(O,b).parametric_curve(0,pi/2)

    surface = SurfaceBetweenParametricCurves(c1,c2,interval=(0,pi/2))

    surface.parameters.hatched()
    surface.parameters.hatch.color="blue"
    surface.parameters.color = "blue"

    Ax = Point(a,0)
    Bx = Point(b,0)
    Ay = Point(0,a)
    By = Point(0,b)

    Ax.put_mark(0.1,-90,"$a$",automatic_place=(pspict,"N"))
    Bx.put_mark(0.1,-90,"$b$",automatic_place=(pspict,"N"))
    Ay.put_mark(0.1,180,"$a$",automatic_place=(pspict,"E"))
    By.put_mark(0.1,180,"$b$",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(surface,Ax,Ay,Bx,By)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.comment="Une surface hachurée en bleu"
    fig.conclude()
    fig.write_the_file()
