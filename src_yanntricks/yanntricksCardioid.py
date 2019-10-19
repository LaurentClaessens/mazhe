from yanntricks import *
def Cardioid():
    pspict,fig = SinglePicture("Cardioid")
    
    x=var('x')
    a=1.5
    f=a*(1+cos(x))
    cardioid=PolarCurve(f).graph(0,2*pi)
    cardioid.parameters.color="red"

    pspict.DrawGraphs(cardioid)

    fig.conclude()
    fig.write_the_file()


