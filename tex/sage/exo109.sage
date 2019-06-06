# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_9():
	var('x,y')
	f(x,y)=x**2+y**2+(x*y-2)**2
	print outilsINGE.Extrema(f)
