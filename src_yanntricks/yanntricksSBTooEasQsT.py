#!../venv/bin/python3

import numpy

import dirmanage
from yanntricks import SinglePicture
from yanntricks import phyFunction
from sage.all import var, exp
_ = dirmanage, exp


dprint = print


def SBTooEasQsT():
    pspict, fig = SinglePicture("SBTooEasQsT")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.1)

    x = var('x')
    for c in numpy.linspace(-5, 5, 10):
        dprint("fait pour ", c)
        f = phyFunction(c*exp(x)).graph(-4, 2)
        pspict.DrawGraphs(f)

    pspict.axes.single_axeY.Dx = 10
    pspict.grid.Dy = 5
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    # fig.no_figure()
    fig.conclude()
    fig.write_the_file()


SBTooEasQsT()
