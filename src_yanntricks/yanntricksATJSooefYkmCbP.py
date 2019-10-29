import itertools
from yanntricks import *

def action(k, l, m, P):
    """Act with the group on the point P"""
    z = P.x+I*P.y
    new_z = exp(I*pi*m)*z

    new_P = Point(new_z.real_part(), new_z.imag_part())

    new_P = new_P + l * Point(-1/2, sqrt(3)/2)
    new_P = new_P + k * Point(1, 0)

    return new_P


def move_polygon(k, l, m, polygon):
    """Move the polygon with the group."""
    new_vertices = [action(k, l, m, P) for P in polygon.vertices]
    return Polygon(new_vertices)


def ATJSooefYkmCbP():
    pspict, fig = SinglePicture("ATJSooefYkmCbP")
    # pspict.dilatation_X(1)
    # pspict.dilatation_Y(1)
    pspict.dilatation(1)

    A = Point(0, 0)
    B = Point(1/2, 0)
    C = Point(1/2, 1)
    D = Point(0, 1)
    base = Polygon(A, B, C, D)
    rotated = move_polygon(0, 0, 1, base)

    pspict.DrawGraphs(base, rotated)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
