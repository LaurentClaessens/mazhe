from yanntricks import *
def SolsSinpA():
    pspict,fig = SinglePicture("SolsSinpA")

    x=var('x')
    colors=['red','green','blue','cyan','brown']
    X=[-pi/2,-pi/4,0,pi/4,pi/2]
    for i,C in enumerate(X) :
        f=phyFunction(sin(x+C)).graph(-pi/2-C,pi/2-C)
        f.parameters.color=colors[i]
    pspict.DrawGraphs(f)

    pspict.axes.single_axeX.axes_unit=AxesUnit(pi,"")
    pspict.axes.single_axeX.Dx=0.5

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

