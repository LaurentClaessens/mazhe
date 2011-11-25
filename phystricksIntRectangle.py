from phystricks import *
def IntRectangle():
    pspict,fig = SinglePicture("IntRectangle")

    x=var('x')
    l=1
    h=2
    f=phyFunction(h)
    surface=SurfaceUnderFunction(f,0,l)
    surface.parameters.color="green"
    surface.f1.parameters.style="solid"
    surface.f1.parameters.color="red"
    surface.Fsegment.parameters.style="solid"
    surface.Fsegment.parameters.color="red"

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
