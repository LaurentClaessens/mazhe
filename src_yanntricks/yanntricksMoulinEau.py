# -*- coding: utf8 -*-
from yanntricks import *

def MoulinEau():
    pspicts,fig = MultiplePictures("MoulinEau",2)

    pspicts[0].mother.caption=u"L'eau pousse bien perpendiculairement à la palle du moulin."
    pspicts[1].mother.caption=u"Lorsque l'eau ne pousse pas perpendiculairement, une partie de la force est perdue."

    h=SR(2)
    P = Point(0,h)
    l=2

    x,y=var('x,y')
    courant=VectorField(-1,0).graph(xvalues=(x,-2,2,3),yvalues=(y,0,h,3))
    courant.parameters.color="blue"

    palle0 = Segment(P,P.get_polar_point(l,-90))
    Q=palle0.get_point_proportion(0.7)
    #v=AffineVector( Q, Point(Q.x-1,Q.y) )
    #v.parameters.color="blue"


    pspicts[0].DrawGraphs(palle0,courant)

    palle1 = Segment(P,P.get_polar_point(l,-130))
    Q=palle1.get_point_proportion(0.5)
    v=AffineVector( Q, Point(Q.x-1,Q.y) )
    vx,vy = v.decomposition(palle1)
    
    v.parameters.color="blue"
    vx.parameters.color="red"
    vy.parameters.color="green"

    pspicts[1].DrawGraphs(palle1,vx,vy,courant)

    fig.conclude()
    fig.write_the_file()

