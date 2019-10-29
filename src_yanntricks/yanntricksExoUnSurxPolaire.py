from yanntricks import *
def ExoUnSurxPolaire():
    pspict,fig = SinglePicture("ExoUnSurxPolaire")

    x=var('x')
    f=phyFunction(1/x)
    eps=0.25
    a=5

    f1=f.graph(-a,-eps)
    f2=f.graph(eps,a)

    pspict.DrawGraphs(f1,f2)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

