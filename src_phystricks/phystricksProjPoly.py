from phystricks import *
def ProjPoly():
    pspict,fig = SinglePicture("ProjPoly")
    pspict.dilatation(0.5)

    x,y=var('x,y')
    F=ImplicitCurve(x**2-x-y**2-1==0,(x,-5,5),(y,-5,5))

    pspict.DrawGraphs(F)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
