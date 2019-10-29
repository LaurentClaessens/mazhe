# -*- coding: utf8 -*-
from yanntricks import *
def IOCTooePeHGCXH():
    pspict,fig = SinglePicture("IOCTooePeHGCXH")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(2)

    R1=1
    R2=1.5
    C1=Point(0,R1)
    C2=Point(R1+R2-0.5,R2)
    Cir1=Circle(C1,R1)
    Cir2=Circle(C2,R2)

    gta=Cir1.get_point(-90)
    gtb=Cir2.get_point(-90)
    gtC=Segment(gta,gtb).dilatation(3)

    gtC.F.parameters.symbol=""
    gtC.F.put_mark(0.2,angle=None,added_angle=0,text="\( \\tilde\phi(\mC)\)",pspict=pspict)

    gta.put_mark(0.3,angle=None,added_angle=0,text="\( \\tilde \phi(a)\)",pspict=pspict)
    gtb.put_mark(0.3,angle=None,added_angle=0,text="\( \\tilde \phi(b)\)",pspict=pspict)


    ii=Intersection(Cir1,Cir2)
    gtm=ii[0]
    O=ii[1]

    O.put_mark(0.2,angle=0,added_angle=0,text="\( 0\)",pspict=pspict)
    gtm.put_mark(0.2,angle=0,added_angle=0,text="\( \\tilde\phi(m)\)",pspict=pspict)

    L=Segment(gtm,O).dilatation(2)

    gtc=Intersection(L,gtC)[0]
    gtc.put_mark(0.2,angle=220,added_angle=0,text="\( \\tilde\phi(c)\)",pspict=pspict)



    mm1=Cir1.get_point(150)
    mm2=Cir2.get_point(45)
    mm1.parameters.symbol=""
    mm2.parameters.symbol=""
    mm1.put_mark(0.2,angle=None,added_angle=0,text="\( \\tilde \phi(A)\)",pspict=pspict)
    mm2.put_mark(0.2,angle=None,added_angle=0,text="\( \\tilde \phi(B)\)",pspict=pspict)

    pspict.DrawGraphs(Cir1,Cir2,gta,gtc,gtb,gtC,gtm,mm1,mm2,O,L,gtC.F)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

