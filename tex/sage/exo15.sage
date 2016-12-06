# -*- coding: utf8 -*-

def exercise_1_5():
	var('r,s,y1,y2,y3,y4')
	A=matrix([[1,2,3,4,y1],[2,-1,1,-1,y2],[3,1,r,3,y3],[-2,6,4,s,y4]])
	A[3]=A[3]+A[1]
	A[1]=A[1]-2*A[0]
	A[2]=A[2]-3*A[0]
	print A
	A[2]=A[2]-A[1]
	A[3]=A[3]+A[1]
	print A
