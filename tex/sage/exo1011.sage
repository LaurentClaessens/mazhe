# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_11():
	var('x,y')
	f(x,y)=x**3-3*x*y**2
	print outilsINGE.Extrema(f)
