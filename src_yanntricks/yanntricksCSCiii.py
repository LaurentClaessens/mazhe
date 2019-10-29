from yanntricks import *


def CSCiii():
    pspict, fig = MultiplePictures("CSCiii", 3)
    pspict[0].mother.caption = u"La première branche pour les angles positifs."
    pspict[1].mother.caption = u"Quelques autres branches pour les angles positifs."
    pspict[2].mother.caption = u"Le dessin au complet"

    pspict[0].dilatation(3)
    pspict[1].dilatation(30)
    pspict[2].dilatation(3)

    nBranches = 5

    x = var('x')
    f = sin(x)/x
    curve = PolarCurve(f)
    branch = [curve.graph(0.01, pi)]
    colors = ["brown", "cyan", "green", "magenta", "gray"]
    for k in range(1, nBranches):
        c = curve.graph(2*k*pi, (2*k+1)*pi)
        # c.linear_plotpoints=
        c.parameters.color = colors[k]
        branch.append(c)

    pspict[0].DrawGraphs(branch[0])
    for i in range(1, nBranches):
        pspict[1].DrawGraphs(branch[i])

    pspict[0].axes.single_axeX.Dx = 0.5
    pspict[0].axes.single_axeY.Dx = 0.5

    pspict[1].axes.single_axeX.Dx = 0.05
    pspict[1].axes.single_axeY.Dx = 0.1

    for br in branch:
        minus = curve.graph(-br.mx, -br.Mx)
        minus.parameters.color = "red"
        pspict[2].DrawGraphs(br, minus)

    pspict[2].axes.single_axeX.Dx = 0.5
    pspict[2].axes.single_axeY.Dx = 0.5

    for psp in pspict:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
