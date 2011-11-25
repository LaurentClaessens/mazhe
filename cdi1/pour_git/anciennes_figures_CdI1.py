#! /usr/bin/sage -python
# -*- coding: utf8 -*-

######################################
#
# Ce fichier contient les figures produites anciennement pour CdI1.
# Elles utilisent une vieille version de phystricks.
# TODO : les mettre à jour.
####################################

from __future__ import division
import commands, os, copy, math						# Le module copy est pour faire des copies d'objets
from sage.all import *
from sympy import *
from phystricks import *
# Ce script demande aussi la présence de Maxima sur le système,
# pour calculer des extrema de fonctions, entre autres.


REP = commands.getoutput("pwd")

def couleur(k):
	if k == 0 : return "black"
	if k == 1 : return "red"
	if k == 2 : return "blue"
	if k == 3 : return "green"
	if k == 4 : return "cyan"
	if k == 5 : return "brown"
	if k == 6 : return "yellow"
	if k == 7 : return "black"
	if k == 8 : return "red"
	if k == 9 : return "blue"
	if k == 10 : return "green"
	if k == 11 : return "cyan"
	if k == 12 : return "brown"
	if k == 13 : return "yellow"
	#if k == 1 : return ""

def figure_111():
	mx = -1.2
	Mx = 1.2

	pspict = pspicture()
	nom = "exouuu"
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	
	axes = Axes( Point(0,0), BoundingBox(Point(1,0), Point(1,1.2)) )

	for i in range(1,5):
		f = Fonction("(1-x^4)^"+str(i-1))
		axes.AjusteFonction(f,mx,Mx)
		pspict.TraceFonction(f,"linecolor="+couleur(i),mx,Mx)

	#axes.AjouteGrille()
	pspict.TraceAxes(axes)
	#pspict.TraceBB()

	fig.AjoutePspicture(pspict)
	fig.DilateX(3)
	fig.DilateY(3)
	#fig.Dilate(0.9)
	fig.Conclure()
	fig.EcrireFichier()

def figure_112():
	pspict = pspicture()
	nom = "exouud"
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	
	axes = Axes( Point(0,0), BoundingBox(Point(1,0), Point(1.2,1.2)) )

	for i in range(1,5):
		f = Fonction("1-"+str(i)+"*x")
		axes.AjusteFonction(f,0,1/i)
		pspict.TraceFonction(f,"linecolor="+couleur(i),0,1/i)

	#axes.AjouteGrille()
	pspict.TraceAxes(axes)
	#pspict.TraceBB()

	fig.AjoutePspicture(pspict)
	fig.DilateX(4)
	fig.DilateY(2)
	fig.Conclure()
	fig.EcrireFichier()

def figure_113():
	pspict = pspicture()
	nom = "exouut"
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	m = -1
	z = 0
	n = 1
	p = 2
	f = 4
	h = 1

	M = Point(m,0)
	Z = Point(z,0)
	N = Point(n,0)
	P = Point(p,0)
	F = Point(f,0)

	A = Point(n,h)
	B = Point(p,h)

	pspict.TraceSegment( Segment(M,N), "")
	pspict.TraceSegment( Segment(N,P), "linestyle=dotted")
	pspict.TraceSegment( Segment(N,A), "linestyle=dashed")
	pspict.TraceSegment( Segment(P,B), "linestyle=dashed")
	pspict.TraceSegment( Segment(A,B), "")
	pspict.TraceSegment( Segment(P,F), "")

	pspict.MarquePoint( Z, 0.3,-90, "none", "$0$" )
	pspict.MarquePoint( N, 0.3,-90, "none", "$n$" )
	pspict.MarquePoint( P, 0.3,-90, "none", "$n+1$" )

	fig.AjoutePspicture(pspict)
	fig.DilateX(2.5)
	fig.DilateY(1)
	fig.Conclure()
	fig.EcrireFichier()


