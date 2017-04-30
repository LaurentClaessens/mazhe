#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

var('x')
f=x**2-x**4
print f.diff(x)
f=cos(2*x)
print f.diff(x)
f=(x**2-2)/(x+1)
print f.diff(x)
f=(x+1)/(x**3)
print f.diff(x)
f=tan(x)
print f.diff(x)
f=x**2+1/x
print f.diff(x)
f=2**x
print f.diff(x)
f=x/sqrt(x**2+1)
print f.diff(x)
f=sin(x)
print f.diff(x)
f=1/(x**2-4)
print f.diff(x)
f=1/abs(x**2-4)
print f.diff(x)
