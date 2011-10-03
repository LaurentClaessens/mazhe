from phystricks import *
def BiaisOuPas():
    pspict,fig = SinglePicture("BiaisOuPas")

    
    x=var('x')
    def normale(m,s):
        return phyFunction( 1/(s*sqrt(2*pi))*exp(-((x-m)/2)**2) )


    pspict.DrawGraphs(<++>)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
