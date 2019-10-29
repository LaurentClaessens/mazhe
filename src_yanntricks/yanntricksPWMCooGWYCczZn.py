
import itertools
from yanntricks import *


def action(k, l, m, P):
    """Act with the group on the point P"""
    z = P.x+I*P.y
    new_z = exp(I*pi*m/3)*z

    new_P = Point(new_z.real_part(), new_z.imag_part())

    new_P = new_P + l * Point(-1/2, sqrt(3)/2)
    new_P = new_P + k * Point(1, 0)

    return new_P


def move_polygon(k, l, m, polygon):
    """Move the polygon with the group."""
    new_vertices = [action(k, l, m, P) for P in polygon.vertices]
    return Polygon(new_vertices)


def fAB(P):
    return P.x-sqrt(3)*P.y

def fBC(P):
    return -P.x-sqrt(3)*P.y+1

def fAC(P):
    return P.y

def rfAB(P):
    return P.x+sqrt(3)*P.y

def rfBC(P):
    return -2*P.x-1

def rfAC(P):
    return -sqrt(3)*P.x/2-P.y/2

def gfAB(k,l,P):
    return P.x+sqrt(3)*P.y-k-l

def gfBC(k,l,P):
    return -2*P.x+2*k-l-1

def gfAC(k,l,P):
    return -sqrt(3)*P.x/2-P.y/2+sqrt(3)*k/2

def PWMCooGWYCczZn():
    pspicts, fig = MultiplePictures("PWMCooGWYCczZn", 3)
    pspicts[0].mother.caption = r"Le compact \( K\) et ses rotations."
    pspicts[1].mother.caption = r"Une maille du réseau des translations de \( G\)."
    pspicts[2].mother.caption = "Une partie du pavage complet."

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)
    
    pspicts[1].dilatation(2)

    # subfigure 1

    A = Point(0, 0)
    B = Point(1/2, sqrt(3)/6)
    C = Point(1, 0)

    rA = action(0,0,2,A)
    rB = action(0,0,2,B)
    rC = action(0,0,2,C)

    k=var('k')
    l=var('l')
    gA = action(k,l,2,A)
    gB = action(k,l,2,B)
    gC = action(k,l,2,C)


    a=var('a')
    b=var('b')
    L = action(0,0,2,Point(a,b))
    print("Lx", L.x.simplify_full())
    print("Ly", L.y.simplify_full())
    Q = action(k,l,2,Point(a,b))
    
    print(fAC(Q).simplify_full())


    base = Polygon(A, B, C)

    triangles = [base]
    for m in [1, 2, 3, 4, 5]:
        triangles.append(move_polygon(0, 0, m, base))

    pspicts[0].DrawGraphs(triangles)

    # subfigure 2

    u1 = Point(1, 0)
    u2 = Point(1/2, sqrt(3)/2)
    Z = u1 + u2

    parallelogram = Polygon(Point(0,0), u1, Z, u2)

    T0 = move_polygon(0,0,0,base)
    T1 = move_polygon(1,0,1,base)
    T2 = move_polygon(1,0,2,base)
    T3 = move_polygon(2,1,3,base)
    T4 = move_polygon(1,1,4,base)
    T5 = move_polygon(1,1,5,base)

    T4.edges_parameters.color = "red"

    trigs = [T0, T1, T2, T3, T4, T5]

    pspicts[1].DrawGraphs(T0, T1, T2, T5, T3, T4)

    # subfigure 3


    pavage = [base]
    N = 3
    for k, l, m in itertools.product(range(-N, N+1),
                                     range(-N, N+1),
                                     [0, 1, 2, 3, 4, 5]):

        pavage.append(move_polygon(k, l, m, base))

    pspicts[2].DrawGraphs(pavage)

    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
