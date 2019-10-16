# -*- coding: utf8 -*-
from yanntricks import *
def PHTVjfk():
    pspictTwo,figTwo = SinglePicture("PHTVjfk")
    
    x,y=var('x,y')

    Gmoins2=ImplicitCurve( 1-x**2-y**2+2==0 ,(x,-5,5),(y,-5,5))
    Gmoins1=ImplicitCurve( 1-x**2-y**2+1==0 ,(x,-5,5),(y,-5,5))
    G0=ImplicitCurve( 1-x**2-y**2==0 ,(x,-5,5),(y,-5,5))
    G1=ImplicitCurve( 1-x**2-y**2-0.5==0 ,(x,-5,5),(y,-5,5))

    pspictTwo.DrawGraphs(Gmoins2, Gmoins1, G0, G1)
    pspictTwo.DrawDefaultAxes()
    pspictTwo.dilatation(1)
    figTwo.conclude()
    figTwo.write_the_file()

