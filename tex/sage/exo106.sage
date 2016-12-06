# -*- coding: utf8 -*-

import outilsINGE

def exercise_10_6():
	var('x,y,V')
	assume(V>0)
	f(x,y)=x*y+V/y+V/x
	print outilsINGE.Extrema(f)
