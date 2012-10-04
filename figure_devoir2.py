#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *

def exercice1A1():
    pspict,fig = SinglePicture("exerciceunAun",script_filename="figure_devoir2")
    

    x=var('x')
    f1=2*x**2+4*x+2
    f2=x
    g1=sqrt(4-x**2)
    g2=x
    my=0.6
    medy=0
    My=-2
    mx=-1
    Mx=5
    v1=ParametricCurve(f1,f2).graph(My, my)
    v12=ParametricCurve(f1,f2).graph(My,medy)
    v2=ParametricCurve(g1,g2).graph(My, my)
    v22=ParametricCurve(g1,g2).graph(My, medy)
    l1=phyFunction(0.5).graph(mx,Mx)
    l2=phyFunction(-1.5).graph(mx,Mx)

    #A=v1.get_point(0)

    B=v1.get_point(-1.5)
    C=v2.get_point(-1.5)
    sh=Segment(B,C)
    surf=CustomSurface(v12, v22, sh)
    surf.parameters.filled()
    surf.parameters.fill.color="blue"
    pspict.DrawGraphs(v1, v2, l1, l2)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    
    fig.conclude()
    fig.write_the_file()

exercice1A1()

def exercice1A2():
    
    pspict,fig = SinglePicture("exerciceunAdeux")

    x=var('x')
    epsilon=0.005
    mx=epsilon
    Mx=0.5
    f2=phyFunction(sin(1/x))
	#pts = Intersection(f1,f2)
	#x0=pts[0].x
    x0=epsilon
    x1=1
    #F1=f1.graph(x1,Mx)
    F2=f2.graph(x0,Mx)
    F2.plotpoints=5000
    #F1.parameters.color="gray"
    #F1.parameters.style="dashed"
    #F2.parameters=F1.parameters
    #F1p=f1.graph(-Mx/2,-mx)
    F2p=f2.graph(-Mx/2,-mx)
    F2p.plotpoints=F2.plotpoints
    #F1p.parameters=F1.parameters
    #F2p.parameters=F1.parameters
    
    #P=Point(0,0.7)
    #Cer=Circle(P,0.1)
    
    #A=SurfaceBetweenFunctions(f1,f2,x0,x1)
    #A.f2.plotpoints=F2.plotpoints
    #A.vertical_left.parameters.style="solid"
    #A.vertical_left.parameters.color="blue"
    #A.vertical_right.parameters = A.vertical_left.parameters
    #A.parameters.hatched()
    #A.parameters.hatch.color="red"
    #A.f1.parameters.color="blue"
    #A.f1.parameters.style="solid"
    #A.f2.parameters = A.f1.parameters
    
    pspict.DrawGraphs(F2)
	#pspict.DrawGraphs(F1p,F2p,F1,F2,P)
    
    pspict.axes.Dx=0.5
    pspict.DrawDefaultAxes()
    pspict.dilatation_X(4)
    
    fig.conclude()
    fig.write_the_file()

    

exercice1A2()

def exercice4():

    pspictOne,figOne = SinglePicture("levelsetsOne",script_filename="figure_devoir2")
    pspictTwo,figTwo = SinglePicture("levelsetsTwo",script_filename="figure_devoir2")
    pspictThree,figThree = SinglePicture("levelsetsThree",script_filename="figure_devoir2")
    
    x,y=var('x,y')

    Fmoins1=ImplicitCurve(x+y+1==0,(x,-3,3),(y,-3,3))
    F0=ImplicitCurve(x+y==0,(x,-3,3),(y,-3,3))
    F1=ImplicitCurve(x+y-1==0,(x,-3,3),(y,-3,3))
    F2=ImplicitCurve(x+y-2==0,(x,-3,3),(y,-3,3))
    Gmoins2=ImplicitCurve( 1-x**2-y**2+2==0 ,(x,-5,5),(y,-5,5))
    Gmoins1=ImplicitCurve( 1-x**2-y**2+1==0 ,(x,-5,5),(y,-5,5))
    G0=ImplicitCurve( 1-x**2-y**2==0 ,(x,-5,5),(y,-5,5))
    G1=ImplicitCurve( 1-x**2-y**2-0.5==0 ,(x,-5,5),(y,-5,5))
    Hmoins2=ImplicitCurve( x-y**2+2==0 ,(x,-5,5),(y,-5,5))
    Hmoins1=ImplicitCurve( x-y**2+1==0 ,(x,-5,5),(y,-5,5))
    H0=ImplicitCurve( x-y**2==0 ,(x,-5,5),(y,-5,5))
    H1=ImplicitCurve( x-y**2-1==0 ,(x,-5,5),(y,-5,5))
    H2=ImplicitCurve( x-y**2-2==0 ,(x,-5,5),(y,-5,5))
    pspictOne.DrawGraphs(Fmoins1, F0, F1, F2)
    pspictOne.DrawDefaultAxes()
    pspictOne.dilatation(1)
    figOne.conclude()
    figOne.write_the_file()
    pspictTwo.DrawGraphs(Gmoins2, Gmoins1, G0, G1)
    pspictTwo.DrawDefaultAxes()
    pspictTwo.dilatation(1)
    figTwo.conclude()
    figTwo.write_the_file()
    pspictThree.DrawGraphs(Hmoins2, Hmoins1, H0, H1, H2)
    pspictThree.DrawDefaultAxes()
    pspictThree.dilatation(1)
    figThree.conclude()
    figThree.write_the_file()
    
exercice4()
