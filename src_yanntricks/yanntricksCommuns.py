from yanntricks import *


def CorrectionParametrique(curve, LLms, name, dilatation=1):
    fig = GenericFigure("SubfiguresCDU"+name, script_filename="Communs")

    ssfig1 = fig.new_subfigure(u"Quelques points de repères", "SS1"+name)
    pspict1 = ssfig1.new_pspicture(name+"psp1")
    ssfig2 = fig.new_subfigure(u"La courbe", "SS2"+name)
    pspict2 = ssfig2.new_pspicture(name+"psp2")

    for llam in LLms:
        P = curve(llam)
        tangent = curve.get_tangent_segment(llam)
        second = curve.get_second_derivative_vector(llam)
        normal = curve.get_normal_vector(llam)
        normal.parameters.color = "green"
        tangent.parameters.color = "brown"

        pspict1.DrawGraphs(P, second, tangent, normal)
        pspict2.DrawGraphs(P, tangent)

    curve.parameters.style = "dashed"
    pspict2.DrawGraphs(curve)
    pspict1.DrawDefaultAxes()
    pspict1.dilatation(dilatation)
    pspict2.DrawDefaultAxes()
    pspict2.dilatation(dilatation)

    fig.conclude()
    fig.write_the_file()
