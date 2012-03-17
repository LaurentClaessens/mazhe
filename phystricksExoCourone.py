from phystricks import *
def ExoCourone():
    pspict,fig = SinglePicture("ExoCourone")

    Ra=1
    Rb=2

    A=Point(Ra,0)
    B=Point(Rb,0)

    A.put_mark(0.2,45,"$R_1$",automatic_place=pspict)
    B.put_mark(0.2,45,"$R_2$",automatic_place=pspict)

    x=var('x')
    curve1=ParametricCurve(Ra*cos(x),Ra*sin(x)).graph(0,2*pi)
    curve2=ParametricCurve(Rb*cos(x),Rb*sin(x)).graph(0,2*pi)

    surface=SurfaceBetweenParametricCurves(curve1,curve2)
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
    pspict.dilatation(1)

    fig.conclude()
    fig.write_the_file()
