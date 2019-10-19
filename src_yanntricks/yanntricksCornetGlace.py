from yanntricks import *
def CornetGlace():
    pspict,fig = SinglePicture("CornetGlace")

    l=1.2
    x=var('x')

    f1=phyFunction(sqrt(1-x**2)).graph(-1,1) # half-circle
    f2a=phyFunction(-x).graph(-l,0)
    f2b=phyFunction(x).graph(0,l)

    P = Intersection(f1,f2a)[0]
    Q = Intersection(f1,f2b)[0]

    c1=ParametricCurve(x,sqrt(1-x**2)).graph(P.x,Q.x).reverse()

    c2a=f2a.graph(P.x,0) # descending line
    c2b=f2b.graph(0,Q.x) # ascending line

    surf=CustomSurface(c2a,c2b,c1)
    surf.parameters.hatched()
    surf.parameters.hatch.color="lightgray"

    pspict.DrawGraphs(surf,f1,f2a,f2b)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
