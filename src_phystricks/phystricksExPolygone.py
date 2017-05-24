from phystricks import *
def ExPolygone():
    pspict,fig = SinglePicture("ExPolygone")

    A=Point(1,1)
    B=Point(2,0)
    C=Point(1,-1)
    D=Point(0,0)

    poly=Polygon( A,B,C,D )
    poly.parameters.hatched()
    poly.parameters.hatch.color="green"
    poly.edge_model.parameters.color="blue"

    segments=[s.copy().dilatation(3.3) for s in poly.edges]
    for s in segments :
        s.parameters.color="red"

    pspict.DrawGraphs(segments,poly)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

