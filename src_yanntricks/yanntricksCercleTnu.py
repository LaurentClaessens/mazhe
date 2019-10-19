from yanntricks import *
def CercleTnu():
    pspict,fig = SinglePicture("CercleTnu")

    x=var('x')
    C=Circle(Point(0,0),2)

    C.parameters.color="brown"
    C.parameters.hatched()
    C.parameters.hatch.color="blue"

    for alpha in [30,110]:
        n=C.get_normal_vector(alpha)
        n.parameters.color="green"
        t=C.get_tangent_vector(alpha)
        t.parameters.color="red"
        n.put_mark(0.3,n.advised_mark_angle(pspict),"\( n\)",pspict=pspict)
        t.put_mark(0.3,t.advised_mark_angle(pspict),added_angle=180,text="\( e_{\\theta}\)",pspict=pspict)
    pspict.DrawGraphs(n,t)
        
    pspict.DrawGraphs(C)
    fig.conclude()
    fig.write_the_file()

