from yanntricks import *


def Refraction():
    pspict, fig = SinglePicture("Refraction")

    O = Point(0, 0)
    plan = Segment(Point(-3, 0), Point(3, 0))
    # N est le vecteur vertical, de bas en haut
    N = AffineVector(Point(0, -2), Point(0, 2))
    N.put_mark(0.3, 0, r"$\overline{ N }$", pspict=pspict)

    A = Point(1, 1)
    B = Point(-2, -1)
    a = AffineVector(A, O)
    b = AffineVector(O, B).normalize(a.length)
    a.parameters.color = "red"
    b.parameters.color = "blue"

    theta1 = AngleAOB(a.I, O, N.F)
    theta2 = AngleAOB(B, O, N.I)
    theta1.put_mark(text=r"$\theta_1$", pspict=pspict)
    theta2.put_mark(text=r"$\theta_2$", pspict=pspict)

    pspict.DrawGraphs(plan, N, theta1, theta2, a, b)
    pspict.dilatation(1)
    fig.conclude()
    fig.write_the_file()
