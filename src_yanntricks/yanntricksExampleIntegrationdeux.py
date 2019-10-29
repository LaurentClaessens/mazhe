from yanntricks import *
def ExampleIntegrationdeux():
    pspict,fig = SinglePicture("ExampleIntegrationdeux")
    
    a=-3
    b=-1
    e=0
    c=5
    d=6
    x=var('x')
    f=phyFunction(x-1)
    g=phyFunction(sqrt(2*x+6))
    h=phyFunction(-sqrt(2*x+6))
    F=f.graph(a,d)
    G=g.graph(a,d)
    H=h.graph(a,e)
    reg=SurfaceBetweenFunctions(f,g,b, c)
    reg.parameters.hatched()
    reg.parameters.hatch.color="red"
    reg1=SurfaceBetweenFunctions(g,h,a,b)
    reg1.parameters.hatched()
    reg1.parameters.hatch.color="green"
    F.parameters.style="solid"
    F.parameters.color="blue"
    G.parameters.style="solid"
    G.parameters.color="blue"
    H.parameters.style="solid"
    H.parameters.color="blue"

    pspict.DrawGraphs(reg, reg1, F, G, H)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

