from yanntricks import *
import yanntricksCommuns as Communs


def TraceCycloide():
    x = var('x')
    f1 = phyFunction(x+cos(x))
    f2 = phyFunction(1+sin(x))
    curve = ParametricCurve(f1, f2).graph(0, 2*pi)
    curve.parameters.color = "blue"
    LLms = [0, pi, 3*pi/2, 2*pi, pi/4, 3*pi/4, 5*pi/4, 7*pi/4]

    Communs.CorrectionParametrique(curve, LLms, "TraceCycloide")
