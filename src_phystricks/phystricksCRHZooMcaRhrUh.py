# -*- coding: utf8 -*-

from __future__ import division

import itertools

from phystricks import *


def action(k, l, m, P):
    """Act with the group on the point P"""
    z = P.x+I*P.y
    new_z = exp(i*pi*2*m/3)*z
    new_P = Point(new_z.real_part(), new_z.imag_part())

    new_P = new_P + l * Point(-1/2, sqrt(3)/2)
    new_P = new_P + k * Point(1, 0)

    return new_P


def move_polygon(k, l, m, polygon):
    """Move the polygon with the group."""
    new_vertices = [action(k, l, m, P) for P in polygon.vertices]
    return Polygon(new_vertices)


def CRHZooMcaRhrUh():
    pspict, fig = SinglePicture("CRHZooMcaRhrUh")
    # pspict.dilatation_X(1)
    # pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A = Point(0, 0)
    B = Point(1/2, -sqrt(3)/6)
    C = Point(1, 0)
    D = Point(1/2, sqrt(3)/6)

    base = Polygon(A, B, C, D)

    rotated_polys = [move_polygon(0, 0, k, base) for k in [0, 1, 2]]
    
    max_translate = 3
    K = range(-max_translate, max_translate + 1)
    L = range(-max_translate, max_translate + 1)
    M = [0, 1, 2]

    print(action(0,0,1,Point(1,0)))
    print(action(0,0,2,Point(1,0)))
    print(action(0,0,3,Point(1,0)))
    print(action(0,0,4,Point(1,0)))

    polys = []
    for k,l,m in itertools.product(K, L, M):
        polys.append(move_polygon(k,l,m,base))
        

    pspict.DrawGraphs(polys)

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
