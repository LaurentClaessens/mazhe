from yanntricks import *
def CouroneExam():
    pspict,fig = SinglePicture("CouroneExam")

    Origin=Point(0,0)
    C1=Circle(Origin,1)
    C2=Circle(Origin,2)

    surface=SurfaceBetweenParametricCurves(C1,C2,interval=(0,pi/2))
    surface.parameters.filled()
    surface.parameters.fill.color="lightgray"

    surface.parameters.color="blue"

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

