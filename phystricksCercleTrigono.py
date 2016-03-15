from phystricks import *
def CercleTrigono():
    pspict,fig = SinglePicture("CercleTrigono")
    
    O=Point(0,0)
    Cercle=Circle(O,2)
    alpha=30
    P=Cercle.get_point(alpha)
    P.put_mark(0.3,P.advised_mark_angle(pspict),"$P$",automatic_place=(pspict,""))
    P.parameters.symbol=""
    vecteur=Vector(P)
    vecteur.parameters.color="blue"
    C=P.projection(pspict.axes.single_axeX)
    S=P.projection(pspict.axes.single_axeY)
    pc=Segment(P,C)
    ps=Segment(P,S)
    pc.parameters.color="brown"
    pc.parameters.style="dotted"
    ps.parameters=pc.parameters
    measureCos=MeasureLength(Segment(O,C),0.2)
    measureSin=MeasureLength(Segment(O,S),-0.2)
    measureCos.put_mark(0.1,-90,r"$\cos(\theta)$",automatic_place=(pspict,"N"))
    measureSin.put_mark(-0.1,0,r"$\sin(\theta)$",automatic_place=(pspict,"E"))

    angle=Angle(C,O,P,0.4)
    angle.put_mark(0.3,None,r"$\theta$",automatic_place=(pspict,""))

    pspict.DrawGraphs(Cercle,pc,ps,S,C,measureSin,measureCos,vecteur,angle,P)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
