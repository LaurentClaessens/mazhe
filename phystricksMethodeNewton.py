from phystricks import *
import phystricks.MathConstructions

def MethodeNewton():
    pspict,fig = SinglePicture("MethodeNewton")

    x=var('x')
    a = -1.5
    b = 0.3
    var('x')
    f = phyFunction(x**2+a*x+b)
    xn = -0.3
    mx = -0.5
    Mx = 2
    F=f.graph(mx,Mx)
    pspict.DrawGraph(F)

    newton = phystricks.MathConstructions.NewtonMethod(f)
    elements = newton.step_from_point(xn)
    A=elements.A
    B=elements.B
    P=elements.P
    A.put_mark(0.3,-90,"$x_n$")
    B.put_mark(0.3,-90,"$x_{n+1}$")
    P.put_mark(0.3,45,"$y_n$")
    elements.vertical_segment.parameters.style="dotted"
    elements.vertical_segment.parameters.color="red"
    elements.diagonal_segment.parameters.style="dashed"
    elements.diagonal_segment.parameters.color="green"
    pspict.DrawGraphs(elements.vertical_segment,elements.diagonal_segment,A,B,P)

    roots = f.roots()
    for i in range(len(roots)):
        P = roots[i]
        P.put_mark(0.3,90,"$r_%s$"%str(i))
        pspict.DrawGraph(P)
    sommet=f.get_point( (roots[0].x+roots[1].x)/2 )
    C=sommet
    C.put_mark(0.3,-90,"$S$")
    pspict.DrawGraph(C)


    pspict.DrawDefaultAxes()

    pspict.dilatation(3)
    fig.conclude()
    fig.write_the_file()

