from yanntricks import *
def KScolorD():
    pspict,fig = SinglePicture("KScolorD")
    pspict.dilatation(1)

    x=var('x')
    C=Circle(Point(0,0),1)
    N1=C.graph(90,180)
    N2=C.graph(270,360)

    C.parameters.color="blue"
    N1.parameters.color="black"
    N2.parameters.color=N1.parameters.color
    N1.wave(0.1,0.2)
    #N2.wave(0.1,0.2)
    N=Point(0,1)
    S=Point(0,-1)

    pspict.axes.no_graduation()
    pspict.DrawGraphs(C,N1,N2,N,S)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

