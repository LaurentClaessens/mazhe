from yanntricks import *
def CbCartTui():
    pspict,fig = SinglePicture("CbCartTui")
    pspict.dilatation(0.7)

    x=var('x')
    f1=phyFunction(x+1/x)
    f2=phyFunction(x+1/x**2)

    courbe=ParametricCurve(f1,f2)
    c1=courbe.graph(-5,-0.5)

    c2=courbe.graph(0.5,1)
    c3=courbe.graph(1,5)
    c1.put_arrow(-4.8,-3,-2,-0.7)
    c2.put_arrow(0.6,0.8)
    c3.put_arrow(1.2,2,3)

    pspict.DrawGraphs(c1,c2,c3)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

