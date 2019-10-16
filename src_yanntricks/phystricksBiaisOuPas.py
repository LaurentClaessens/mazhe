from yanntricks import *
def BiaisOuPas():
    pspict,fig = SinglePicture("BiaisOuPas")
    pspict.dilatation(2.5)

    
    x=var('x')
    def normale(m,s):
        return phyFunction( 1/(s*sqrt(2*pi))*exp(-((x-m)/s)**2) ).graph(-3,3)

    f1=normale(0,1)
    f2=normale(-0.2,0.2)

    f2.linea_plotpoints=1000

    a=0.5
    I=Segment(Point(-a,0),Point(a,0))
    measure=MeasureLength(I,0.2)
    measure.put_mark(0.3,measure.advised_mark_angle(pspict),"\( I\)",pspict=pspict)
    measure.parameters.color="cyan"

    f2.parameters.color="red"

    pspict.DrawGraphs(f1,f2,measure)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

