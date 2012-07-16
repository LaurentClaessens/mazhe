from phystricks import *
def CbCartTuii():
    pspict,fig = SinglePicture("CbCartTuii")

    x=var('x')
    f1=phyFunction(cos(x)**2)
    f2=phyFunction(cos(x)**3*sin(x))

    courbe=ParametricCurve(f1,f2).graph(0,2*pi)
    

    pspict.DrawGraphs(courbe)
    pspict.DrawDefaultAxes()
    pspict.dilatation(2)
    fig.conclude()
    fig.write_the_file()
