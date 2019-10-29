from yanntricks import *


def ParamTangente():
    pspict, fig = SinglePicture("ParamTangente")
    x = var('x')
    f1 = sqrt((2*x)**2)
    f2 = x**3
    mx = -1.5
    Mx = -mx
    curve = ParametricCurve(f1, f2).graph(mx, Mx)
    pspict.DrawGraphs(curve)
    lls = curve.getRegularLengthParameters(mx, Mx, 1.5)
    for ll in lls:
        Q = curve.get_point(ll)
        v = curve.get_tangent_vector(ll)
        v.parameters.color = "red"
        pspict.DrawGraphs(v)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
