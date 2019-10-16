# -*- coding: utf8 -*-
from yanntricks import *
def ROAOooPgUZIt():
    pspict,fig = SinglePicture("ROAOooPgUZIt")
    a=3
    R=1
    C = Point(0,a)
    cercle = Circle(C,R)
    cercle.parameters.color="brown"

    O = Point(0,0)
    measure = MeasureLength(Segment(O,C),R+0.5)
    measure.put_mark(0.3,measure.advised_mark_angle(pspict),"$a$",pspict=pspict)

    rayon = Segment(C,cercle.get_point(30))
    rayon.parameters.color="red"
    rayon.put_mark(0.3,rayon.advised_mark_angle(pspict),"$R$",pspict=pspict)

    seg = Segment(C,measure.F)
    seg.parameters.color="blue"
    seg.parameters.style="dotted"

    pspict.DrawGraphs(cercle,measure,C,rayon,seg)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

