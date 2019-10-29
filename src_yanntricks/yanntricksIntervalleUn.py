from yanntricks import *
def IntervalleUn():
    pspict,fig = SinglePicture("IntervalleUn")
    pspict.dilatation(3)

    O=Point(0,0)
    A=Point(0.3,0)
    U=Point(1,0)
    I=Point(-0.5,0)
    F=Point(1.5,0)
    
    A.put_mark(0.3,-90,"$a$",pspict=pspict)
    O.put_mark(0.3,-90,"$0$",pspict=pspict)
    U.put_mark(0.3,-90,"$1$",pspict=pspict)
    pspict.DrawGraphs(Segment(I,F))
    pspict.DrawGraphs(A,O,U)

    measureOA=MeasureLength(Segment(O,A),-0.1)
    measureOA.put_mark(0.3,measureOA.advised_mark_angle(pspict),"$a$",pspict=pspict)
    measureAU=MeasureLength(Segment(A,U),-0.1)
    measureAU.put_mark(0.3,measureAU.advised_mark_angle(pspict),"$1-a$",pspict=pspict)

    pspict.DrawGraphs(measureOA,measureAU)

    fig.conclude()
    fig.write_the_file()

