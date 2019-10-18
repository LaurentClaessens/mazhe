from yanntricks import *
def AdhIntFrDeux():
    pspict,fig = SinglePicture("AdhIntFrDeux")

    x=var('x')
    mx=-0.5
    Mx=3
    f1=phyFunction(x+1)
    f2=phyFunction(2*x)
    pts = Intersection(f1,f2)
    x0=pts[0].x
    F1=f1.graph(mx,Mx)
    F2=f2.graph(mx,Mx)
    F1.parameters.color="gray"
    F1.parameters.style="dashed"
    F2.parameters=F1.parameters

    P=f1.get_point(x0)
    Cer=Circle(P,0.7)

    A=SurfaceBetweenFunctions(f1,f2,x0,Mx)
    A.parameters.hatched()
    A.parameters.hatch.color="red"
    A.curve1.parameters.color="blue"
    A.curve1.parameters.style="solid"
    A.curve2.parameters = A.curve1.parameters

    #A.Fsegment.parameters.style="none"

    pspict.DrawGraphs(F1,F2,A,P,Cer)

    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

