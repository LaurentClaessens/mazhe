from sage.all import factorial
from yanntricks import *


def proba(l, k):
    return exp(-l)*(l**k/factorial(k))


def UGCFooQoCihh():
    pspict, fig = SinglePicture("UGCFooQoCihh")
    pspict.dilatation_Y(10)

    l = 2
    for k in range(0, 10):
        P = Point(k, proba(l, k))
        P.parameters.symbol = "*"
        pspict.DrawGraphs(P)

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
