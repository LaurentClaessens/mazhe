from yanntricks import *
def CheminFresnel():
    pspict,fig = SinglePicture("CheminFresnel")

    x=var('x')
    R=2
    gamma1=ParametricCurve(x,0).graph(0,R)
    gamma2=PolarCurve(R).graph(0,pi/4)
    gamma3=ParametricCurve(x*cos(pi/4),x*sin(pi/4)).graph(0,R)

    gamma1.put_arrow(R/2)
    gamma2.put_arrow(pi/8)
    gamma3.put_arrow(R/2)

    P1=gamma1.get_point(R/2)
    P2=gamma2.get_point(pi/8)
    P3=gamma3.get_point(R/2)

    P1.parameters.symbol=""
    P2.parameters.symbol=""
    P3.parameters.symbol=""

    P1.put_mark(0.1,P1.advised_mark_angle(pspict),"\( \gamma_1\)",pspict=pspict)
    P2.put_mark(0.1,P2.advised_mark_angle(pspict),"\( \gamma_2\)",pspict=pspict)
    P3.put_mark(0.1,P3.advised_mark_angle(pspict),added_angle=180,text="\( \gamma_3\)",pspict=pspict)

    gamma1.parameters.color="blue"
    gamma2.parameters.color=gamma1.parameters.color
    gamma3.parameters.color=gamma1.parameters.color
    

    pspict.DrawGraphs(gamma1,gamma2,gamma3,P1,P2,P3)
    pspict.axes.no_numbering()
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

