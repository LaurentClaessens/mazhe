from yanntricks import *
def SurfaceCercle():
    pspict,fig = SinglePicture("SurfaceCercle")

    r=2
    x=var('x')
    f1=phyFunction(sqrt(r**2-x**2)).graph(-r,r)
    f2=phyFunction(-sqrt(r**2-x**2)).graph(-r,r)
    f2.parameters.color="red"

    pspict.DrawGraphs(f1,f2)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