def figure_114():
	pspict = pspicture()
	nom = "exouuiv"
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	pspictbis = pspicture()
	nom = "exouuivbis"
	figbis = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	n = 3

	x1 = -2
	x2 = -1
	x3 = -1/n
	x4 = 1/n
	x5 = 1
	x6 = 2
	h = 1

	A = Point(x1,0)
	B = Point(x2,h)
	Bp = Point(x2,0)
	C = Point(x3,h)
	Cp = Point(x3,0)
	D = Point(x4,-h)
	Dpp = Point(x4,h)
	E = Point(x5,-h)
	Dp = Point(x4,0)
	Ep = Point(x5,0)
	F = Point(x6,0)
	P = Point(0,-h)
	H = Point(0,h)
	Hp = Point(0,-h)

	axes = Axes( Point(0,0), BoundingBox(Point(-2.1,-1.1), Point(2.1,1.1)) )

	pspict.TraceAxes(axes)
	pspict.TraceSegment( Segment(A,B), "")
	pspict.TraceSegment( Segment(B,C), "")
	pspict.TraceSegment( Segment(C,D), "")
	pspict.TraceSegment( Segment(D,E), "")
	pspict.TraceSegment( Segment(E,F), "")
	pspict.TraceSegment( Segment(B,Bp), "linestyle=dotted")
	pspict.TraceSegment( Segment(C,Cp), "linestyle=dotted")
	pspict.TraceSegment( Segment(D,Dp), "linestyle=dotted")
	pspict.TraceSegment( Segment(E,Ep), "linestyle=dotted")
	pspict.TraceSegment( Segment(P,D), "linestyle=dotted")
	pspict.MarquePoint( Cp, 0.3,-90, "none", "$-1/n$" )
	pspict.MarquePoint( Dp, 0.3,90, "none", "$1/n$" )

	pspictbis.TraceAxes(axes)
	pspictbis.TraceSegment( Segment(A,B), "")
	pspictbis.TraceSegment( Segment(B,H), "")
	pspictbis.TraceSegment( Segment(Hp,E), "")
	pspictbis.TraceSegment( Segment(E,F), "")

	pspict.TraceSegment( Segment(B,Bp), "linestyle=dotted")
	pspict.TraceSegment( Segment(E,Ep), "linestyle=dotted")

	fig.AjoutePspicture(pspict)
	fig.DilateX(2.3)
	fig.DilateY(1)
	fig.Conclure()
	fig.EcrireFichier()

	figbis.AjoutePspicture(pspictbis)
	figbis.DilateX(2.3)
	figbis.DilateY(1)
	figbis.Conclure()
	figbis.EcrireFichier()

	# La figure avec la différence f_n - f.
	
	n = 1.25		# Note que le n change par rapport à la première figure.	

	gG = Fonction( "-"+str(n)+"*x-1" )
	gD = Fonction( "1-"+str(n)+"*x" )

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1.1), Point(1,1.1)) )
	axes.AjouteLabelX(0.3,-90,"$x$")
	axes.AjouteLabelY(0.7,0,"$f_n-f$")		# La distance ici est au vogelpic 
	axes.AjouteOption("labels=none,ticks=none")
	axes.AjusteFonction(gG,-1.3,0)
	axes.AjusteFonction(gD,0,1.3)
	pspictU = pspicture()
	pspictU.TraceAxes(axes)
	pspictU.TraceFonction(gG,"",-1/n,0)
	pspictU.TraceFonction(gD,"",0,1/n)
	#pspictU.MarquePoint( Point(0,1) , 0.3,45, "none", "$f_n-f$" )
	pspictU.MarquePoint( Point(-1/n,0) , 0.3,135, "none", "$-1/n$" )
	pspictU.MarquePoint( Point(1/n,0) , 0.3,-45, "none", "$1/n$" )

	ssfigU = subfigure("La différence entre une des fonctions et la limite.","labelpetit")
	ssfigU.AjoutePspicture(pspictU)


	hG = Fonction( "("+gG.string+")^2" )
	hD = Fonction( "("+gD.string+")^2" )

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1.1), Point(1,1.1)) )
	axes.AjouteLabelX(0.3,-90,"$x$")
	axes.AjouteLabelY(0.9,0,"$(f_n-f)^2$")		# La distance ici est au vogelpic 
	axes.AjouteOption("labels=none,ticks=none")
	axes.AjusteFonction(hG,-1.3,0)
	axes.AjusteFonction(hD,0,1.3)
	pspictD = pspicture()
	pspictD.TraceAxes(axes)
	hG.AjouteSurface(-1/n,0)
	hG.ListeSurface[-1].options.DicoOptions["fillstyle"] = "vlines"
	hD.AjouteSurface(0,1/n)
	hD.ListeSurface[-1].options.DicoOptions["fillstyle"] = "vlines"
	pspictD.TraceFonction(hG,"",-1/n,0)
	pspictD.TraceFonction(hD,"",0,1/n)
	pspictD.MarquePoint( Point(-1/n,0) , 0.3,-90, "none", "$-1/n$" )
	pspictD.MarquePoint( Point(1/n,0) , 0.3,-90, "none", "$1/n$" )

	ssfigD = subfigure("La carré de la différence.","labelpetit")
	ssfigD.AjoutePspicture(pspictD)


	nom = "Sixdiff"
	figM = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")
	figM.AjouteSSfigure(ssfigU)
	figM.AjouteSSfigure(ssfigD)
	figM.DilateX(1.5)
	figM.DilateY(1)
	figM.Conclure()
	figM.EcrireFichier()


