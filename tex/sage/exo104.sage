# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_4():
	var('x,y')
	f(x,y)=x*y**2*exp(-(x**2+y**2)/4)
	print outilsINGE.Extrema(f)
