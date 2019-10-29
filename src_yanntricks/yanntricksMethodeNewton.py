from yanntricks import *
import yanntricks.src.MathConstructions

def MethodeNewton():
    pspict,fig = SinglePicture("MethodeNewton")
    pspict.dilatation(3)

    x=var('x')
    a = -1.5
    b = 0.3
    var('x')
    f = phyFunction(x**2+a*x+b)
    xn = -0.3
    mx = -0.5
    Mx = 2
    F=f.graph(mx,Mx)
    pspict.DrawGraphs(F)

    newton = yanntricks.src.MathConstructions.NewtonMethod(f)
    elements = newton.step_from_point(xn)
    A=elements.A
    B=elements.B
    P=elements.P
    A.put_mark(0.3,-90,"$x_n$",pspict=pspict)
    B.put_mark(0.3,-90,"$x_{n+1}$",pspict=pspict)
    P.put_mark(0.3,45,"$y_n$",pspict=pspict)
    elements.vertical_segment.parameters.style="dotted"
    elements.vertical_segment.parameters.color="red"
    elements.diagonal_segment.parameters.style="dashed"
    elements.diagonal_segment.parameters.color="green"
    pspict.DrawGraphs(elements.vertical_segment,elements.diagonal_segment,A,B,P)

    roots = f.roots()
    for i in range(len(roots)):
        P = roots[i]
        P.put_mark(0.3,90,"$r_%s$"%str(i),pspict=pspict)
    pspict.DrawGraphs(P)
    sommet=f.get_point( (roots[0].x+roots[1].x)/2 )
    C=sommet
    C.put_mark(0.3,-90,"$S$",pspict=pspict)
    pspict.DrawGraphs(C)

    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()


