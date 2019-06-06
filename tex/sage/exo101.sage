# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_1_A():
	var('x,y')
	f(x,y)=2-sqrt(x**2+y**2)
	print outilsINGE.Extrema(f)
def exercise_10_1_B():
	var('x,y')
	f(x,y)=x**3+3*x*y**2-15*x-12*y
	print outilsINGE.Extrema(f)
def exercise_10_1_C():
	var('x,y')
	f(x,y)=x**3/3+4*y**3/3-x**2-3*x-4*y-3
	print outilsINGE.Extrema(f)
