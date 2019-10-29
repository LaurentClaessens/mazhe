from yanntricks import *


def examsseptii():
    pspict, fig = SinglePicture("examsseptii")

    for x in range(0, 4):
        seg = Segment(Point(x**2, -2), Point(x**2, 2))
        seg.parameters.color = "blue"
        pspict.DrawGraphs(seg)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
