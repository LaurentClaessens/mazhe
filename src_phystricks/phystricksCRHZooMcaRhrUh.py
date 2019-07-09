# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *


def action(k, l, m, P):
    """Act with the group on the point P"""
    z = P.x+I*P.y
    new_z = exp(i*pi*2*m/3)*z
    new_P = Point(new_z.real_part(), new_z.imag_part())

    new_P = new_P + l * Point(-1/2, sqrt(3)/2)
    new_P = new_P + k * Point(1, 0)

    return new_P


def CRHZooMcaRhrUh():
    pspict,fig = SinglePicture("CRHZooMcaRhrUh")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A = Point(0,0)
    B = Point(1/2, -sqrt(3)/6)
    C = Point(1,0)
    D = Point(1/2, sqrt(3)/6)

    base = Polygon(A,B,C,D)

    pspict.DrawGraphs(base)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
