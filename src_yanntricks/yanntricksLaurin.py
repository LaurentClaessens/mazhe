from yanntricks import *
def Laurin():
    pspict,fig = SinglePicture("Laurin")

    x=var('x')
    mx=-2
    Mx=2
    f=phyFunction(exp(x)).graph(mx,Mx)

    n=3
    F=[f]
    for i in range(n):
        F.append(phyFunction( f.sage.taylor(x,0,i) ).graph(mx,Mx))

    colors=["blue","cyan","green","red"]
    for i,g in enumerate(F):
        g.parameters.color=colors[i]
    pspict.DrawGraphs(g)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