def figure_119():

	def _angle(n):
		if n == 0 : return 45
		if n == 2 : return 180
		if n == 4 : return 180
		if n == 6 : return 135
		if n == 8 : return 45
	
	pspict = pspicture()
	nom = "exouuix"
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(1,1)) )

	segsV = []
	segsH = []
	propsV = []
	propsH = []
	for i in range(1,5):
		n = 2*i
		f = Fonction("1/(x^"+str(n)+")-1")
		mx = 1-(1/(n+1))
		Mx = 1
		axes.AjusteFonction(f,mx,Mx)
		pspict.TraceFonction(f,"linecolor="+couleur(i),mx,Mx)
		P = f.PointDessus(mx)
		Q = Point(P.x,0) 
		pspict.MarquePoint( P,0.3,_angle(n),"none","$f_{"+str(n)+"}$" )
		segsV.append([Segment(P,Q),"linestyle=dashed,linecolor="+couleur(i)])
		segsH.append([Segment( Point(0,0),Q),"linecolor="+couleur(i) ] )
		
		#pspict.TraceSegment(Segment( P,Q ),  "linestyle=dashed,linecolor="+couleur(i) )
		#pspict.TraceSegment(Segment( Point(0,0),Q ),  "linecolor="+couleur(i) )

	pspict.TraceAxes(axes)
	for s in segsV :
		pspict.TraceSegment(s[0],s[1])
	for s in reversed(segsH) :
		pspict.TraceSegment(s[0],s[1])

	fig.AjoutePspicture(pspict)
	fig.DilateX(5)
	fig.DilateY(2)
	fig.Conclure()
	fig.EcrireFichier()


def dessinlim():
	pspict=pspicture()
	nom = "DessinLim"
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	f = Fonction(" (1-x^2)^(1/2) ")
	O = Point(0,0)
	X = Point(1,0)
	Y = Point(0,1)
	P = f.PointDessus(0.7)
	OP = Segment(O,P)
	T = OP.Fonction.PointDessus(1)
	C = P.Projection(Segment(O,X))
	S = P.Projection(Segment(O,Y))
	A = T.Projection(Segment(O,X))

	pspict.MarquePoint(O,0.3,-135,"none","$O$")	
	pspict.MarquePoint(P,0.3,0,"none","$P$")	
	pspict.MarquePoint(T,0.3,0,"none","$T$")	
	pspict.MarquePoint(C,0.3,-90,"none","$\cos(x)$")	
	pspict.MarquePoint(S,0.6,180,"none","$\sin(x)$")	
	pspict.MarquePoint(A,0.3,-90,"none","A")	

	pspict.TraceSegment( Segment(S,P), "linestyle=dashed")
	pspict.TraceSegment( Segment(C,P), "linestyle=dashed")
	pspict.TraceSegment( Segment(O,T), "")
	pspict.TraceSegment( Segment(T,A), "")

	axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(1,1)) )
	axes.SansDeco()
	axes.AjusteFonction(f,0,1)
	pspict.TraceFonction(f,"linecolor=blue",0,1)
	pspict.TraceAxes(axes)
	
	fig.AjoutePspicture(pspict)
	fig.DilateX(1)
	fig.DilateY(1)
	fig.Dilate(3)
	fig.Conclure()
	fig.EcrireFichier()

def Cree_graphs(nom,ListeFonctions):
	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	for S in ListeFonctions:
		f = S[0]
		mx = S[1]
		Mx = S[2]
		#n_points = int(abs(Mx-mx)*10)
		n_points = 100
		DilX = S[3]
		DilY = S[4]
		pspict=pspicture()
		axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(1,1)) )
		#axes.SansDeco()
		axes.AjusteFonction(f,mx,Mx)
		if len(S)>=6:
			axes.AjouteOption(S[5])
		pspict.TraceFonction(f,"plotpoints="+str(n_points)+",linecolor=blue",mx,Mx)
		pspict.TraceAxes(axes)
		#pspict.TraceBB()
		pspict.DilateX(DilX)
		pspict.DilateY(DilY)
	
		ssfig = subfigure("La fonction $x\\mapsto"+f.latex+"$","labelpetit")
		ssfig.AjoutePspicture(pspict)
		fig.AjouteSSfigure(ssfig)

	fig.Conclure()
	fig.EcrireFichier()
	

