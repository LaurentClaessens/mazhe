from phystricks import *
def ChiSquaresQuantile():
    pspict,fig = SinglePicture("ChiSquaresQuantile")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(50)

    mx=0
    Mx=30
    f=phyFunction(RealDistribution("chisquared",10).distribution_function).graph(mx,Mx)
    f.plotpoints=1000

    a=5
    b=16
    surface1 = SurfaceUnderFunction(f,mx,a)
    surface2 = SurfaceUnderFunction(f,b,Mx)

    #surface1.Fsegment.parameters.color="red"
    #surface2.Isegment.parameters.color="green"
    #surface1.curve1.parameters.color="yellow"
    #surface2.curve2.parameters.color="cyan"

    pspict.DrawGraphs(f,surface1,surface2)

    pspict.axes.single_axeX.Dx=5
    pspict.axes.single_axeY.Dx=0.05

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
