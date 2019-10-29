from yanntricks import *


def AdhIntFrSix():
    pspict, fig = SinglePicture("AdhIntFrSix")
    pspict.dilatation_X(4)
    pspict.dilatation_Y(4)

    N = 100
    for n in range(1, N):
        x = float(1)/n
        seg = Segment(Point(x, 0), Point(x, 1))
        seg.parameters.color = "blue"
        pspict.DrawGraphs(seg)
        seg = Segment(Point(0, 0), Point(0, 1))
        pspict.DrawGraphs(seg)

    P = Point(0, 0.8)
    Cer = Circle(P, 0.15)
    pspict.DrawGraphs(P, Cer)

    pspict.axes.Dx = 0.5
    pspict.axes.Dy = 0.5
    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
