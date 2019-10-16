from yanntricks import *
def ExempleArcParam():
    fig = GenericFigure("ExempleArcParam")

    ssfigN1 = fig.new_subfigure("$\gamma(t)=(2\sin(t),t)$, avec $0\leq t\leq 2\pi$","LabelArcUn")
    ssfigN2 = fig.new_subfigure("$\gamma(t)=(sin(2t),sin(t))$ avec $-\pi\leq t\leq \pi$","LabelArcDeux")
    pspict1 = ssfigN1.new_pspicture("gammasintti")
    pspict2 = ssfigN2.new_pspicture("gammasindyttii")
    pspict1.dilatation(0.7)
    pspict2.dilatation(1.5)

    x=var('x')
    f1=2*sin(x)
    f2=x
    Mcurve1 = ParametricCurve(f1,f2)
    curve1 = Mcurve1.graph(0,2*pi)
    pspict1.DrawGraphs(curve1)
    pspict1.DrawDefaultAxes()


    g1=sin(2*x)
    g2=sin(x)
    curve2=ParametricCurve(g1,g2).graph(-pi,pi)
    pspict2.DrawGraphs(curve2)
    pspict2.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

