from yanntricks.src.segment import Segment
from yanntricks.src.point import Point
from yanntricks.src.Constructors import phyFunction
from yanntricks.src.Constructors import Intersection
from yanntricks.src.main import SinglePicture
from yanntricks.src.main import MultiplePictures
from yanntricks.src.MeasureLengthGraph import MeasureLength

def LYORooNKDHqt():
    n_ssfig=4           # Au-delà de 4, la figure ne parvient pas à se mettre en carré.
    pspictQuestion,figQuestion = SinglePicture("TangenteQuestion",script_filename="RechercheTangente")
    pspictDetail,figDetail = SinglePicture("TangenteDetail",script_filename="RechercheTangente")
    pspictsSubFig,figSubFig = MultiplePictures("LesSubFigures",n_ssfig)

    pspictDetail.dilatation(1)
    pspictQuestion.dilatation(0.7)
    for psp in pspictsSubFig:
        psp.dilatation(0.7)

    pspicts = [pspictQuestion, pspictDetail]
    pspicts.extend(pspictsSubFig)

    mx=0.7
    Mx=5
    x=var('x')
    f=phyFunction(-3/x+5).graph(mx,Mx)
    P=f.get_point(1.7)
    Q=f.get_point(4)

    P.put_mark(0.3,P.advised_mark_angle(pspicts),"$P$",pspicts=pspicts)
    Q.put_mark(0.3,Q.advised_mark_angle(pspicts),"$Q$",pspicts=pspicts)

    Px=Point(P.x,0)
    Py=Point(0,P.y)
    Qx=Point(Q.x,0)
    Qy=Point(0,Q.y)

    Py.put_mark(0.1,text="$f(a)$",pspicts=pspicts,position="E")
    Qy.put_mark(0.1,text="$f(x)$",pspicts=pspicts,position="E")
    Px.put_mark(0.2,text="$a$",pspicts=pspicts,position="N")
    Qx.put_mark(0.2,text="$x$",pspicts=pspicts,position="N")

    v1=Segment(Q,Qx)
    v2=Segment(P,Px)
    h1=Segment(Q,Qy)
    h2=Segment(P,Py)
    I=Intersection(v1,h2)[0]
    h3=Segment(P,I)
    v1.parameters.color="green"
    v1.parameters.style="dashed"
    v2.parameters=v1.parameters
    h1.parameters=v1.parameters
    h2.parameters=v1.parameters
    h3.parameters=v1.parameters

    corde=Segment(P,Q).dilatation(1.7)
    corde.parameters.color="cyan"

    Dx=MeasureLength(h3,0.2)
    Dx.put_mark(0.2,text="$x-a$",pspicts=pspicts,position="N")
    Dy=MeasureLength(Segment(Q,I),-0.2)
    Dy.put_mark(0.2,text="$f(x)-f(a)$",pspicts=pspicts,position="W")

    pspictDetail.DrawGraphs(corde,v1,v2,h1,h2,h3,f,P,Px,Py,Q,Qx,Qy,Dx,Dy)

    for psp in pspictsSubFig :
        psp.mother.caption="\\ldots de mieux en mieux \\ldots"

    pspictsSubFig[0].mother.caption="Pas très bon \\ldots"
    pspictsSubFig[-1].mother.caption="\\ldots presque parfait"

    fixed_size=4
    tangente=f.get_tangent_segment(P.x).normalize(fixed_size)
    tangente.parameters.color="red"

    for i,psp in enumerate(pspictsSubFig):
        Qi = f.get_point( Q.x-i*(Q.x-P.x)/(n_ssfig) )
        Qi.put_mark(0.3,Qi.advised_mark_angle(pspicts)+180,"$Q_{%s}$"%str(i),pspicts=pspicts,position="corner")


        corde=Segment(P,Qi).normalize(fixed_size)
        corde.parameters.color="cyan"

        psp.DrawGraphs(corde,tangente,f,Qi,P)

    for psp in pspictsSubFig :
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    figSubFig.conclude()
    figSubFig.write_the_file()

    pspictDetail.axes.no_graduation()
    pspictDetail.DrawDefaultAxes()
    figDetail.conclude()
    figDetail.write_the_file()

    pspictQuestion.DrawGraphs(f,P)
    pspictQuestion.axes.no_graduation()
    pspictQuestion.DrawDefaultAxes()
    figQuestion.conclude()
    figQuestion.write_the_file()

