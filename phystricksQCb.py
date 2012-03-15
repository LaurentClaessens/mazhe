from __future__ import division
from phystricks import *
def QCb():
    pspict,fig = SinglePicture("QCb")

    x=var('x')
    l=2
    O=Point(0,0)
    E=Point(l,0)
    N=Point(0,l)

    a=Point(-l/2,l/2)
    b=Point(l/2,l/2)
    c=Point(l/2,-l/2)
    d=Point(-l/2,-l/2)

    a.put_mark(0,0,"\( xy\)")
    b.put_mark(0,0,"\( \sin(xy)\)")
    c.put_mark(0,0,"\( xy\)")
    d.put_mark(0,0,"\( xy\)")

    for el in [a,b,c,d]:
        el.parameters.symbol="none"

    OE=Segment(O,E)
    NO=Segment(O,N)


    for el in [OE,NO]:
        el.wave(0.1,0.07)
        el.parameters.color="red"

    pspict.DrawGraphs(OE,NO,a,b,c,d)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
