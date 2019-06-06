# -*- coding: utf8 -*-

from phystricks import *
def SurfaceEntreCourbes():
    pspicts,fig = MultiplePictures("SurfaceEntreCourbes",3)
    for psp in pspicts :
        psp.dilatation_X(2)
        psp.dilatation_Y(0.3)


    pspicts[0].mother.caption=u"La grande surface."
    pspicts[1].mother.caption=u"La surface à soustraire."
    pspicts[2].mother.caption=u"La surface entre les deux fonctions."

    x=var('x')
    mx=0.1
    Mx=2.3
    f1 = phyFunction(3*(x-1.25)**2+3).graph(mx,Mx)
    f2 = phyFunction(-3*(x-1.25)**2+8).graph(mx,Mx)

    intersection=Intersection(f1,f2)
    i1=intersection[0].x
    i2=intersection[1].x

    A=Point(i1,0)
    B=Point(i2,0)

    A.put_mark(0.3,-90,"$a$",pspicts=pspicts)
    B.put_mark(0.3,-90,"$b$",pspicts=pspicts)

    grande_surface=SurfaceUnderFunction(f2,i1,i2)
    petite_surface=SurfaceUnderFunction(f1,i1,i2)
    moyenne_surface=SurfaceBetweenFunctions(f1,f2,i1,i2)

    grande_surface.parameters.filled()
    grande_surface.parameters.fill.color="brown"
    petite_surface.parameters.filled()
    petite_surface.parameters.fill.color="cyan"
    moyenne_surface.parameters.filled()
    moyenne_surface.parameters.fill.color="red"


    pspicts[0].DrawGraphs(grande_surface,f1,f2)
    pspicts[1].DrawGraphs(f1,f2,petite_surface)
    pspicts[2].DrawGraphs(moyenne_surface,f1,f2)

    for psp in pspicts :
        psp.DrawGraphs(A,B)
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

