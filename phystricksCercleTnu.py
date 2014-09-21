from phystricks import *
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
        n.put_mark(0.3,n.advised_mark_angle,"\( n\)",automatic_place=pspict)
        t.put_mark(0.3,t.advised_mark_angle+180,"\( e_{\\theta}\)",automatic_place=pspict)
        pspict.DrawGraphs(n,t)
        


    pspict.DrawGraphs(C)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
