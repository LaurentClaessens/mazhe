from yanntricks import *
def AdhIntFrTrois():
    pspict,fig = SinglePicture("AdhIntFrTrois")
    pspict.dilatation_X(4)

    x=var('x')
    epsilon=0.005
    mx=epsilon
    Mx=2
    f1=phyFunction(3)
    f2=phyFunction(sin(1/x))
    #pts = Intersection(f1,f2)
    #x0=pts[0].x
    x0=epsilon
    x1=1
    F1=f1.graph(x1,Mx)
    F2=f2.graph(x1,Mx)
    F2.linear_plotpoints=5000
    F1.parameters.color="gray"
    F1.parameters.style="dashed"
    F2.parameters=F1.parameters
    F1p=f1.graph(-Mx/2,-mx)
    F2p=f2.graph(-Mx/2,-mx)
    F2p.linear_plotpoints=F2.linear_plotpoints
    F1p.parameters=F1.parameters
    F2p.parameters=F1.parameters

    P=Point(0,0.7)
    Cer=Circle(P,0.1)

    A=SurfaceBetweenFunctions(f1,f2,x0,x1)
    A.curve2.linear_plotpoints=F2.linear_plotpoints
    A.Isegment.parameters.style="solid"
    A.Isegment.parameters.color="blue"
    A.Fsegment.parameters = A.Isegment.parameters
    A.parameters.hatched()
    A.parameters.hatch.color="red"
    A.curve1.parameters.color="blue"
    A.curve1.parameters.style="solid"
    A.curve2.parameters = A.curve1.parameters

    pspict.DrawGraphs(F1p,F2p,F1,F2,A,P,Cer)
        

    pspict.axes.Dx=0.5
    pspict.DrawDefaultAxes()
    pspict.comment="Do I have enough plotpoints ?"

    fig.conclude()
    fig.write_the_file()

