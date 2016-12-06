# -*- coding: utf8 -*-
"""
Ce script Sage résout un certain nombre
de systèmes d'équations linéaires du cours INGE1121
"""

import outilsINGE

def exercise_1_1_bcdefhi():
	# Exercice 1.1.b (INGE1121)
	A=matrix([ [1,-2,3,-2,0],[3,-7,-2,4,0],[4,3,5,2,0] ])
	v=vector((0,0,0,0,0))
	print outilsINGE.SolveLinearSystem(A,v)
	# Exercice 1.1.c (INGE1121)
	A=matrix([ [2,1,-2,3],[3,2,-1,3],[3,3,3,-3] ])
	v=vector((0,4,9))
	print outilsINGE.SolveLinearSystem(A,v)
	# Exercice 1.1.d (INGE1121)
	A=matrix([ [1,2,-3],[2,5,2],[3,-1,-4] ])
	v=vector((0,0,0))
	print outilsINGE.SolveLinearSystem(A,v)
	# Exercice 1.1.e (INGE1121)
	A=matrix([ [1,2,-1],[2,5,2],[1,4,7],[1,3,3] ])
	v=vector((0,0,0,0))
	print outilsINGE.SolveLinearSystem(A,v)
	# Exercice 1.1.f (INGE1121)
	A=matrix([ [1,1,1,1],[1,1,1,-1],[1,1,-1,1],[1,-1,1,1] ])
	v=vector((0,4,-4,2))
	print outilsINGE.SolveLinearSystem(A,v)
	# Exercice 1.1.h (INGE1121)
	A=matrix([ [1,3,3],[1,3,4],[1,4,3] ])
	v=vector((1,0,3))
	print outilsINGE.SolveLinearSystem(A,v)
	# Exercice 1.1.i (INGE1121)
	A=matrix([ [1,-3,2],[-3,3,-1],[2,-1,0] ])
	v=vector((-6,17,3))
	print outilsINGE.SolveLinearSystem(A,v)
