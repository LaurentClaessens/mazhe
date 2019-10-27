from yanntricks import *
def Trajs():
    pspict,fig = SinglePicture("Trajs")
    pspict.dilatation(1)

    x=var('x')
    colors=['red','green','blue','cyan','brown']
    for i,B in enumerate([-1,0,1,2]):
        f1=phyFunction(cos(x)+B*sin(x))
        f2=phyFunction(-sin(x)+B*cos(x))
        curve=ParametricCurve(f1,f2).graph(-1,1)
        curve.parameters.color=colors[i]
        P=curve.get_point(0)
        P.parameters.color="brown"
        pspict.DrawGraphs(curve,P)


    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

