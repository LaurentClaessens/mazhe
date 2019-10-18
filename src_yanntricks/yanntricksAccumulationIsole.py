from yanntricks import *
def AccumulationIsole():
    pspict,fig = SinglePicture("AccumulationIsole")

    O=Point(0,0)
    Boule=Circle(O,1)
    Boule.parameters.color="red"
    Boule.parameters.filled()
    Boule.parameters.fill.color="lightgray"

    P=Point(1,1)
    P.put_mark(0.4,0,"$P$",pspict=pspict)
    Q=Point(-1,0)
    Q.parameters.color="red"
    Q.put_mark(0.4,180,"$Q$",pspict=pspict)

    S=Point(0.5,0.5)
    S.put_mark(0.3,-135,"$S$",pspict=pspict)

    CercleP=Circle(P,0.2)
    CercleP.parameters.color="black"
    CercleQ=Circle(Q,0.2)
    CercleQ.parameters = CercleP.parameters

    CercleS=Circle(S,0.2)
    CercleS.parameters = CercleP.parameters
    
    pspict.DrawGraphs(Boule,P,Q,S,CercleP,CercleQ,CercleS)

    fig.conclude()
    fig.write_the_file()

