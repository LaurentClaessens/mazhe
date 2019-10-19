from yanntricks import *
def Cardioideexo():
    pspict,fig = SinglePicture("Cardioideexo")

    x=var('x')
    f=phyFunction(1+cos(x))
    curve=PolarCurve(f).graph(0,2*pi)

    P=Point(1,1)
    O=Point(0,0)
    Q=curve.get_point(pi/4)
    rect=Rectangle(O,P)
    rect.edges_parameters.color="lightgray"

    C1=Circle(O,1)
    C2=Circle(O,2)
    C1.parameters.color="lightgray"
    C2.parameters=C1.parameters

    seg=Segment(O,Q)
    seg.parameters.style="dashed"
    seg.parameters.color=rect.edges_parameters.color

    pspict.DrawGraphs(C1,C2,curve,rect,seg,P,Q)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

