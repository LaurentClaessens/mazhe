from yanntricks import *

def YWxOAkh():
    pspict,fig = SinglePicture("YWxOAkh")
    pspict.dilatation_X(4)

    x=var('x')
    epsilon=0.005
    mx=epsilon
    Mx=0.5
    f2=phyFunction(sin(1/x))
    x0=epsilon
    x1=1
    F2=f2.graph(x0,Mx)
    F2.linear_plotpoints=5000
    F2p=f2.graph(-Mx/2,-mx)
    F2p.linear_plotpoints=F2.linear_plotpoints
    
    pspict.DrawGraphs(F2)
    
    pspict.axes.Dx=0.5
    pspict.DrawDefaultAxes()
    pspict.comment="Enough plotpoints ? There were 5000."
    
    fig.conclude()
    fig.write_the_file()

