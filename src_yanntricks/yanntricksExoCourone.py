from yanntricks import *
def ExoCourone():
    pspict,fig = SinglePicture("ExoCourone")
    pspict.dilatation(1)

    Ra=1
    Rb=2

    A=Point(Ra,0)
    B=Point(Rb,0)

    A.put_mark(0.2,45,"$R_1$",pspict=pspict)
    B.put_mark(0.2,45,"$R_2$",pspict=pspict)

    x=var('x')
    curve1=ParametricCurve(Ra*cos(x),Ra*sin(x))
    curve2=ParametricCurve(Rb*cos(x),Rb*sin(x))

    surface=SurfaceBetweenParametricCurves(curve1,curve2,interval=(0,2*pi-0.0001))
    surface.parameters.filled()
    surface.parameters.fill.color="cyan"
    surface.Fsegment.parameters.style="none"
    surface.Isegment.parameters.style="none"
    #surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(surface,A,B)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.comment="Une couronne"

    fig.conclude()
    fig.write_the_file()

