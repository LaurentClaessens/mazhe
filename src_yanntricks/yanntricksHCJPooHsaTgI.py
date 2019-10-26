from yanntricks import *


def HCJPooHsaTgI():
    pspict, fig = MultiplePictures("HCJPooHsaTgI", 2)
    pspict[0].mother.caption = "Un domaine horizontal."
    pspict[1].mother.caption = "Un domaine vertical."

    a = 1
    b = 6
    A = Point(a, 0)
    B = Point(b, 0)

    x = var('x')
    f1 = phyFunction(sin(x)+4).graph(a, b)
    f2 = phyFunction(cos(x/2)*cos(2*x)+2).graph(a, b)
    f1.parameters.color = "blue"
    f2.parameters.color = "blue"

    surface = SurfaceBetweenFunctions(f1, f2, a, b)
    surface.parameters.hatched()
    surface.parameters.hatch.color = "red"
    surface.Isegment.parameters.style = "dashed"
    surface.Isegment.parameters.color = "magenta"
    surface.Fsegment.parameters = surface.Isegment.parameters
    surface.curve1.parameters.style = "solid"
    surface.curve1.parameters.color = "blue"
    surface.curve2.parameters = surface.curve1.parameters

    A.put_mark(0.2, text="$a$", pspict=pspict[0], position="N")
    B.put_mark(0.2, text="$b$", pspict=pspict[0], position="N")
    lA = Segment(A, f1.get_point(a))
    lB = Segment(B, f1.get_point(b))
    lA.parameters.style = "dotted"
    lB.parameters = lA.parameters

    pspict[0].DrawGraphs(surface, A, B, lA, lB, f1, f2,
                         surface.bounding_box(pspict[0]))
    pspict[0].axes.no_graduation()
    pspict[0].DrawDefaultAxes()
    pspict[0].dilatation(1)

    g1 = ParametricCurve(f1, x).graph(a, b)
    g2 = ParametricCurve(f2, x).graph(a, b)

    region = SurfaceBetweenParametricCurves(g1, g2, interval=(a, b))

    g1.parameters.style = "solid"
    g1.parameters.color = "blue"
    g2.parameters = g1.parameters

    region.Fsegment.parameters.color = "magenta"
    region.Fsegment.parameters.style = "dashed"
    region.Isegment.parameters = region.Fsegment.parameters
    region.parameters.hatched()
    region.parameters.hatch.color = "red"

    C = Point(0, a)
    D = Point(0, b)
    C.put_mark(0.2, text="$c$", pspict=pspict[1], position="E")
    D.put_mark(0.2, text="$d$", pspict=pspict[1], position="E")
    lC = Segment(C, g1.get_point(a))
    lD = Segment(D, g2.get_point(b))
    lC.parameters = lA.parameters
    lD.parameters = lA.parameters

    pspict[1].DrawGraphs(region, C, D, lC, lD, g1, g2,
                         region.bounding_box(pspict[1]))
    pspict[1].axes.no_graduation()
    pspict[1].DrawDefaultAxes()
    pspict[1].dilatation(1)

    fig.conclude()
    fig.write_the_file()
