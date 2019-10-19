from sage.all import floor
from yanntricks import *
def PartieEntiere():
    pspict,fig = SinglePicture("PartieEntiere")

    x=var('x')
    f=phyFunction(floor(x)).graph(-2,3)
    f.linear_plotpoints=1000

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

