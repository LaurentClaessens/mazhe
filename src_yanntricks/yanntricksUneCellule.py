from yanntricks import *


def UneCellule():

    def Sigma(dep, leng):
        sigma = [dep]
        d = dep
        for l in leng:
            d = d+l
            sigma.append(d)
        return sigma

    pspict, fig = SinglePicture("UneCellule")

    a1 = 1
    l1 = [1.2, 1.5, 0.5, 1, 1]
    sigma1 = Sigma(a1, l1)
    b1 = a1+sum(l1)
    a2 = 2
    l2 = [0.5, 1.5, 1]
    sigma2 = Sigma(a2, l2)
    b2 = a2+sum(l2)
    for i in range(len(sigma1)):
        dist = 0.3+(1-(-1)**i)*0.15
        x = sigma1[i]
        P = Point(x, 0)
        if i == 0:
            P.put_mark(dist, -90, "$a_1=y_{10}$", pspict=pspict)
        elif i == len(sigma1)-1:
            P.put_mark(dist, -90, "$b_1=y_{1%s}$" % str(i),
                       pspict=pspict)
        else:
            P.put_mark(dist, -90, "$y_{1%s}$" % str(i), pspict=pspict)
        seg1 = Segment(P, Point(x, a2))
        seg1.parameters.style = "dotted"
        seg2 = Segment(Point(x, a2), Point(x, b2))
        pspict.DrawGraphs(P, seg1, seg2)

    for i in range(len(sigma2)):
        y = sigma2[i]
        P = Point(0, y)
        if i == 0:
            P.put_mark(0.3, 180, "$a_2=y_{20}$", pspict=pspict)
        elif i == len(sigma2)-1:
            P.put_mark(0.3, 180, "$b_2=y_{2%s}$" % str(i),
                       pspict=pspict)
        else:
            P.put_mark(0.3, 180, "$y_{2%s}$" % str(i), pspict=pspict)
        seg1 = Segment(P, Point(a1, y))
        seg1.parameters.style = "dotted"
        seg2 = Segment(Point(a1, y), Point(b1, y))
        pspict.DrawGraphs(P, seg1, seg2)

    cellule = Rectangle(Point(sigma1[3], sigma2[1]),
                        Point(sigma1[4], sigma2[2]))
    cellule.filled()
    cellule.fill_parameters.color = "lightgray"
    pspict.DrawGraphs(cellule)

    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    pspict.dilatation(1)

    fig.conclude()
    fig.write_the_file()
