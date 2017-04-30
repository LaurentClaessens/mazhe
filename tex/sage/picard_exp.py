#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

x=var('x')

def Phi(f):
    prim=f.integrate()
    return 1+prim(x)-prim(0)

f=sin(x)

for i in range(1,30):
    print(i,f)
    f=Phi(f)

g=f(x)-exp(x)
plot(g,(x,-10,10)).show()
