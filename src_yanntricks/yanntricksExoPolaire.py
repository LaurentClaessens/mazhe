from yanntricks import *
def ExoPolaire():
    pspict,fig = SinglePicture("ExoPolaire")
    pspict.dilatation(1)
    
    O=Point(0,0)
    X=Point(1,0)

    P=Point(sqrt(3),1)
    P.put_mark(0.1,text="$(\sqrt{3},1)$",pspict=pspict,position="W")
    P.parameters.symbol=""

    v=Vector(P)
    m=v.midpoint()
    m.parameters.symbol=""
    m.put_mark(0.3,m.advised_mark_angle(pspict),"$l$",pspict=pspict)

    theta=AngleAOB(X,O,P,r=0.5)
    theta.put_mark(text=r"$\theta$",pspict=pspict)

    pspict.axes.no_numbering()

    pspict.DrawGraphs(P,m,theta,v)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()

