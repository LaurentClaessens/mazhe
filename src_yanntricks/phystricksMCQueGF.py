# -*- coding: utf8 -*-
from yanntricks import *
def MCQueGF():
    #pspictOne,figOne = SinglePicture("levelsetsOne")
    pspictOne,figOne = SinglePicture("MCQueGF")
    
    x,y=var('x,y')

    Fmoins1=ImplicitCurve(x+y+1==0,(x,-3,3),(y,-3,3))
    F0=ImplicitCurve(x+y==0,(x,-3,3),(y,-3,3))
    F1=ImplicitCurve(x+y-1==0,(x,-3,3),(y,-3,3))
    F2=ImplicitCurve(x+y-2==0,(x,-3,3),(y,-3,3))

    pspictOne.DrawGraphs(Fmoins1, F0, F1, F2)
    pspictOne.DrawDefaultAxes()
    pspictOne.dilatation(1)
    figOne.conclude()
    figOne.write_the_file()

