from phystricks import *
class Gamma(object):
	def __init__(self,f1,f2):
		self.f1=f1
		self.f2=f2
		self.curve=ParametricCurve(f1,f2)
	def valeurs(self,llam):
		print "Valeur : ",self.curve(llam,False)
		print "Tangente : ",self.curve.derivative()(llam)
		print "Normale : ",self.curve.get_normal_vector(llam)
		print "Derivée seconde :",self.curve.derivative(2)(llam)
	def derives(self):
		print "Fonction :",self.curve
		print "Derivée : ",self.curve.derivative()
		print "Derivée seconde : ",self.curve.derivative(2)
	def plot(self,l1,l2):
		return parametric_plot( (self.f1(x),self.f2(x)),(x,l1,l2) )

var('x')
f1=x+1/x
f2=x+1/(2*x**2)
gamma=Gamma(f1,f2)
