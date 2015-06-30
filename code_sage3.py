#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

def f(z):
    var('alpha,beta')
    x=z.real_part()
    y=z.imag_part()
    return alpha*x+beta*y+I*( -beta*x+alpha*y  )


var('a,b,x,y')

A=a+b*I
Z=x+y*I

z1=f( A*Z  )
z2=A*f( Z )

rep=z1-z2
print(rep.full_simplify())
