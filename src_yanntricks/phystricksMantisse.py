from sage.all import floor
from yanntricks import *
def Mantisse():
    pspict,fig = SinglePicture("Mantisse")

    x=var('x')
    f=phyFunction(x-floor(x)).graph(0,5)
    f.linear_plotpoints=1000
    eps=0.01
    surf=SurfaceUnderFunction(f,1,2-eps)
    surf.parameters.filled()
    surf.parameters.fill.color="green"

    pspict.DrawGraphs(surf,f)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

