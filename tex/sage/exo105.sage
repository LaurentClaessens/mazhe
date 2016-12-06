# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_5():
	var('x,y,A')
	assume(A>0)
	f(x,y)=x*y*(A-x-y)
	print outilsINGE.Extrema(f)
