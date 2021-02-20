"""
Some check for the Lie algebra so(1,3).

This file has to be attached to sage's terminal.

sage: import os
sage: os.chdir('/path/to/tex/sage')
sage: attach('sageSnip021.sage')

This should only print a list of 'True'.
"""


from sageSnip020 import matrix_M
from sageSnip020 import epsilon_matrices
from sageSnip020 import com


def do_work():
    """Do the work."""
    M = {1: matrix_M(3, 2),
         2: matrix_M(1, 3),
         3: matrix_M(2, 1)}
    N = {1: matrix_M(0, 1),
         2: matrix_M(0, 2),
         3: matrix_M(0, 3)}

    # Check [M_i, M_j]=epsilon_{ijk}M_k
    for kk in range(1, 4):
        for ll in range(1, 4):
            ans = epsilon_matrices(kk, ll, M)
            print(com(M[kk], M[ll]) == ans)

    # Check [M_i, N_j]=epsilon_{ijk}N_k
    for kk in range(1, 4):
        for ll in range(1, 4):
            ans = epsilon_matrices(kk, ll, N)
            print(com(M[kk], N[ll]) == ans)

    # Check [N_i, N_j]=-epsilon_{ijk}M_k
    for kk in range(1, 4):
        for ll in range(1, 4):
            ans = - epsilon_matrices(kk, ll, M)
            print(com(N[kk], N[ll]) == ans)


do_work()
