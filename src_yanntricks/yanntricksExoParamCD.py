from yanntricks import *
def ExoParamCD():
    pspict,fig = SinglePicture("ExoParamCD")
    pspict.dilatation(3)
    
    x=var('x')
    f1=sin(2*x)
    f2=sin(3*x)

    courbe=ParametricCurve(f1,f2)
    courbe1=courbe.graph(0,pi)
    courbe2=courbe.graph(pi,2*pi)

    courbe1.parameters.color="blue"
    courbe2.parameters.color="red"

    for t in [0,pi/4,pi/2,3*pi/4,pi,5*pi/4,3*pi/2]:
        if t < pi:
           courbe1.put_arrow(t)
        else:
           courbe2.put_arrow(t)

    pspict.DrawGraphs(courbe1,courbe2)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

