# -*- coding: utf8 -*-

import outilsINGE

def exercise_1_3():
	A=matrix([[2,1,-2],[3,2,2],[5,4,3]])
	v=vector((10,1,4))
	print outilsINGE.SolveLinearSystem(A,v)
	print "Matrice inverse :"
	print A.inverse()
