from phystricks import *
def DefinitionCartesiennes():
	pspict,fig = SinglePicture("DefinitionCartesiennes")

	def PlacePoint(x,y,color):
		M=Point(x,y)
		M.put_mark(0.1,M.angle(),"$(%s,%s)$"%(str(x),str(y)),automatic_place=pspict)
		v=Vector(M)
		v.parameters.color=color
		Px=M.projection(pspict.single_axeX)
		Py=M.projection(pspict.single_axeY)
		seg1=Segment(M,Px)
		seg2=Segment(M,Py)
		seg1.parameters.color=color
		seg1.parameters.style="dashed"
		seg2.parameters=seg1.parameters
		pspict.DrawGraphs(seg1,seg2,M,v)

	PlacePoint(3,1,"blue")
	PlacePoint(-1.5,-2.5,"green")
	PlacePoint(-1,2.5,"brown")
	PlacePoint(1.5,-1,"cyan")
	#PlacePoint(2,2,"gray")
	pspict.DrawDefaultAxes()
	pspict.dilatation(1)
	fig.conclude()
	fig.write_the_file()
