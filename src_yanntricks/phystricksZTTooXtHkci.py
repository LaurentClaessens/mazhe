from yanntricks import *
def ZTTooXtHkci():
    pspicts,fig = MultiplePictures("ZTTooXtHkci",2)
    pspicts[0].mother.caption=r"La région \( V\)"
    pspicts[1].mother.caption=r"La région \( U=\phi^{-1}(V)\)"

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    A=Point(1,0)
    B=Point(2,0)
    C=Point(0,-2)
    D=Point(0,-1)

    regV=Polygon(A,B,C,D)
    regV.hatched()
    regV.hatch_parameters.color="red"

    K=Point(-2,2)
    L=Point(2,2)
    M=Point(1,1)
    N=Point(-1,1)

    regU=Polygon(K,L,M,N)
    regU.hatched()
    regU.hatch_parameters.color="blue"

    pspicts[0].DrawGraphs(regV)
    pspicts[1].DrawGraphs(regU)

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
