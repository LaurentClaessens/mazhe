from yanntricks import *
def trigoWedd():
    pspict,fig = SinglePicture("trigoWedd")

    x=var('x')
    C=Circle(Point(0,0),1)
    U=C.get_point(0)
    Z=C.get_point(30)
    q=2
    Q=Point(q,0)

    Z.put_mark(0.3,Z.advised_mark_angle(pspict),"$z_0$",pspict=pspict)
    Q.put_mark(0.1,text="$q$",pspict=pspict,position="N")
    U.put_mark(0.2,text="$1$",pspict=pspict,position="N")

    pspict.axes.no_graduation()


    pspict.DrawGraphs(C,Z,Q,U)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()

