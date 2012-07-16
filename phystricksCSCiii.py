# -*- coding: utf8 -*-

from phystricks import *
def CSCiii():
    pspict,fig = MultiplePictures("CSCiii",3)
    pspict[0].mother.caption=u"La première branche pour les angles positifs."
    pspict[1].mother.caption=u"Quelque autres branches pour les angles positifs."
    pspict[2].mother.caption=u"Le dessin au complet"

    nBranches=5

    x=var('x')
    f=sin(x)/x
    curve=PolarCurve(f)
    branch=[curve.graph(0.01,pi)]
    for i in range(1,nBranches):
        branch.append(curve.graph(2*i*pi,(2*i+1)*pi))

    pspict[0].DrawGraphs(branch[0])
    for i in range(1,nBranches):
        pspict[1].DrawGraphs(branch[i])

    pspict[0].axes.single_axeX.Dx=0.5
    pspict[0].axes.single_axeY.Dx=0.5


    pspict[1].axes.single_axeX.Dx=0.05
    pspict[1].axes.single_axeY.Dx=0.1


    for br in branch :
        minus = curve.graph(-br.mx,-br.Mx )
        minus.parameters.color="red"
        pspict[2].DrawGraphs(br,minus)

    pspict[2].axes.single_axeX.Dx=0.5
    pspict[2].axes.single_axeY.Dx=0.5

    for psp in pspict:
        psp.DrawDefaultAxes()

    pspict[0].dilatation(3)
    pspict[1].dilatation(30)
    pspict[2].dilatation(3)

    fig.conclude()
    fig.write_the_file()
