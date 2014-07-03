from phystricks import *
def IntEcourbe():
    pspict,fig = SinglePicture("IntEcourbe")

    x=var('x')
    f1=phyFunction((x-2)**2+2.5)
    f2=phyFunction(sin(x)+0.5)

    surface=SurfaceBetweenFunctions(f1,f2,1,3)
    surface.parameters.color="green"
    surface.curve1.parameters.style="solid"
    surface.curve1.parameters.color="red"
    surface.curve2.parameters=surface.curve1.parameters


    pspict.DrawGraphs(surface,surface.bounding_box(pspict))
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