def GraphsElemes():

	ListeFonctions = []
	#			fonction	mx	Mx	DilateX		DilateY
	ListeFonctions.append([Fonction("math.exp(x)"),	-3,	2,	1.2,		0.9	])
	ListeFonctions.append([Fonction("math.exp(-x)"),	-2,	3,	1.2,		0.9	])
	ListeFonctions.append([Fonction("-math.exp(x)"),	-3,	2,	1.2,		0.7	])
	ListeFonctions.append([Fonction("-math.exp(-x)"),	-2,	3,	1.2,		0.7	])
	ListeFonctions.append([Fonction("math.exp(x-2)"),	-1,	4,	1.2,		0.9	])
	ListeFonctions.append([Fonction("math.exp(x)-2"),	-3,	2,	1.2,		0.9	])

	Cree_graphs("DessinExp",ListeFonctions)

	ListeFonctions = []
	#			fonction	mx	Mx	DilateX		DilateY
	ListeFonctions.append([Fonction("math.log(x)"),	0.05,	10,	1,		1	])
	ListeFonctions.append([Fonction("math.log10(x)"),	0.05,	15,	1,		3	])
	ListeFonctions.append([Fonction("math.log(1/x)"),	0.01,	2.5,	5,		1	])

	Cree_graphs("DessinLog",ListeFonctions)

	ListeFonctions = []
	#			fonction	mx	Mx	DilateX		DilateY
	ListeFonctions.append([Fonction("math.abs(x)"),	-4,	4,	0.8,		1	])
	ListeFonctions.append([Fonction("math.abs(x-2)"),	-4,	4,	0.8,		1	])
	ListeFonctions.append([Fonction("math.abs(x)-2"),	-4,	4,	1,		1	])

	Cree_graphs("DessinAbs",ListeFonctions)

	ListeFonctions = []
	#			fonction	mx	Mx	DilateX		DilateY
	ListeFonctions.append([Fonction("math.cosh(x)"),	-2.5,	2.5,	1.2,		1	])
	ListeFonctions.append([Fonction("math.sinh(x)"),	-2.5,	2.5,	1.2,		1	])

	Cree_graphs("DessinHyperbolique",ListeFonctions)

def DessinSinxx():
	pspict=pspicture()
	fig = GenereFigure(REP,"Sinxx")

	f = Fonction("math.sin(x)/x")
	mx = -15
	Mx = 15
	n_points = 100

	axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(1,1.5)) )
	axes.AjouteOption("Dx=5")
	axes.AjusteFonction(f,mx,Mx)

	pspict.TraceFonction(f,"plotpoints="+str(n_points)+",linecolor=blue",mx,Mx)
	pspict.TraceAxes(axes)
	pspict.DilateX(0.5)
	pspict.DilateY(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()
	
def DessinAbsx():
	pspict=pspicture()
	fig = GenereFigure(REP,"Absx")

	f = Fonction("math.abs(x)")
	g = Fonction("math.abs(x-2)")
	h = Fonction("math.abs(x)-1")
	h.listeExtrema.append( h.PointDessus(0) )		# Il faut mettre ce minimum à la main.
	mx = -4
	Mx = 4
	n_points = 100

	axes = Axes( Point(0,0), BoundingBox(Point(0,-2), Point(1,1.5)) )
	axes.AjouteOption("Dx=5")
	axes.AjusteFonction(f,mx,Mx)
	axes.AjusteFonction(g,mx,Mx)
	axes.AjusteFonction(h,mx,Mx)

	pspict.TraceFonction(f,"plotpoints="+str(n_points)+",linecolor=blue",mx,Mx)
	pspict.TraceFonction(g,"plotpoints="+str(n_points)+",linecolor=cyan",mx,Mx)
	pspict.TraceFonction(h,"plotpoints="+str(n_points)+",linecolor=red",mx,Mx)

	pspict.MarquePoint( f.PointDessus(Mx),0.3,90,"none","$x\mapsto "+f.latex+"$")
	pspict.MarquePoint( g.PointDessus(Mx),1.3,0,"none","$x\mapsto "+g.latex+"$")
	pspict.MarquePoint( h.PointDessus(Mx),1.3,0,"none","$x\mapsto "+h.latex+"$")

	pspict.TraceAxes(axes)
	#pspict.DilateX(0.5)
	#pspict.DilateY(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()
	

def DessinCosxx():
	pspict=pspicture()
	fig = GenereFigure(REP,"Cosxx")

	f = Fonction("math.cos(x)/x")

	mx1 = 0.2
	Mx1 = 15
	mx2 = -mx1
	Mx2 = -Mx1

	n_points = 100

	axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(1,1.5)) )
	axes.AjouteOption("Dx=5")
	axes.AjusteFonction(f,mx1,Mx1)
	axes.AjusteFonction(f,mx2,Mx2)

	pspict.TraceFonction(f,"plotpoints="+str(n_points)+",linecolor=blue",mx1,Mx1)
	pspict.TraceFonction(f,"plotpoints="+str(n_points)+",linecolor=blue",mx2,Mx2)

	pspict.TraceAxes(axes)
	pspict.DilateX(0.5)
	#pspict.DilateY(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()
	


def ExoXLVL():
	pspict=pspicture()
	fig =GenereFigure(REP,"ExoXLVL")
