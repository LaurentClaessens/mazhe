from yanntricks import *


def SuiteUnSurn():
    pspict, fig = SinglePicture("SuiteUnSurn")
    pspict.dilatation_Y(3)

    def suite(i):
        return SR(1)/i

    n = 10
    for i in range(1, n+1):
        y = suite(i)
        P = Point(i, float(y))
        P.put_mark(0.3, 90, "$%s$" % (repr(y)), pspict=pspict)
        print(P)
        pspict.DrawGraphs(P)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
