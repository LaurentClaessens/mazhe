from yanntricks import *

def ArcLongueurFinesse():
    pspict,fig = SinglePicture("ArcLongueurFinesse")
    pspict.dilatation(0.7)

    def TraceDivision(n,curve,pspict,color):
        sigma=[(Mx-mx)*float(i)/n  for i in range(n+1)  ]
        points = [ curve.get_point(t) for t in sigma ]
        for i in range(len(points)-1):
            A=points[i]
            B=points[i+1]
            seg=Segment(A,B)
            seg.parameters.color=color
            pspict.DrawGraphs(seg)

    x=var('x')
    #f1=-20*cos(x)
    #f2=2*sin(2*pi*x)
    #mx=0
    #Mx=1
    f1=x
    f2=cos(x)
    mx=0
    Mx=6*pi
    curve=ParametricCurve(f1,f2).graph(mx,Mx)
    curve.parameters.style="dashed"
    pspict.DrawGraphs(curve)
    TraceDivision(5,curve,pspict,"red")
    TraceDivision(11,curve,pspict,"green")

    fig.conclude()
    fig.write_the_file()

