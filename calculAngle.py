#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from sage.all import *

def PointToPolaire(x,y):
	x=SR(x)
	y=SR(y)
	r = sqrt(x**2+y**2)
	if x == 0:
		if y > 0:
			alpha = pi/2
		if y < 0:
			alpha = 3*pi/2
		if y == 0 : 	
			raise ValueError,"Pas d'angle pour le point (0,0) !!"
	else :
		alpha = atan(y/x)
	if (x < 0) and (y == 0) :
		alpha = pi
	if (x < 0) and (y > 0) :
		alpha = alpha + pi
	if (x < 0) and (y < 0 ) :
		alpha = alpha + pi
	alpha=alpha.simplify_trig()
	return (r,alpha)

print PointToPolaire(1,1)
print PointToPolaire(-2,1)
print PointToPolaire(6*sqrt(3)/2,3)
