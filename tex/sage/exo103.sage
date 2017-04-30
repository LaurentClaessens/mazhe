# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_3_A():
	var('x,y')
	f(x,y)=x**2+4*x+y**2-2*y
	print outilsINGE.Extrema(f)

def exercise_10_3_H():
	var('x,y')
	f(x,y)=exp(x**2+x*y)
	print outilsINGE.Extrema(f)

def exercise_10_3_Q():
	var('x,y')
	f(x,y)=exp(x)*sin(y)
	print outilsINGE.Extrema(f)
