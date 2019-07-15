# coding: utf8

from __future__ import division

import itertools

from phystricks import *


def action(k, l, m, P):
    """Act with the group on the point P"""
    z = P.x+I*P.y
    new_z = exp(i*pi*m/3)*z

    new_P = Point(new_z.real_part(), new_z.imag_part())

    new_P = new_P + l * Point(-1/2, sqrt(3)/2)
    new_P = new_P + k * Point(1, 0)

    return new_P


def move_polygon(k, l, m, polygon):
    """Move the polygon with the group."""
    new_vertices = [action(k, l, m, P) for P in polygon.vertices]
    return Polygon(new_vertices)


def PWMCooGWYCczZn():
    pspicts, fig = MultiplePictures("PWMCooGWYCczZn", 3)
    pspicts[0].mother.caption = "<+caption1+>"
    pspicts[1].mother.caption = "<+caption2+>"
    pspicts[2].mother.caption = "<+caption3+>"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)
    
    pspicts[1].dilatation(2)

    # subfigure 1

    A = Point(0, 0)
    B = Point(1/2, sqrt(3)/6)
    C = Point(1, 0)

    base = Polygon(A, B, C)

    triangles = [base]
    for m in [1, 2, 3, 4, 5]:
        triangles.append(move_polygon(0, 0, m, base))

    pspicts[0].DrawGraphs(triangles)

    # subfigure 2

    u1 = Point(1, 0)
    u2 = Point(1/2, sqrt(3)/2)
    Z = u1 + u2

    parallelogram = Polygon(Point(0,0), u1, Z, u2)

    T0 = move_polygon(0,0,0,base)
    T1 = move_polygon(1,0,1,base)
    T2 = move_polygon(1,0,2,base)
    T3 = move_polygon(2,1,3,base)
    T4 = move_polygon(1,1,4,base)
    T5 = move_polygon(1,1,5,base)

    T4.edges_parameters.color = "red"

    trigs = [T0, T1, T2, T3, T4, T5]

    pspicts[1].DrawGraphs(T0, T1, T2, T5, T3, T4)

    # subfigure 3


    pavage = [base]
    N = 3
    for k, l, m in itertools.product(range(-N, N+1),
                                     range(-N, N+1),
                                     [0, 1, 2, 3, 4, 5]):

        pavage.append(move_polygon(k, l, m, base))

    pspicts[2].DrawGraphs(pavage)

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
