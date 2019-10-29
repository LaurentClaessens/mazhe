# -*- coding: utf8 -*-
from yanntricks import *
def DDCTooYscVzA():
    pspict,fig = SinglePicture("DDCTooYscVzA")
    pspict.dilatation(2)

    x=var('x')
    contour=PolarCurve(1+cos(x)*sin(x)).graph(0,2*pi)

    pts = contour.getRegularLengthParameters(0,2*pi,1,initial_point=True)

    for llam in pts:
        t = contour.get_tangent_vector(llam).normalize(0.5)

        # In this particular case, I need to change the sign of the produced normal vector :
        n = -contour.get_normal_vector(llam,Green_convention=True).normalize(0.5)
        n.parameters.color="green"
        t.parameters.color="red"
    pspict.DrawGraphs(t,n)

    contour.put_arrow(pts)

    pspict.DrawGraphs(contour)
    fig.conclude()
    fig.write_the_file()

