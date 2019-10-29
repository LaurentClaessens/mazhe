from yanntricks import *
def DivergenceDeux():
    pspict,fig = SinglePicture("DivergenceDeux")

    x,y=var('x,y')

    import numpy
    pos_x=numpy.linspace(-4,4,15)
    pos_y=numpy.linspace(-4,4,15)

    l=(1.0/3)
    draw_points=[  Point(xx,yy) for xx in pos_x for yy in pos_y if xx!=0 or yy!=0]

    F=VectorField(l*y/sqrt(x**2+y**2),l*-x/sqrt(x**2+y**2)).graph(draw_points=draw_points)

    pspict.DrawGraphs(F)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

