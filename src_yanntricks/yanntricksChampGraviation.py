from yanntricks import *
def ChampGraviation():
    pspict,fig = SinglePicture("ChampGraviation")

    import numpy
    O=Point(0,0)
    mx=my=-4
    Mx=My=4
    R=0.7

    terre=Circle(O,R)
    terre.parameters.color="blue"

    pos_x=numpy.linspace(mx,Mx,15)
    pos_y=numpy.linspace(my,My,15)


    for x in pos_x:
        for y in pos_y:
                P=Point(x,y)
                if P.norm>R:
                    d=P.norm
                    F=2*Vector(P).fix_origin(P).normalize(1/d**2)
                pspict.DrawGraphs(F)

    pspict.DrawGraphs(terre)
    fig.conclude()
    fig.write_the_file()