#	fig = figure("\CaptionFig"+nom,"LabelFig"+nom,REP+"/"+"Fig_"+nom+".pstricks")

	hdx=2
	hdy=2
	bgx=-2
	bgy=-2

	A=Point(bgx,hdy)
	B=Point(hdx,hdy)
	C=Point(hdx,bgy)
	D=Point(bgx,bgy)

	dist = 0.1		# La distance entre les axes et le bord du carré quand ça ne touche pas

	O = Point(0,0)
	X = Point(1,0)
	Y = Point(0,1)

	axes = Axes( Point(0,0), BoundingBox(Point(D.x-1,D.y-1), Point(B.x+1,B.y+1)) )
	axes.AjouteOption("linewidth=0.7mm")
	axes.SansDeco()
	pspict.TraceAxes(axes)

	zA = Rectangle( A, Point(-dist,dist) )	
	zB = Rectangle( B, O )	
	zC = Rectangle( Point(dist,-dist), C )	
	zD = Rectangle( O,D )
	pspict.MarquePoint( zA.centre,0,0,"none","$xy$" )
	pspict.MarquePoint( zB.centre,0,0,"none","$x-y$" )
	pspict.MarquePoint( zC.centre,0,0,"none","$x+y$" )
	pspict.MarquePoint( zD.centre,0,0,"none","$x^2y$" )


	pspict.TraceRectangle(zA,"linecolor=blue,linestyle=dashed")
	pspict.TraceRectangle(zB,"linecolor=red,linestyle=dashed")
	pspict.TraceRectangle(zC,"linecolor=green,linestyle=dashed")
	pspict.TraceRectangle(zD,"linecolor=cyan,linestyle=dashed")

	
	fig.AjoutePspicture(pspict)
	fig.DilateX(1)
	fig.DilateY(1)
	fig.Conclure()
	fig.EcrireFichier()


def Exo44():
	fig =GenereFigure(REP,"QQa")

	axes = Axes( Point(0,0), BoundingBox(Point(-2,-2), Point(2,2)) )
	axes.SansDeco()

	N=Point( axes.O.x,axes.BB.hd.y )
	S=Point( axes.O.x,axes.BB.bg.y )
	O=Point( axes.BB.bg.x,axes.O.y )
	E=Point( axes.BB.hd.x,axes.O.y )
	SO=Point(O.x,S.y)
	NE=Point(E.x,N.y)
	C=axes.O

	pspictGene=pspicture()
	pspictGene.TraceAxes(axes)

# Premier dessin.
	pspict = copy.deepcopy(pspictGene)

	l = Segment(N,S)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	
	ssfig = subfigure("Premier","labela")
	ssfig.AjoutePspicture(pspict)

	fig.AjouteSSfigure(ssfig)

# Second dessin.
	pspict = copy.deepcopy(pspictGene)

	l = Segment(N,C)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	l = Segment(C,E)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	
	ssfig = subfigure("Deuxième","labelb")
	ssfig.AjoutePspicture(pspict)

	fig.AjouteSSfigure(ssfig)

# Troisième dessin.
	pspict = copy.deepcopy(pspictGene)

	l = Segment(SO,NE)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	
	ssfig = subfigure("Troisième","labelb")
	ssfig.AjoutePspicture(pspict)

	fig.AjouteSSfigure(ssfig)

# Quatrième dessin.
	print "Je rentre dans le gros calcul"
	pspict = copy.deepcopy(pspictGene)

	f = Fonction("math.log(x)")
	pspict.TraceFonctionOndule(f,0.1,3,0.1,0.07,"linecolor=red")
	
	ssfig = subfigure("Quatrième","labelb")
	ssfig.AjoutePspicture(pspict)

	fig.AjouteSSfigure(ssfig)
	print "Je suis sorti du gros calcul"

# Cinquième dessin.
	pspict = copy.deepcopy(pspictGene)

	l = Segment(S,N)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	l = Segment(E,O)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	
	ssfig = subfigure("Cinquième","labelb")
	ssfig.AjoutePspicture(pspict)

	fig.AjouteSSfigure(ssfig)

# Sixième dessin.
	pspict = copy.deepcopy(pspictGene)

	l = Segment(S,N)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	l = Segment(E,O)
	pspict.TraceSegmentOndule(l,0.1,0.08,"linecolor=red")
	
	ssfig = subfigure("Siwième","labelb")
	ssfig.AjoutePspicture(pspict)

	fig.AjouteSSfigure(ssfig)


# Conclusion +++
	fig.Conclure()
	fig.EcrireFichier()


