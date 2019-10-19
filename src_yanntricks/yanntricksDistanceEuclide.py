from yanntricks import *
def DistanceEuclide():
    pspict,fig=SinglePicture("DistanceEuclide")

    A=Point(1,4)
    B=Point(3,1)
    C=Point(B.x,A.y)
    A.put_mark(0.3,90,"$(A_x,A_y)$",pspict=pspict)
    B.put_mark(0.3,0,"$(B_x,B_y)$",pspict=pspict)
    C.put_mark(0.3,45,"$C$",pspict=pspict)
    pspict.DrawGraphs(A,B,C)

    Lab=Segment(A,B)
    Lac=Segment(A,C)
    Lbc=Segment(B,C)
    pspict.DrawGraphs(Lab,Lac,Lbc)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

