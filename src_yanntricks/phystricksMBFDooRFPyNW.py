# -*- coding: utf8 -*-
from yanntricks import *

pspict,fig = SinglePicture("CQIXooBEDnfK")
pspict2,fig2 = SinglePicture("KGQXooZFNVnW")

mx=-3
Mx=3
my=-3
My=3
d1=Segment(Point(mx,My),Point(Mx,my))
d2=Segment(Point(mx,my),Point(Mx,My))
d1.parameters.color="brown"
d2.parameters=d1.parameters

x,y=var('x,y')
f1=phyFunction(sqrt(x**2-1))
f2=phyFunction(-sqrt(x**2-1))
f3=phyFunction(sqrt(1+x**2))
f4=phyFunction(-sqrt(1+x**2))

P=Point(1,0)
Q=Point(-1,0)
R=Point(0,1)
S=Point(0,-1)
P.put_mark(0.1,135,"$P$",pspict=pspict)
Q.put_mark(0.1,45,"$Q$",pspict=pspict)
R.put_mark(0.1,-45,"$R$",pspict=pspict2)
S.put_mark(0.1,45,"$S$",pspict=pspict2)

F1=f1.graph(1,Mx)
F2=f1.graph(mx,-1)
F3=f2.graph(1,Mx)
F4=f2.graph(mx,-1)

F5=f3.graph(mx,Mx)
F6=f4.graph(mx,Mx)
F5.parameters.color="red"
F6.parameters=F5.parameters

def CQIXooBEDnfK():
    pspict.DrawGraphs(F1,F2,F3,F4,d1,d2,P,Q)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

def KGQXooZFNVnW():
    pspict2.DrawGraphs(F5,F6,d1,d2,R,S)
    pspict2.DrawDefaultAxes()
    pspict2.dilatation(1)
    fig2.conclude()
    fig2.write_the_file()


