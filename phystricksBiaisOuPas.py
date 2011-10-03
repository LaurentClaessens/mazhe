from phystricks import *
def BiaisOuPas():
    pspict,fig = SinglePicture("BiaisOuPas")

    
    x=var('x')
    def normale(m,s):
        return phyFunction( 1/(s*sqrt(2*pi))*exp(-((x-m)/2)**2) )

    f1=normale(0,2)
    f2=normale(-0.2,1)

    f2.parameters.color="red"

    pspict.DrawGraphs(f1,f2)
    pspict.DrawDefaultAxes()
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
