from phystricks import *
def IntRectangle():
    pspict,fig = SinglePicture("IntRectangle")
    pspict.dilatation(1)

    x=var('x')
    l=1
    h=2
    f=phyFunction(h).graph(0,l)
    f.parameters.color="red"
    surface=SurfaceUnderFunction(f,0,l)
    surface.parameters.filled()
    surface.parameters.fill.color="green"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.Fsegment.parameters.style="solid"
    surface.Fsegment.parameters.color="red"

    pspict.DrawGraphs(surface,f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
