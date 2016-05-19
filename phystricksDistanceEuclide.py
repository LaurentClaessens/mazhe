from phystricks import *
def DistanceEuclide():
	pspict,fig=SinglePicture("DistanceEuclide")

	A=Point(1,4)
	B=Point(3,1)
	C=Point(B.x,A.y)
	A.put_mark(0.4,90,"$(A_x,A_y)$",automatic_place=(pspict,""))
	B.put_mark(1,0,"$(B_x,B_y)$",automatic_place=(pspict,""))
	C.put_mark(0.4,45,"$C$",automatic_place=(pspict,""))
	pspicts.DrawGraphs(A,B,C)

	Lab=Segment(A,B)
	Lac=Segment(A,C)
	Lbc=Segment(B,C)
	pspicts.DrawGraphs(Lab,Lac,Lbc)

	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
