from yanntricks import *
def VWFLooPSrOqz():
    pspict,fig = SinglePicture("VWFLooPSrOqz")

    A=Point(1,1)
    B=Point(2,0)
    C=Point(1,-1)
    D=Point(0,0)

    poly=Polygon( A,B,C,D )
    poly.hatched()
    poly.hatch_parameters.color="green"
    poly.edges_parameters.color="blue"

    segments=[s.copy().dilatation(3.3) for s in poly.edges]
    for s in segments :
        s.parameters.color="red"

    pspict.DrawGraphs(segments,poly)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
