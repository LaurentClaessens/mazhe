#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

var('x')
f=sin(ln(x))
print f.diff(x)
f=sin(x)/x
print f.diff(x)
f=exp(x**2)
print f.diff(x)
f=cos(x)**(sin(x))
print f.diff(x)
