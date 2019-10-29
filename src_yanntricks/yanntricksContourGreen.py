from yanntricks import *
def ContourGreen():
    pspict,fig = SinglePicture("ContourGreen")

    x=var('x')
    contour=PolarCurve(1+cos(x)*sin(x)).graph(0,2*pi)
    contour.put_arrow([i*pi/4+0.5 for i in range(0,8)])

    pspict.DrawGraphs(contour)
    fig.conclude()
    fig.write_the_file()

