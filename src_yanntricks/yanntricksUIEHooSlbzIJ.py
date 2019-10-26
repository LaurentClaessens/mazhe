from yanntricks import *


def proba(p, k):
    return p*(1-p)**k


def UIEHooSlbzIJ():
    pspict, fig = SinglePicture("UIEHooSlbzIJ")
    # pspict.dilatation_X(1)
    pspict.dilatation_Y(10)

    p = 0.4
    for k in range(0, 15):
        P = Point(k, proba(p, k))
        P.parameters.symbol = "*"
        pspict.DrawGraphs(P)

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
