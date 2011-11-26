# -*- coding: utf8 -*-

from phystricks import *
def SurfaceEntreCourbes():
    pspict,fig = MultiplePictures("SurfaceEntreCourbes",3)

    pspict[0].mother.caption=u"La grande surface."
    pspict[1].mother.caption=u"La surface à soustraire."
    pspict[2].mother.caption=u"La surface entre les deux fonctions."

    x=var('x')
    mx=0.5
    Mx=3.5
    f1 = phyFunction(3*(x-2)**2+3).graph(mx,Mx)
    f2 = phyFunction(-3*(x-2)**2+8).graph(mx,Mx)

    intersection=Intersection(f1,f2)
    i1=intersection[0].x
    i2=intersection[1].x

    A=Point(i1,0)
    B=Point(i2,0)

    A.put_mark(0.3,-90,"$a$")
    B.put_mark(0.3,-90,"$b$")

    grande_surface=SurfaceUnderFunction(f2,i1,i2)
    petite_surface=SurfaceUnderFunction(f1,i1,i2)
    moyenne_surface=SurfaceBetweenFunctions(f1,f2,i1,i2)

    grande_surface.parameters.color="brown"
    petite_surface.parameters.color="cyan"
    moyenne_surface.parameters.color="red"


    pspict[0].DrawGraphs(f1,f2,grande_surface)
    pspict[1].DrawGraphs(f1,f2,petite_surface)
    pspict[2].DrawGraphs(f1,f2,moyenne_surface)

    for psp in pspict :
        psp.DrawGraphs(A,B)
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()
        psp.dilatation_X(2)
        psp.dilatation_Y(0.3)

    fig.conclude()
    fig.write_the_file()
