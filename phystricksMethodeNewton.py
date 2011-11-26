from phystricks import *
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
    F=Graph(f,mx,Mx)
    pspict.DrawGraph(F)

    newton = phystricks.MathConstructions.NewtonMethod(f)
    elements = newton.step_from_point(xn)
    A=Graph(elements.A)
    B=Graph(elements.B)
    P=Graph(elements.P)
    A.mark(0.3,-90,"$x_n$")
    B.mark(0.3,-90,"$x_{n+1}$")
    P.mark(0.3,45,"$y_n$")
    pspict.DrawSegment(elements.vertical_segment,"linestyle=dotted,linecolor=red")
    pspict.DrawSegment(elements.diagonal_segment,"linestyle=dashed,linecolor=green")
    pspict.DrawGraph(A)
    pspict.DrawGraph(B)
    pspict.DrawGraph(P)

    roots = f.roots()
    for i in range(len(roots)):
        P = Graph(roots[i])
        P.mark(0.3,90,"$r_%s$"%str(i))
        pspict.DrawGraph(P)
    sommet=f.get_point( (roots[0].x+roots[1].x)/2 )
    C=Graph(sommet)
    C.mark(0.3,-90,"$S$")
    pspict.DrawGraph(C)


    pspict.DrawDefaultAxes()

    pspict.dilatation(3)
    fig.conclude()
    fig.write_the_file()

