from phystricks import *
def SuiteInverseAlterne():

    def suite(i):
        return SR((-1)**i)/i

    pspict,fig = SinglePicture("SuiteInverseAlterne")
    pspict.dilatation_Y(3)
    n=10
    for i in range(1,n+1):
        P=Point(i,suite(i))
        P.put_mark(0.3,(-1)**i*90,"$%s$"%(repr(suite(i))),pspict=pspict)
        pspict.DrawGraphs(P)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()


    fig.conclude()
    fig.write_the_file()
