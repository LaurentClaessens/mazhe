from yanntricks import *
def UnSurxInt():
    pspict,fig = SinglePicture("UnSurxInt")

    epsilon=0.3
    l=3
    a=1
    b=2
    x=var("x")
    f=phyFunction(1/x)
    F=[f.graph(-l,-epsilon),f.graph(epsilon,l)]
    surf=[SurfaceUnderFunction(f,-b,-a),SurfaceUnderFunction(f,a,b)]
    for s in surf:
        s.parameters.hatched()
        s.parameters.hatch.color="blue"
        s.Isegment.parameters.style="solid"
        s.Isegment.parameters.color="brown"
        s.Fsegment.parameters=s.Isegment.parameters

    pspict.DrawGraphs(F,surf)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

