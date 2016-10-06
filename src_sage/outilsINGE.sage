# -*- coding: utf8 -*-
from sage.all import *

"""
This module provides _pragmatic_ tools for solving exercise for
a first year in general mathematics.
"""

# TODO : trouver une bonne traduction pour "point de selle."

def automatedVar(symbol,n):
	""" If symbol = "x" and n=4, return the string 'x1,x2,x3,x4'  """
	s = ",".join([ symbol+str(i) for i in range(1,n+1)])
	return s

class SolveLinearSystem(object):
	"""
	Solve Ax=v and print it in a nice way

	Example :

	A=matrix([ [1,-2,3,-2,0],[3,-7,-2,4,0],[4,3,5,2,0] ])
	v=vector((0,0,0,0,0))
	print SolveLinearSystem(A,v)
	"""
	def __init__(self,A,v):
		self.matrix = A
		self.vector = v
		self.nvars = A.ncols()
		s = automatedVar("x",self.nvars)
		self.xx=var(s)
	def equations(self):
		"""Return the equations corresponding to the 
                self.matrix and self.vector as a list of equations"""
		X=matrix( [self.xx[i] for i in range(0,self.nvars) ]).transpose()
		eqs=[]
		for i in range(0,self.matrix.nrows()):
			exp = (self.matrix*X)[i][0]==self.vector[i]
			eqs.append(exp)
		return eqs
	def solutions(self):
		return solve(self.equations(),self.xx)
	def latex(self):
		""""Return the LaTeX's code of the system."""
		a=[]
		a.append(r"""

				\item
					$
					\left\{
					\begin{array}{ll}
		""")
		for eq in self.equations():
			a.append("					"+str(eq).replace("x","x_").replace("*","").replace("==","=")+"\\\\ \n")
		a.append(r"""	
					\end{array}
					\right.
					$
					""")
		return "".join(a)
	def __str__(self):
		a = []
		a.append("The given matrix corresponds to the system")
		for eq in self.equations():
			a.append(str(eq))
		a.append("And the solutions are")
		a.append(str(self.solutions()))
		return "\n".join(a)

def QuadraticMap(A,v):
	"""
	Return the result of the quadratic form associated
        with A applied on the vector v, that is the number
	A_ij v^iv^j
	using the summation convention.
	"""
	n = A.nrows()
	if not A.is_symmetric():
		print "Warning : Given matrix is not symmetric"
	if not A.is_square():
		raise TypeError,"Error : The matrix A is not square"
	if not v.degree()==n :
		raise TypeError,"The size do not agree"
	return sum([ A[i,j]*v[i]*v[j] for i in range(n) for j in range(n)  ]).simplify_full()

class SymmetricMatrix(object):
	"""
	Provide informations about the matrix A assuming it is symmetric.
	"""
	def __init__(self,A):
		if not A.is_square():
			print "Error : A symmetric matrix must be square"
			raise TypeError
		self.matrix = A
		self.degree = A.nrows()
		self.matrix.set_immutable()
	def primary_principal_submatrix(self,n):
		"""
		Return the primary principal submatrix of order n, that is the matrix obtained
                by removing the n last lines and columns from self.
		"""
		taille=self.degree-n
		v=[]
		for i in range(0,taille):
			v.append(self.matrix[i][0:taille])
		return matrix(v)
	def principal_minors(self):
		"""
		Return the list of principal minors. The principal minor of order k is 
                the determinant of the primary principal matrix of order k.
		"""
		a=[]
		for i in range(self.degree):
			a.append(self.primary_principal_submatrix(i).determinant())
		return a
	def genre_list(self):
		"""
		Return the genius of the matrix as a list of booleans in the order
		positive defined, negative defined; 
                semidefinite positive, semidefinite negative, indefinite.

		"""
		defpos = True
		defneg = True
		semidefpos = True
		semidefneg = True
		indefinie=True
 		mineurs = self.principal_minors()
		for i in range(len(mineurs)):
			m = mineurs[i]
			if m == 0:
				defneg=False
				defpos=False
			if m < 0:
				defpos=False
				semidefpos=False
				if i%2==0:
					defneg=False
			if m > 0:
				semidefneg=False
				if i%2==1:
					defneg=False
		if 0 not in mineurs:
			semidefneg=False
			semidefpos=False
		if (defpos==True)or(defneg==True)or(semidefpos==True)or(semidefneg==True):indefinie=False
		return [defpos,defneg,semidefpos,semidefneg,indefinie]
	def __str__(self):
		return str(self.matrix)

