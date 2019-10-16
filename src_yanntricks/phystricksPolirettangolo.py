from yanntricks import *
def Polirettangolo():
    pspict,fig = SinglePicture("Polirettangolo")
    pspict.dilatation(0.5)

    P=Point(0,2)
    P1=Point(3,4)
    P2=Point(1,4)
    P3=Point(4,5)
    P4=Point(4,0)
    P5=Point(6,2)
    P6=Point(4,3)
    P7=Point(7,7)
    
    R=Rectangle(P,P1)
    R1=Rectangle(P2,P3)
    R2=Rectangle(P4,P5)
    R3=Rectangle(P6,P7)
    R.hatched()
    R.hatch_parameters.color="red"

    for rect in [R,R1,R2,R3]:
        rect.edges_parameters.style="dotted"

    for rect in [R1,R2,R3]:
        rect.hatched()
        rect.edges_parameters=R.edges_parameters.copy()
        rect.hatch_parameters=R.hatch_parameters.copy()

    pspict.DrawGraphs(R,R1,R2,R3)
    
    pspict.single_axeX.Dx=2
    pspict.single_axeY.Dx=2
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
