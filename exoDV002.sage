# -*- coding: utf8 -*-

def LesCalculs(f):
	print "Pour la fonction %s"%str(f)
	print "d_x",f.diff(x).simplify_full()
	print "d_y",f.diff(y).simplify_full()
	print "d^2_x",f.diff(x).diff(x).simplify_full()
	print "d_xd_y",f.diff(x).diff(y).simplify_full()
	print "d_yd_x",f.diff(y).diff(x).simplify_full()
	print "d^2_y",f.diff(y).diff(y).simplify_full()
	print ""

def exercise_DV002():
	var('x,y')
	fa(x,y)=2*x**3+3*x**2*y-2*y**2
	fb(x,y)=ln(x*y**2)
	fc(x,y)=tan(x/y)
	fd(x,y)=x*y**2/(x+y)
	LesCalculs(fa)
	LesCalculs(fb)
	LesCalculs(fc)
	LesCalculs(fd)
