from yanntricks import *
def LBGooAdteCt():
    pspict,fig = SinglePicture("LBGooAdteCt")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(exp(x)).graph(-5,5)
    f.cut_y(-1,5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
