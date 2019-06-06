# -*- coding: utf8 -*-

import outilsINGE

def exercise_6_5():
	A=matrix(QQ,4,4,[2,1,-1,1,1,0,1,1,-1,1,2,1,1,1,1,0])
	x=outilsINGE.QuadraticForm(A)
	print x
