# -*- coding: utf8 -*-
from yanntricks import *
def MCKyvdk():
    pspict,fig = SinglePicture("MCKyvdk")
    pspict.dilatation(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    pspict.DrawGraphs(cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