def Exo45():
	pspict=pspicture()
	fig =GenereFigure(REP,"QCb")

	axes = Axes( Point(0,0), BoundingBox(Point(-2,-2), Point(2,2)) )
	axes.SansDeco()
	pspict.TraceAxes(axes)

	l = Segment(axes.C,axes.N)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")
	l = Segment(axes.C,axes.E)
	pspict.TraceSegmentOndule(l,0.1,0.07,"linecolor=red")

	

	pspict.MarquePoint( Segment(axes.C,axes.NO).Milieu(),0,0,"none","$xy$")
	pspict.MarquePoint( Segment(axes.C,axes.NE).Milieu(),0,0,"none","$\sin(xy)$")
	pspict.MarquePoint( Segment(axes.C,axes.SO).Milieu(),0,0,"none","$xy$")
	pspict.MarquePoint( Segment(axes.C,axes.SE).Milieu(),0,0,"none","$xy$")

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def DisqueConv():
	pspict=pspicture()
	fig = GenereFigure(REP,"DisqueConv")

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(3,3)) )
	axes.SansDeco()
	pspict.TraceAxes(axes)

	C = Point(1.3,1.3)
	Mar = C.Translate(0.2,0.2)

	Cer = Cercle(C,1)
	
	pspict.TraceCercle(Cer,"linecolor=red,fillcolor=green, fillstyle=vlines,hatchcolor=green")
	pspict.MarquePoint(C,0,0,"*","")
	pspict.MarquePoint(Mar,0,0,"none","$z_0$")

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def EssOndule():
	pspict=pspicture()
	fig = GenereFigure(REP,"EssOndule")

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(3,3)) )
	axes.SansDeco()
	pspict.TraceAxes(axes)

	f = Fonction("math.cos(x)/x")

	pspict.TraceFonctionOndule( f,-15,15,0.5,0,"linecolor=red" )	

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def LaurinExp():
	pspict=pspicture()
	fig = GenereFigure(REP,"Laurin")

	f = Fonction("math.exp(x)")
	f1 = Fonction("1+x")
	f2 = Fonction("1+x+x^2/2")
	mx = -2
	Mx = 2

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(3,3)) )
	axes.AjusteFonction(f,mx,Mx)
	axes.AjusteFonction(f1,mx,Mx)
	axes.AjusteFonction(f2,mx,Mx)
	#axes.SansDeco()
	pspict.TraceAxes(axes)

	pspict.TraceFonction(f,"linecolor=blue",mx,Mx)	
	pspict.TraceFonction(f1,"linecolor=green",mx,Mx)	
	pspict.TraceFonction(f2,"linecolor=red",mx,Mx)	

	pspict.DilateX(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def IntRectangle():
	pspict=pspicture()
	fig = GenereFigure(REP,"IntRectangle")

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(3,3)) )
	#axes.SansDeco()

	O = Point(0,0)
	P = Point(1,2)
	R = Rectangle(O,P)

	pspict.TraceRectangle(R,"linecolor=red,fillstyle=vlines,hatchcolor=green")
	pspict.TraceAxes(axes)

	pspict.Dilate(1)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def IntTriangle():
	pspict=pspicture()
	fig = GenereFigure(REP,"IntTriangle")

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(3,3)) )
	#axes.SansDeco()

	A = Point(0,0)
	B = Point(0,2)
	C = Point(2,2)
	T = Triangle(A,B,C)

	pspict.TraceTriangle(T,"linecolor=red,fillstyle=vlines,hatchcolor=green")
	pspict.TraceAxes(axes)

	pspict.Dilate(1)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def IntEcourbe():
	pspict=pspicture()
	fig = GenereFigure(REP,"IntEcourbe")

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(3,3)) )
	#axes.SansDeco()

	mx = 1
	Mx = 3

	f = Fonction("(x-2)^2+2.5")
	g = Fonction("math.sin(x)+0.5")
	axes.AjusteFonction(f,mx,Mx)	
	axes.AjusteFonction(g,mx,Mx)	

	surface = SurfaceEntreFcnctions(f,g,mx,Mx)
	surface.AjouteOption("linecolor=red,fillstyle=vlines,hatchcolor=green")
	pspict.TraceSurfaceEntreFonction(surface)
	pspict.TraceFonction(f,mx,Mx,"linecolor=red")
	pspict.TraceFonction(g,mx,Mx,"linecolor=red")
	C = f.PointDessus(Mx)
	pspict.MarquePoint(C,0.3,45,"none","$\\beta(x)$")
	D = g.PointDessus(Mx)
	pspict.MarquePoint(D,0.5,0,"none","$\\alpha(x)$")

	R = Rectangle(Point(mx,f.PointDessus(mx).y),Point(Mx,g.PointDessus(Mx).y))
	pspict.TraceRectangle(R,"linecolor=blue,linestyle=dashed")

	pspict.TraceAxes(axes)

	pspict.Dilate(1)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def IntBoutCercle():
	pspict=pspicture()
	fig = GenereFigure(REP,"IntBoutCercle")

	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(1.5,1.5)) )
	#axes.SansDeco()

	rayon = 0.5
	A = Point(0,rayon)
	C = Cercle(A,rayon)
	O = Point(0,0)
	S = Segment(O,Point(1,1))
	Op = CercleInterLigne(C,S)[0]
	I = CercleInterLigne(C,S)[1]
	L = Segment(Op,I)
	mx = L.I.x
	Mx = L.F.x
	
	La = L.AugmenteTaille(0.5,0.5)
	pspict.TraceCercle(C,"linecolor=blue")
	f = L.Fonction
	g = Fonction("-((math.sqrt(1-4*x^2)-1)/2)")		# Ceci est un peu hard-codé par rapport à la donnée du cerlce

	surface = SurfaceEntreFcnctions(f,g,mx,Mx)
	surface.AjouteOption("linecolor=red,fillstyle=vlines,hatchcolor=green")
	pspict.TraceSurfaceEntreFonction(surface)
	pspict.TraceSegment(La,"linecolor=red")
	pspict.TraceFonction(g,mx,Mx,"linecolor=red")


	pspict.TraceAxes(axes)

	pspict.Dilate(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def IntDeuxCarres():
	pspict=pspicture()
	fig = GenereFigure(REP,"IntDeuxCarres")

	l = 1
	L = 2
	axes = Axes( Point(0,0), BoundingBox(Point(-L-0.5,-L-0.5), Point(L+0.5,L+0.5)) )

	O = Point(0,0)
	A = Point(l,l)
	B = Point(L,L)
	C = Point(-l,-l)
	D = Point(-L,-L)
	Ri = Rectangle(C,A)
	Re = Rectangle(D,B)

	pspict.TraceRectangle(Re,"linecolor=red,fillstyle=vlines,hatchcolor=green")
	pspict.TraceRectangle(Ri,"linecolor=red,fillstyle=solid,fillcolor=white")
	pspict.TraceAxes(axes)

	pspict.Dilate(1)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def SurfVar():
	pspict=pspicture()
	fig = GenereFigure(REP,"SurfVar")

	O = Point(0,0)
	X = Point(1,0)
	Y = Point(0,1)
	eX = Segment(O,X)
	eY = Segment(O,Y)
	W = Cercle( O,1.5 )

	#pspict.TraceRectangle(Re,"linecolor=red,fillstyle=vlines,hatchcolor=green")
	#pspict.TraceRectangle(Ri,"linecolor=red,fillstyle=solid,fillcolor=white")

	pspict.TraceSegment(eX,"arrows=->")
	pspict.TraceSegment(eY,"arrows=->")
	pspict.TraceCercle(W,"")


	pspict.Dilate(1)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def CercleImplicite():
	pspict=pspicture()
	fig = GenereFigure(REP,"CercleImplicite")

	O = Point(0,0)
	r = 2
	alpha = math.pi/3
	C = Cercle(O,r)
	Q = Point(-r,0)
	P = Point(r*math.cos(alpha),r*math.sin(alpha))
	Pp = Point(r*math.cos(alpha),-r*math.sin(alpha))
	axes = Axes( Point(0,0), BoundingBox(Point(-r-0.5,-r-0.5), Point(r+0.5,r+0.5)) )
	axes.SansDeco()

	pspict.TraceCercle(C,"")
	pspict.TraceAxes(axes)
	pspict.MarquePoint(Q,0.3,180,"*","$Q$")
	pspict.MarquePoint(P,0.3,45,"*","$P$")
	pspict.MarquePoint(Pp,0.3,-45,"*","$P'$")

	pspict.Dilate(1)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def ExempleNonRang():
	pspict=pspicture()
	fig = GenereFigure(REP,"ExempleNonRang")

	f = Fonction("x^(3/2)")
	g = Fonction("-x^(3/2)")
	mx = 0
	Mx = 1
	axes = Axes( Point(0,0), BoundingBox(Point(-1,-1), Point(1.5,1.5)) )
	axes.SansDeco()
	axes.AjusteFonction(f,mx,Mx)
	axes.AjusteFonction(g,mx,Mx)


	pspict.TraceFonction(f,mx,Mx,"linecolor=blue")
	pspict.TraceFonction(g,mx,Mx,"linecolor=blue")
	pspict.TraceAxes(axes)

	pspict.DilateX(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def CoinPasVar():
	pspict=pspicture()
	fig = GenereFigure(REP,"CoinPasVar")

	l = 1
	O = Point(0,0)
	P = Point(l,0)
	Q = Point(-l,0)
	N = Point(0,l)
	t1 = Segment(Q,N).milieu()
	t2 = Segment(P,N).milieu()
	axes = Axes( Point(0,0), BoundingBox(Point(-l-0.3,-0.3), Point(l+0.3,l+0.3)) )
	axes.SansDeco()

	pspict.TraceAxes(axes)
	pspict.TraceSegment( Segment(Q,N),"linecolor=blue" )
	pspict.TraceSegment( Segment(P,N),"linecolor=blue" )
	pspict.MarquePoint(N,0.3,45,"*","$N$")
	pspict.MarquePoint(t1,0.3,135,"*","$t_1$")
	pspict.MarquePoint(t2,0.3,45,"*","$t_2$")

	pspict.Dilate(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def CercleVarCarte():
	pspict=pspicture()
	fig = GenereFigure(REP,"CercleVarCarte")

	r = 1
	alpha = math.pi/6
	P = Point( r*math.cos(alpha),r*math.sin(alpha) )
	O = Point(0,0)
	X = Point(1,0)
	S = Point(0,-r)
	C = Cercle(O,r)
	axes = Axes( Point(0,0), BoundingBox(Point(-r-0.3,-r-0.3), Point(r+0.3,r+0.3)) )
	axes.SansDeco()

	pspict.TraceSegment( Segment(O,P),"linecolor=green" )
	pspict.TraceAxes(axes)
	pspict.TraceCercle(C,"linecolor=blue")
	pspict.MarquePoint(S,0.3,-45,"*","$S$")
	pspict.MarquePoint(P,0.3,alpha*180/math.pi,"*","$P$")
	pspict.MarqueAngle(X,O,P,"$\\theta$","")

	pspict.Dilate(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()


def SqrtCarre():
	pspict=pspicture()
	fig = GenereFigure(REP,"SqrtCarre")

	f1 = Fonction("sqrt(x)")
	f2 = Fonction("x^2")
	mx = 0
	Mx = 1.2
	pspict.TraceFonction(f1,mx,Mx,"linecolor=blue")
	pspict.TraceFonction(f2,mx,Mx,"linecolor=red")

	axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(1,1)) )
	#axes.SansDeco()
	axes.BB = pspict.BB
	pspict.TraceAxes(axes)

	pspict.Dilate(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def TriangleUV():
	pspict=pspicture()
	fig = GenereFigure(REP,"TriangleUV")

	mx = 0
	Mx = 2
	O = Point(0,0)
	var('x')
	f = Fonction(2-x)
	milieu = f.PointDessus((Mx-mx)/2)
	P = f.PointDessusNormal(milieu.x,0.1)
	nu = f.VecteurNormal(milieu.x).lie(P)
	T = f.VecteurTangent(milieu.x).lie(P).inverse()
	uu = Vecteur(O,Point(1,0))
	uv = Vecteur(O,Point(0,1))

	f.AjouteSurface(mx,Mx)
	f.ListeSurface[-1].options.DicoOptions["fillstyle"] = "vlines"


	pspict.TraceFonction(f,mx,Mx,"linecolor=blue")
	#pspict.MarquePoint(P,0,0,"*","")

	axes = Axes( Point(0,0), BoundingBox(Point(0,0), Point(Mx+0.5,Mx+0.5)) )
	axes.SansDeco()
	pspict.TraceAxes(axes)

	pspict.TraceVecteur(T,"linecolor=red").MarqueVecteur(0.3,45,"$T$")
	pspict.TraceVecteur(nu,"linecolor=green").MarqueVecteur(0.3,-45,"$\\nu$")
	pspict.TraceVecteur(uu,"linecolor=green,linewidth=0.05").MarqueVecteur(0.3,-90,"$1_u$")
	pspict.TraceVecteur(uv,"linecolor=red,linewidth=0.05").MarqueVecteur(0.3,180,"$1_v$")

	pspict.Dilate(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def CercleTnu():

	def PlaceTg(C,angle,a1,mT,a2,mn):
		T = C.VecteurTangent(angle)
		nu = C.VecteurNormal(angle)
		pspict.TraceVecteur(T,"linecolor=red").MarqueVecteur(0.3,a1,mT)
		pspict.TraceVecteur(nu,"linecolor=green").MarqueVecteur(0.3,a2,mn)

	pspict=pspicture()
	fig = GenereFigure(REP,"CercleTnu")

	O = Point(0,0)
	C = Cercle(O,1)

	PlaceTg(C,30,45,"$T$",-45,"$\\nu$")
	PlaceTg(C,110,120,"$1_{\\theta}$",45,"$1_r$")
	pspict.TraceCercle(C,"linecolor=blue,fillstyle=vlines,hatchcolor=blue")

	pspict.Dilate(2)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

def ExoVarj():
	pspict=pspicture()
	fig = GenereFigure(REP,"ExoVarj")

	var('x')
	f1 = Fonction(-sqrt(sqrt(4*x**2 + 1) - x**2 - 1))
	f2 = Fonction(sqrt(sqrt(4*x**2 + 1) - x**2 - 1))

	pspict.TraceFonction(f1,-1,1,"linecolor=red")
	pspict.TraceFonction(f2,-1,1,"linecolor=blue")

	pspict.TraceAxesDefaut()

	pspict.Dilate(3)

	fig.AjoutePspicture(pspict)
	fig.Conclure()
	fig.EcrireFichier()

ExoVarj()
#CercleTnu()
#TriangleUV()
#SqrtCarre()
#CoinPasVar()
#CercleVarCarte()
#ExempleNonRang()
#SurfVar()
#IntDeuxCarres()
#IntBoutCercle()
#IntEcourbe()
#IntTriangle()
#IntRectangle()
#LaurinExp()
#dessinlim()
#GraphsElemes()
#ExoXLVL()
#Ondule()
#Exo44()
#Exo45()
#DisqueConv()

#EssOndule()
#DessinSinxx()
#DessinCosxx()
#DessinAbsx()
