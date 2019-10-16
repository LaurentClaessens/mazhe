# -*- coding: utf8 -*-
from yanntricks import *
def IWuPxFc():
    pspictThree,figThree = SinglePicture("IWuPxFc")
    
    x,y=var('x,y')

    Hmoins2=ImplicitCurve( x-y**2+2==0 ,(x,-5,5),(y,-5,5))
    Hmoins1=ImplicitCurve( x-y**2+1==0 ,(x,-5,5),(y,-5,5))
    H0=ImplicitCurve( x-y**2==0 ,(x,-5,5),(y,-5,5))
    H1=ImplicitCurve( x-y**2-1==0 ,(x,-5,5),(y,-5,5))
    H2=ImplicitCurve( x-y**2-2==0 ,(x,-5,5),(y,-5,5))

    pspictThree.DrawGraphs(Hmoins2, Hmoins1, H0, H1, H2)
    pspictThree.DrawDefaultAxes()
    pspictThree.dilatation(1)
    figThree.conclude()
    figThree.write_the_file()

