from yanntricks import *

dprint = print


def Phi(f):
    dprint("la fonction : ", f, type(f))
    prim = integrate(f, x)
    return 1+prim(x)-prim(0)


def XOLBooGcrjiwoU():
    pspict, fig = SinglePicture("XOLBooGcrjiwoU")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(300)

    x = var('x')
    f = sin(x)

    for i in range(1, 30):
        f = Phi(f)

    g = phyFunction(f(x)-exp(x)).graph(-10, 10)

    pspict.DrawGraphs(g)
    pspict.axes.single_axeX.Dx = 2
    pspict.axes.single_axeY.Dx = 0.005
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
