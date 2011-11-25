from phystricks import *
def IntegraleSimple():
    pspict,fig = SinglePicture("IntegraleSimple")


    a=-pi/2
    b=2*pi
    x=var('x')
    f=phyFunction(sin(x)+2).graph(a,b)
    A=Point(a,0)
    B=Point(b,0)

    A.put_mark(0.2,-90,"$a$",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"$b$",automatic_place=(pspict,"N"))

    surface=SurfaceUnderFunction(f,a,b)
    surface.Isegment.parameters.style="dashed"
    surface.Fsegment.parameters.style="dashed"
    surface.f1.parameters.style="solid"
    surface.f1.parameters.color="blue"
    surface.parameters.color="red"

    pspict.DrawGraphs(A,B,surface)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    pspict.DrawGraphs(A,B,surface)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
