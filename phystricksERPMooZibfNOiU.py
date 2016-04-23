# -*- coding: utf8 -*-
from phystricks import *


def ERPMooZibfNOiU():
    pspict,fig = SinglePicture("ERPMooZibfNOiU")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(1)

    t0=40
    a=2.3
    b=1.3
    O=Point(0,0)
    axeX=Segment( Point(-3,0),Point(3,0)  )
    lp=Segment( O,Circle(O,5).getPoint(t0)    )
    plp=lp.F
    plp.parameters.symbol=""
    plp.put_mark(0.2,angle=None,added_angle=0,text="\( \ell_p\)",automatic_place=(pspict,""))
    angle_t0=AngleAOB(axeX.F,O,lp.F)
    angle_t0.put_mark(0.3,angle=None,added_angle=0,text="\( \\alpha\)",automatic_place=(pspict,""))
    P=lp.midpoint()
    P.put_mark(0.2,angle=None,added_angle=180,text="\( P\)",automatic_place=(pspict,""))

    fun = lambda t:Point(a*cos(t),b*sin(t)).rotation(t0)+P 
    decal=fun(pi/2)-P
    Gamma = NonAnalyticPointParametricCurve( lambda x:fun(x)+decal  ,0,2*pi  )
    Gamma.parameters.plotpoints=20

    ss=[0.01,0.05]
    for s in ss:
        pt=Gamma(s)
        pspict.DrawGraphs(pt)

    pspict.DrawGraphs(axeX,lp,angle_t0,P,Gamma,plp)
    pspict.comment="l'ellipse est tangente à la droite au point P. La marque de P est à l'extérieur de l'ellipse."
    fig.conclude()
    fig.write_the_file()
