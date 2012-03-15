from phystricks import *
def ExoVarj():
    pspict,fig = SinglePicture("ExoVarj")

    x=var('x')
    g=sqrt(  sqrt(4*x**2+1)-x**2-1 )

    f1=phyFunction(g).graph(-1,1)
    f2=phyFunction(-g).graph(-1,1)

    f1.parameters.color="blue"
    f2.parameters.color="red"

    pspict.DrawGraphs(f1,f2)
    pspict.DrawDefaultAxes()
    pspict.dilatation(3)
    fig.conclude()
    fig.write_the_file()
