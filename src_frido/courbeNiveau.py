#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

var('x,y')
f=x**2+y**2
G=Graphics()
a=3
for i in range(0,5):
	G=G+implicit_plot(f==i,(x,-a,a),(y,-a,a))
show(G)
