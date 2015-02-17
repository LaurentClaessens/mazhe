from phystricks import *
def Parallelogramme():
    pspict,fig = SinglePicture("Parallelogramme")

    O=Point(0,0)

    a=Vector(3,0)
    b=Vector(2,2)
    a.put_mark(0.3,-45,"$a$",automatic_place=pspict)
    b.put_mark(0.3,90,"$b$",automatic_place=pspict)

    C=(a+b).F

    l1=Segment(b.F,C)
    l2=Segment(a.F,C)
    l1.parameters.style="dotted"
    l1.parameters.color="blue"
    l2.parameters=l1.parameters

    D=b.F.projection(a)

    h=Segment(b.F,D)
    h.parameters.style="dashed"
    h.put_mark(0.2,0,"$h$",automatic_place=pspict)

    theta=Angle(D,O,b.F)
    theta.put_mark(0.3,None,r"$\theta$",automatic_place=pspict)

    pspict.DrawGraphs(a,b,C,l1,l2,h,theta,D)
    #pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
