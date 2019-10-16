from yanntricks import *
def QuelCote():
    pspict,fig = SinglePicture("QuelCote")
    pspict.dilatation(2)

    x=var('x')
    f1=phyFunction(x+1/x+1)
    f2=phyFunction(x+1/(2*x**2)+1)
    llamI=-2
    llamF=-0.7
    llam = -1.2
    curve=ParametricCurve(f1,f2).graph(llamI,llamF)

    P=curve.get_point(llam)
    normal=curve.get_normal_vector(llam)
    Mnormal=-normal
    normal.parameters.color="green"
    Mnormal.parameters.color="green"
    Mnormal.parameters.style="dashed"
    second=curve.get_second_derivative_vector(llam)
    tangent_segment=curve.get_tangent_segment(llam)
    tangent_vector=curve.get_tangent_vector(llam)
    tangent_segment.parameters.color="brown"
    tangent_vector.parameters.color="brown"
    tangent_segment.parameters.style="dashed"
    tangent_vector.put_mark(0.5,0,"$\gamma'(t)$",pspict=pspict)
    normal.put_mark(0.3,90,"$n(t)$",pspict=pspict)
    Mnormal.put_mark(0.3,90,"$-n(t)$",pspict=pspict)
    second.put_mark(0.3,45,"$\gamma''(t)$",pspict=pspict)
    P.put_mark(0.3,-45,"$P$",pspict=pspict)

    pspict.DrawGraphs(curve,tangent_segment,tangent_vector,second,normal,Mnormal,P)
    fig.conclude()
    fig.write_the_file()

