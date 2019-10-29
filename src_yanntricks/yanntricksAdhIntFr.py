from yanntricks import *
def AdhIntFr():
    pspict,fig = SinglePicture("AdhIntFr")

    x=var('x')
    mx=0.7
    Mx=4.5
    fun=phyFunction(x**2-5*x+6)
    horiz=phyFunction(2)
    #horiz=phyFunction(sqrt(3*x))        # Dans le manuel, mettre ceci.
    pts = Intersection(fun,horiz)
    x0=pts[0].x
    x1=pts[1].x
    droite=horiz.graph(mx,Mx)
    f=fun.graph(mx,Mx)
    droite.parameters.color="gray"
    f.parameters.color="gray"
    droite.parameters.style="dashed"
    f.parameters.style="dashed"

    P=f.get_point(3.5)
    Cer=Circle(P,0.3)

    A=SurfaceBetweenFunctions(fun,horiz,x0,x1)
    A.parameters.hatched()
    A.parameters.hatch.color="red"
    A.curve1.parameters.color="blue"
    A.curve1.parameters.style="solid"
    A.curve2.parameters.style="solid"
    A.curve2.parameters.color="blue"

    pspict.DrawGraphs(droite,f,A,P,Cer)

    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

