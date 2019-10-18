from yanntricks import *
def examssepti():
    pspict,fig = SinglePicture("examssepti")
    pspict.dilatation(3)

    a=-1
    b=0.5
    x=var('x')
    f1=phyFunction(x**2).graph(a,b)
    f2=phyFunction(sqrt(1-x**2)).graph(a,b)

    f1.parameters.color="red"

    x0=sqrt(sqrt(5)-1)/2*sqrt(2)
    I=f1.get_point(-x0)
    J=Point(-x0,0)
    J.put_mark(0.1,text="\( -x_0\)",pspict=pspict,position="N")

    vert=Segment(I,J)
    vert.parameters.style="dotted"

    surface=SurfaceBetweenFunctions(f1,f2,mx=-x0,Mx=b)
    surface.parameters.hatched()
    surface.Fsegment.parameters.style="dotted"
    surface.parameters.color="green"

    pspict.DrawGraphs(vert,surface,f1,f2,I,J)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

