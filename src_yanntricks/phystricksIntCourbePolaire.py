from yanntricks import *
def IntCourbePolaire():
    pspict,fig = SinglePicture("IntCourbePolaire")

    x=var('x')
    a = 2
    f=a*sqrt(cos(2*x))

    curve = PolarCurve(f)
    part1=curve.graph(-pi/4,pi/4)
    part2=curve.graph(-pi/4+pi,pi/4+pi)

    pspict.DrawGraphs(part1,part2)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

