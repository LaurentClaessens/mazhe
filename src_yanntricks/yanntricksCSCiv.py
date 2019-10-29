from yanntricks import *
def CSCiv():
    pspict,fig = SinglePicture("CSCiv")

    x=var('x')
    f=(x-1)/(x+1)
    epsilon=0.5
    Mtheta=-50
    curve1=PolarCurve(f).graph(1,50)
    curve2=PolarCurve(f).graph(Mtheta,-1-epsilon)
    curve2.parameters.color="brown"
    curve1.linear_plotpoints=1000
    curve2.linear_plotpoints=1000

    pspict.DrawGraphs(curve1,curve2)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

