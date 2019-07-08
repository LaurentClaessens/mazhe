

import itertools
from phystricks import *


def rotate_point(P):
    """Return a rotation of the given point."""
    z = P.x + I * P.y
    new_z = exp(I*pi/3)*z
    return Point(new_z.real_part(), new_z.imag_part())


def tau1(P, n):
    return P + n * Point(1, 0)


def tau2(P, n):
    return P + n * Point(0.5, sqrt(3)/2)


def move_polygon(polygon, fun):
    """Return the rotation of the given polygon."""

    new_points_list = [fun(P) for P in polygon.points_list]
    return Polygon(new_points_list)


def AUMZoodbKuHtXe():
    pspict, fig = SinglePicture("AUMZoodbKuHtXe")
    pspict.dilatation(1)

    A = Point(0, 0)
    B = Point(1, 0)
    C = Point(0.5, sqrt(3)/6)

    base = Polygon(A, B, C)
    bases = [base]

    for i in range(0, 5):
        bases.append(move_polygon(bases[-1], rotate_point))

    triangles = []
    N = 1
    colors = ["blue", "red", "green", "yellow", "brown", "cyan"]
    for color, rotated in zip(colors, bases):
        for k, l in itertools.product(range(-N, N+1), range(-N, N+1)):
            trig = rotated
            trig = move_polygon(trig, lambda P: tau1(P, k))
            trig = move_polygon(trig, lambda P: tau2(P, l))
            trig.filled()
            trig.fill_parameters.color = color
            triangles.append(trig)

    pspict.DrawGraphs(base, rotated, triangles)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
