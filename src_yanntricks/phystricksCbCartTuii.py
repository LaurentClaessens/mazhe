from yanntricks import *
def CbCartTuii():
    pspict,fig = SinglePicture("CbCartTuii")
    pspict.dilatation(2)

    x=var('x')
    f1=phyFunction(cos(x)**2)
    f2=phyFunction(cos(x)**3*sin(x))

    courbe=ParametricCurve(f1,f2).graph(0,2*pi)
    

    pspict.DrawGraphs(courbe)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

