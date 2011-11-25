from phystricks import *
def CouroneExam():
    pspict,fig = SinglePicture("CouroneExam")

    Origin=Point(0,0)
    C1=Circle(Origin,1)
    C2=Circle(Origin,2)

    surface=SurfaceBetweenParametricCurves((C1,0,pi/2),(C2,0,pi/2))
    surface.parameters.color="blue"

    pspict.DrawGraphs(surface)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
