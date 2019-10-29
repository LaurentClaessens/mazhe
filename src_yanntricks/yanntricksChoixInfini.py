from yanntricks import *


def ChoixInfini():
    pspict, fig = MultiplePictures("ChoixInfini", 2)

    x = var('x')
    d1 = Segment(Point(-3, 1), Point(3, 1))
    P1 = Point(1, 0)
    pspict[0].mother.caption = r"Ici le point à l'infini est la direction \( (1,0)\)."

    d2 = Segment(Point(-2, 0), Point(2, 2))
    P2 = Point(1, 1)
    pspict[1].mother.caption = r"Ici le point à l'infini est la direction \( (1,1)\)."

    d1.parameters.color = "blue"
    d2.parameters.color = "blue"
    P1.parameters.color = "blue"
    P2.parameters.color = "blue"

    pspict[0].DrawGraphs(d1, P1)
    pspict[0].DrawDefaultAxes()

    pspict[1].DrawGraphs(d2, P2)
    pspict[1].DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
