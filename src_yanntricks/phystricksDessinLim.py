from yanntricks import *
def DessinLim():
    pspict,fig = SinglePicture("DessinLim")

    x=var('x')
    R=2.3
    O=Point(0,0)
    C=Circle(O,R).graph(0,90)
    C.parameters.color="blue"
    T=Point(R,R)
    lineT=Segment(O,T)

    P=Intersection(C,lineT)[1]
    A=T.projection(pspict.axes.single_axeX)
    s=P.projection(pspict.axes.single_axeY)
    c=P.projection(pspict.axes.single_axeX)


    P.put_mark(0.3,0,"\( P\)",pspict=pspict)
    T.put_mark(0.1,0,"\( T\)",pspict=pspict)
    O.put_mark(0.1,135,"\( O\)",pspict=pspict)
    s.put_mark(0.1,text="\( \sin(x)\)",pspict=pspict,position="E")
    c.put_mark(0.1,text="\( \cos(x)\)",pspict=pspict,position="N")
    A.put_mark(0.1,-60,"\( A\)",pspict=pspict)

    sP=Segment(s,P)
    sP.parameters.style="dashed"
    cP=Segment(c,P)
    cP.parameters.style="dashed"
    TA=Segment(T,A)


    pspict.axes.no_graduation()

    pspict.DrawGraphs(C,lineT,sP,cP,TA,s,c,A,T,P)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)

    fig.conclude()
    fig.write_the_file()

