# -*- coding: utf8 -*-
from phystricks import *


def rotate_point(P):
    """Return a rotation of the given point."""
    z = P.x + I * P.y
    new_z = exp(I*pi/3)*z

    return Point(new_z.real_part(), new_z.imag_part())

def rotate_polygon(polygon):
    """Return the rotation of the given polygon."""

    new_points_list = [rotate_point(P) for P in polygon.points_list]
    return Polygon(new_points_list)

def AUMZoodbKuHtXe():
    pspict, fig = SinglePicture("AUMZoodbKuHtXe")
    pspict.dilatation(1)

    A = Point(0, 0)
    B = Point(1, 0)
    C = Point(0.5, sqrt(3)/6)

    triangles = [Polygon(A, B ,C)]

    for i in range(0, 5):
        triangles.append( rotate_polygon(triangles[-1]) )

    pspict.DrawGraphs(triangles)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
