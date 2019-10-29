from yanntricks import *
def AireParabole():
    pspict,fig = SinglePicture("AireParabole")

    x=var('x')
    f=phyFunction(x**2-x).graph(-1,3)
    seg=Segment(Point(2,-1),Point(2,3))

    pspict.DrawGraphs(f,seg)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