class QuadraticForm(SymmetricMatrix):
	"""
	From a symmetric matrix A, provide informations concerning the associated quadratic form.
	"""
	def __init__(self,A):
		SymmetricMatrix.__init__(self,A)
		if not A.is_symmetric():
			print "Warning : matrix is not symmetric"
	def evaluate(self,v):
		"""
		Return the value of the quadratic form on the vector v.
		"""
		return QuadraticMap(self.matrix,v)
	def diagonalizing_martrix(self):
		"""
		Return the matrix B such that B^tAB is diagonal. 
		"""
		# The transposition is because, in the matrix B, the eigenvectors have 
		# to be read as column while Sage's matrix constructor takes rows.
		return matrix(self.orthonormal_basis()).transpose() 
	def new_variables(self):
		"""
		Give the change of variables needed to put the quadratic form under its normal form
		X=BY
		where X are the "old" variables
		"""
		variables = var(automatedVar("y",self.degree))
		Y = vector(variables)
		return self.diagonalizing_martrix()*Y
	def eigenmatrix_left(self):
		return self.matrix.eigenmatrix_left()
	def eigenvectors(self):
		"""
		Return a list of eigenvectors of the matrix. 

		As the matrix is symmetric, that list has to be a basis.
		"""
		D,P = self.eigenmatrix_left()
		return [P[i] for i in range(P.nrows())]
	def eigenvalues(self):
		"""
		Return a list of eigenvalues of the matrix in the same order as the list of eigenvectors given in 
			self.eigenvectors()
		"""
		D,P = self.eigenmatrix_left()
		return [ D[i,i] for i in range(D.nrows()) ]
	def orthonormal_basis(self):
		"""
		Return a basis of eigenvectors normalised to 1 as a list.
		"""
		M,mu = matrix(self.eigenvectors()).gram_schmidt()
		return [ v/v.norm() for v in M ]
	def verification(self):
		"""
		return the value of the quadratic form on the vector new_variables()
		"""
		return self.evaluate(self.new_variables())

	def __str__(self):
		a = []
		a.append("Hi guy; I'm the quadratic form associated with the matix")
		a.append(str(self.matrix))
		a.append("My eigenvalues and eigenvectors are : ")
		veps = self.eigenvectors()
		vaps = self.eigenvalues()
		for i in range(len(veps)):
			a.append("%s -> %s"%(str(vaps[i]),str(veps[i])))
		a.append("I've the following orthonormal basis of eigenvectors :")
		for v in self.orthonormal_basis():
			a.append(str(v))
		a.append("A matrix B such that B^tAB is diagonal is ")
		a.append(str(self.diagonalizing_martrix()))
		a.append("I'm quite pretty in the following variables ...")
		for i in range(self.degree):
			a.append("x%s = %s"%(str(i+1),str(self.new_variables()[i])))
		a.append("Look at me when I wear my cool variables")
		a.append(str(self.verification()))
		return "\n".join(a)

class Extrema(object):
	"""
	From a function f, provides the informations for the study of the extrema :
	partial derivative
	critical points
	Hessian matrix at the critical points
	Genius of the Hessian and conclusion as local min/max

	Dear student : remember that this class does not furnish any informations
        concerning *global* extrema. The latter have to be found
		among the critical points OR on the border of the domain.
	"""
	def __init__(self,f):
		var('x,y')
		self.fun = f
		self.gx=self.fun.diff(x).full_simplify()
		self.gy=self.fun.diff(y).full_simplify()
		self.gxx=self.gx.diff(x).simplify_full()
		self.gxy=self.gx.diff(y).full_simplify()
		self.gyy=self.gy.diff(y).full_simplify()
		self.cp = solve( [self.gx(x,y)==0,self.gy(x,y)==0],[x,y] )
	def critical_points(self):
		"""
		Return the critical points as a list of tuples (x,y)
		"""
		a = []
		for pt in self.cp :
			try :
				px = SR(pt[0].rhs())
				py = SR(pt[1].rhs())
				a.append((px,py))
			except TypeError :
				a.append("	I'm not able to solve these equations.")
		return a
	def hessienne(self,a,b):
		return matrix(SR,2,2,[self.gxx(a,b),self.gxy(a,b),self.gxy(a,b),self.gyy(a,b)])
	def __str__(self):
		a = []
		a.append ("The function :")
		a.append(str(self.fun))
		a.append ("Derivative x and y :")
		a.append(str(self.gx))
		a.append(str(self.gy))
		a.append ("Hessian matrix :")
		a.append(str(self.hessienne(x,y)))
		a.append ("Critical points :")
		for pt in self.critical_points() :
			a.append(str(pt))
		for pt in self.critical_points():
			try :
				px = pt[0]
				py = pt[1]
				a.append("At (%s,%s), the Hessian is"%(str(px),str(py)))
				try :
					Hess = SymmetricMatrix(self.hessienne(px,py))
					for l in Hess.matrix:
						a.append("	"+str(l))
					a.append("	Primary principal minors are %s"%str(Hess.principal_minors()))
					l = Hess.genre_list()
					if l[0]==True:
						a.append("	Hessian positive defined")
						a.append("	local minimum")
					if l[1]==True:
						a.append("	Hessian negative defined")
						a.append("	local maximum")
					if l[2]==True:
						a.append("	Hessian positive semidéfinite")
						a.append("	I don't conclude")
					if l[3]==True:
						a.append("	Hessian negative semidefinite")
						a.append("	I don't conclude")
					if l[4]==True:
						a.append("	Undefinite Hessian")
						a.append("	«selle» point")
				except RuntimeError,data :
					a.append("	"+str(data))
			except TypeError :
				a.append("	I'm not able to solve these equations.")
		return "\n".join(a)
