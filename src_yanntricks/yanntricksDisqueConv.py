from yanntricks import *
def DisqueConv():
    pspict,fig = SinglePicture("DisqueConv")

    x=var('x')
    Z=Point(2,2)
    C=Circle(Z,1)

    Z.put_mark(0.1,225,"$z_0$",pspict=pspict)
    C.parameters.color="red"
    C.parameters.hatched()
    C.parameters.hatch.color="green"

    pspict.axes.no_graduation()
    pspict.DrawGraphs(Z,C)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

