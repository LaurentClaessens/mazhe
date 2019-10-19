from yanntricks import *
def Osculateur():
    pspict,fig = SinglePicture("Osculateur")

    x=var('x')
    f1=phyFunction(-20*cos(x))
    f2=phyFunction(2*sin(2*pi*x))
    llamI=0
    llamF=1
    curve=ParametricCurve(f1,f2).graph(llamI,llamF)
    
    LLms=[0.25,0.3,0.7]
    for llam in LLms :
        P=curve.get_point(llam)
        osculateur=curve.get_osculating_circle(llam)
        if abs(osculateur.radius)<3:
            pspict.DrawGraphs(P,osculateur)
    pspict.DrawGraphs(P)
    
    pspict.DrawGraphs(curve)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

