from yanntricks import *


def PLTWoocPNeiZir():
    pspict, fig = SinglePicture("PLTWoocPNeiZir")
    pspict.dilatation(1)

    ell = Segment(Point(0, 0), Point(3, 2))
    P = ell.get_point_proportion(0.7)
    P.put_mark(0.2, angle=None, added_angle=180, text=r"\( P\)", pspict=pspict)

    ell_perp = ell.orthogonal(point=P)
    ell_perp.parameters.style = "dashed"

    for p in [0.3, 0.5, 0.7]:
        C = ell_perp.get_point_proportion(p)
        circle = CircleOA(C, P)
        circle.parameters.color = "red"
        pspict.DrawGraphs(circle)

    pspict.DrawGraphs(P, ell, ell_perp)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
