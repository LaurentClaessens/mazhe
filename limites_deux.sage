import sys

class PrintToShow(object):
	def __init__(self):
		self.liste=[]
	def write(self,a):
		self.liste.append(a)
		print a
	def close(self):
		show(self.liste)

def chemin(f,g1,g2):
	var('t')
	return f(g1,g2).simplify_full()

def test_chemin(X,f,g1,g2):
	var('k,t')
	X.write("Sur le chemin (%s,%s) :"%(repr(g1),repr(g2)))
	gamma(k,t)=chemin(f,g1,g2)
	X.write(gamma)
	X.write("La limite pour t-> 0 est")
	l=limit(gamma(k,t),t=0).simplify_full()
	X.write(l)

def StudyLimit(f):
	X = PrintToShow()
	var('r,theta,t,k')
	X.write("La fonction")
	X.write(f)
	fPolaire(r,theta)=f(r*cos(theta),r*sin(theta)).simplify_full()
	X.write("La fonction en polaires")
	X.write(fPolaire)
	# --- (t,kt) ---
	test_chemin(X,f,t,k*t)
	# --- (0,t) ---
	test_chemin(X,f,0,t)
	# --- (t,t^2)
	test_chemin(X,f,t,t**2)
	X.write("EN POLAIRES, MAINTENANT")
	test_chemin(X,fPolaire,t,k*t)

	X.close()

def StudyFunction(f):
	StudyLimit(f)
	dxf(x,y)=f.diff(x).simplify_full()
	StudyLimit(dxf)
