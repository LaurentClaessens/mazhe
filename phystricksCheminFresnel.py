from phystricks import *
def CheminFresnel():
    pspict,fig = SinglePicture("CheminFresnel")
    pspict.dilatation(1)

    x=var('x')
    R=2
    gamma1=ParametricCurve(x,0).graph(0,R)
    gamma2=PolarCurve(R).graph(0,pi/4)
    gamma3=ParametricCurve(x*cos(pi/4),x*sin(pi/4)).graph(0,R)

    gamma1.parameters.color="blue"
    gamma2.parameters.color=gamma1.parameters.color
    gamma3.parameters.color=gamma1.parameters.color
    

    pspict.DrawGraphs(gamma1,gamma2,gamma3)
    pspict.axes.no_numbering()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
