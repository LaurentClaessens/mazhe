# -*- coding: utf8 -*-
from phystricks import *
def LesSpheres():
	pspicts,fig = MultiplePictures("LesSpheres",3)

	pspicts[0].mother.caption=u"La sphère unité pour la norme $\| . \|_1$"
	pspicts[1].mother.caption=u"La sphère unité pour la norme $\| . \|_2$"
	pspicts[2].mother.caption=u"La sphère unité pour la norme $\| . \|_{\infty}$"

	r=1
	# La norme |  |_1
	A=Point(0,r)
	B=Point(-r,0)
	C=Point(0,-r)
	D=Point(r,0)
	AB=Segment(A,B)
	BC=Segment(B,C)
	CD=Segment(C,D)
	DA=Segment(D,A)
	pspicts[0].DrawGraphs(AB,BC,CD,DA)
	pspicts[0].BB.AddX(-r-1)
	pspicts[0].BB.AddX(r+1)
	pspicts[0].DrawDefaultAxes()

	# La norme |  |_2
	O=Point(0,0)
	Cercle = Circle(O,r)
	pspicts[1].DrawGraph(Cercle)
	pspicts[1].BB.AddX(-r-1)
	pspicts[1].BB.AddX(r+1)
	pspicts[1].DrawDefaultAxes()

	# La norme |  |_infini
	A=Point(r,r)
	B=Point(-r,r)
	C=Point(-r,-r)
	D=Point(r,-r)
	AB=Segment(A,B)
	BC=Segment(B,C)
	CD=Segment(C,D)
	DA=Segment(D,A)
	pspicts[2].DrawGraph(AB)
	pspicts[2].DrawGraph(BC)
	pspicts[2].DrawGraph(CD)
	pspicts[2].DrawGraph(DA)
	pspicts[2].BB.AddX(-r-1)
	pspicts[2].BB.AddX(r+1)
	pspicts[2].DrawDefaultAxes()

	fig.conclude()
	fig.write_the_file()
