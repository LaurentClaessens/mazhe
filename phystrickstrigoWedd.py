from phystricks import *
def trigoWedd():
    pspict,fig = SinglePicture("trigoWedd")

    x=var('x')
    C=Circle(Point(0,0),1)
    U=C.get_point(0)
    Z=C.get_point(30)
    q=2
    Q=Point(q,0)

    Z.put_mark(0.3,Z.advised_mark_angle(pspict),"$z_0$",automatic_place=pspict)
    Q.put_mark(0.1,-90,"$q$",automatic_place=(pspict,"N"))
    U.put_mark(0.2,-45,"$1$",automatic_place=(pspict,"N"))

    pspict.axes.no_graduation()


    pspict.DrawGraphs(C,Z,Q,U)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
