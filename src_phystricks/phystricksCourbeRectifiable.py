from phystricks import *
def CourbeRectifiable():
    pspict,fig = SinglePicture("CourbeRectifiable")
    pspict.dilatation(0.7)
    
    x=var('x')
    f1=-20*cos(x)
    f2=2*sin(2*pi*x)
    n=4        # It makes n+1 points because the first is zero.
    sigma=[float(i)/n  for i in range(n+1)  ]
    points=[]
    curve=ParametricCurve(f1,f2).graph(0,1)
    curve.parameters.force_smoothing=False

    for i in range(len(sigma)) :
        P = curve.get_point(sigma[i])
        P.put_mark(0.5,P.advised_mark_angle(pspict),"$\gamma(t_{%s})$"%str(i),pspict=pspict)
        points.append(P)

    for i in range(len(points)-1):
        A=points[i]
        B=points[i+1]
        seg=Segment(A,B)
        seg.parameters.color="red"
        pspict.DrawGraphs(seg)

    for P in points :
        pspict.DrawGraphs(P)

        pspict.comment="The blue curve is smoothly drawn"
    pspict.DrawGraphs(curve)

    fig.conclude()
    fig.write_the_file()

