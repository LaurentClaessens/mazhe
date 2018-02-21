from phystricks import *
def IntEcourbe():
    pspict,fig = SinglePicture("IntEcourbe")

    x=var('x')
    f1=phyFunction((x-2)**2+2.5).graph(1,3)
    f2=phyFunction(sin(x)+0.5).graph(1,3)

    surface=SurfaceBetweenFunctions(f1,f2,1,3)
    surface.parameters.hatched()
    surface.parameters.hatch.color="green"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters

    pspict.DrawGraphs(f1,f2,surface,surface.bounding_box(pspict))
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
