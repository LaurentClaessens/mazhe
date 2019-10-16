from yanntricks import *
def SolsEqDiffSin():
    pspict,fig = SinglePicture("SolsEqDiffSin")

    epsilon=0.01
    mx=-pi/2-epsilon
    Mx=pi/2+epsilon
    x=var('x')
    f1=phyFunction(sin(x)).graph(mx,Mx)
    f2=phyFunction(1).graph(mx,Mx)
    f3=phyFunction(-1).graph(mx,Mx)
    f1.parameters.color="red"
    f2.parameters.color="blue"
    f3.parameters.color="green"

    pspict.axes.single_axeX.axes_unit=AxesUnit(pi,"")
    pspict.axes.single_axeX.Dx=0.5

    pspict.DrawGraphs(f1,f2,f3)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

