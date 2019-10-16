from yanntricks import *
def ExampleChangementVariables():
    fig = GenericFigure("ExampleChangementVariables")

    ssfig1=fig.new_subfigure(r'''La r\'egion $V$''', 'vecchiaregione')
    ssfig2=fig.new_subfigure(r'''La r\'egion $U=\phi^{-1}(V)$''', 'nuovaregione')
    pspict=ssfig1.new_pspicture('vreg')
    pspict2=ssfig2.new_pspicture('nreg')
    P=Point(0,-1)
    P1=Point(1,0)
    P2=Point(2,0)
    P3=Point(0,-2)
    l1=Segment(P1,P2)
    l2=Segment(P2,P3)
    l3=Segment(P3,P)
    l4=Segment(P,P1)
    reg=CustomSurface(l1,l2,l3,l4)
    reg.parameters.hatched()
    reg.parameters.hatch.color="red"
    
    pspict.DrawGraphs(reg,l1,l2,l3,l4 )
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    
    R=Point(-1,1)
    R1=Point(1,1)
    R2=Point(2,2)
    R3=Point(-2,2)
    s1=Segment(R1,R2)
    s2=Segment(R2,R3)
    s3=Segment(R3,R)
    s4=Segment(R,R1)
    reg1=CustomSurface(s1,s2,s3,s4)
    reg1.parameters.hatched()
    reg1.parameters.hatch.color="blue"

    pspict2.DrawGraphs(reg1, s1,s2,s3,s4)
    pspict2.DrawDefaultAxes()
    pspict2.dilatation(1)

    fig.conclude()
    fig.write_the_file()

