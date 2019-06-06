# -*- coding: utf8 -*-
from sage.all import *


def Dynkin():
    """
    This proves that the Dynkin diagram with a triple point whose branches are
    of length 1,3,5 does not exist.

    The result is zero.
    """
    a=[var('a'+str(i-1)) for i in range(1,11)]
    l=9
    a[1]=1
    squares = sum( [a[i]**2 for i in range(1,l+1)] )     # The sum goes to l
    lines = sum(  [a[i]*a[i+1] for i in [1,2,3,4,5,6,7]  ]   )+a[3]*a[9]  # The sum goes up to l-1
    f=symbolic_expression(squares - lines)
    X = solve( [f.diff(a[i])==0 for i in range(2,l+1)],[ a[i] for i in range(2,l+1)  ]  )   # We put a1=1, so we don't solve with respect to a1
    print f(   *tuple(  [  X[0][i].rhs() for i in range(0,l-1)  ]  )   )


def gXgemu():
    a,b,t=var('a,b,t')
    X=matrix(3,3,[0,a,b,-a,0,0,-b,0,0])
    g=matrix(3,3,[cos(t),sin(t),0,-sin(t),cos(t),0,0,0,1])
    A=g*X*g.inverse()
    for i in range(0,3):
        for j in range(0,3):
            print i,j," -- ",A[i,j].simplify_full()
    Y=matrix(3,3,[0,t,0,-t,0,0,0,0,0])
    g=Y.exp()
    print g
    for i in range(0,3):
        for j in range(0,3):
            print i,j," -- ",g[i,j].real_part().simplify_full()
