from sage.all import binomial
from yanntricks import *


def proba(n, p, k):
    return binomial(n, k)*p**k*(1-p)**(n-k)


def YYECooQlnKtD():
    pspict, fig = SinglePicture("YYECooQlnKtD")
    # pspict.dilatation_X(1)
    # pspict.dilatation_Y(1)
    pspict.dilatation_Y(10)

    n = 10
    p = 0.7                   # attention : nombres notés dans le texte.
    for k in range(0, n+2):
        P = Point(k, proba(n, p, k))
        P.parameters.symbol = "*"
        pspict.DrawGraphs(P)

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
