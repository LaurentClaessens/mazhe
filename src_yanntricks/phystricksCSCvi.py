from yanntricks import *

def CSCvi():
    pspicts,fig = MultiplePictures("CSCvi",2)

    pspicts[0].mother.caption=r"Le graphique de $r(\theta)$"
    pspicts[1].mother.caption=r"La courbe polaire correspondante"

    #ssfig1 = fig.new_subfigure(r"","CSCviGr")
    #pspict1 = ssfig1.new_pspicture("CSCviGraphe")

    x=var('x')
    epsilon=0.4
    limite=-pi/2
    llam=limite+epsilon
    Llam=pi/2
    r=phyFunction(cos(x)/(1+sin(x)))

    graphe=r.graph(llam,Llam)

    P=Point(limite,0)
    Q=Point(limite,graphe.bounding_box().N().y)
    assymp=Segment(P,Q)
    assymp.parameters.color="lightgray"
    assymp.parameters.style="dashed"
    pspicts[0].DrawGraphs(graphe,assymp)

    pspicts[0].DrawDefaultAxes()

    #ssfig2 = fig.new_subfigure("","CSCviCourbe")
    #pspict2 = ssfig2.new_pspicture("CSCviCourbe")

    curve=PolarCurve(r).graph(llam,Llam)
    pspicts[1].DrawGraphs(curve)

    pspicts[1].DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

