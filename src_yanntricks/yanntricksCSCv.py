from yanntricks import *

def CSCv():
    pspicts,fig = MultiplePictures("CSCv",2)

    pspicts[0].mother.caption=r"Le graphique de $r(\theta)$"
    pspicts[1].mother.caption=r"La courbe polaire correspondante"
    #ssfig1 = fig.new_subfigure(r"","CSCvGr")
    #pspict1 = ssfig1.new_pspicture("CSCvGraphe")

    x=var('x')
    r=phyFunction(cos(x)-cos(2*x)).graph(0,2*pi)
    pspicts[0].DrawGraphs(r)

    pspicts[0].DrawDefaultAxes()

    #ssfig2 = fig.new_subfigure("","CSCvCourbe")
    #pspict2 = ssfig2.new_pspicture("CSCvCourbe")

    curve1=PolarCurve(r).graph(0,2*pi/3)
    curve2=PolarCurve(r).graph(4*pi/3,2*pi)
    pspicts[1].DrawGraphs(curve1,curve2)

    pspicts[1].DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

