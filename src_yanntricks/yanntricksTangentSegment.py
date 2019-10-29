from yanntricks import *
def TangentSegment():
    pspict,fig = SinglePicture("TangentSegment")

    x=var('x')
    f=phyFunction(2*sin(x/2)).graph(-pi,2*pi+1)
    pspict.DrawGraphs(f)
    for x0 in [-pi/2,pi] :
        P=f.get_point(x0)
        seg=f.get_tangent_segment(x0)
        seg=seg.dilatation(2)
    pspict.DrawGraphs(seg,P)

    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()


