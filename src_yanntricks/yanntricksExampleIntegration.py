from yanntricks import *
def ExampleIntegration():
    pspict,fig = SinglePicture("ExampleIntegration")
    
    a=0
    b=(sqrt(5)+1)/2
    c=2
    x=var('x')
    f=phyFunction(x)
    g=phyFunction(x**2-1)
    F=f.graph(a,c)
    G=g.graph(a,c)
    reg=SurfaceBetweenFunctions(f,g,a,b)
    reg.parameters.hatched()
    reg.parameters.hatch.color="red"
    F.parameters.style="solid"
    F.parameters.color="blue"
    G.parameters.style="solid"
    G.parameters.color="blue"

    pspict.DrawGraphs(reg, F, G)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()


