from sage.all import RealDistribution
from yanntricks import *
def ChiSquared():
    pspict,fig = SinglePicture("ChiSquared")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(50)

    f=phyFunction(RealDistribution("chisquared",10).distribution_function).graph(0,30)
    f.linearr_plotpoints=1000

    pspict.DrawGraphs(f)
    pspict.axes.single_axeX.Dx=5
    pspict.axes.single_axeY.Dx=0.05

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

