from phystricks import *
def SenoTopologo():
    pspict,fig = SinglePicture("SenoTopologo")
    pspict.dilatation(5)

    a=-0.5
    b=0.5
    x=var('x')
    f=phyFunction(x*sin(1/x))
    G=f.graph(a,b)
    G.linear_plotpoints=2000
    pspict.DrawGraphs(G)
    pspict.axes.Dx=0.3
    pspict.axes.Dy=0.3
    pspict.DrawDefaultAxes()


    fig.conclude()
    fig.write_the_file()
