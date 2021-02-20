"""
Some check for the Lie algebra so(1,3).

This file has to be attached to sage's terminal.

sage: import os
sage: os.chdir('/path/to/tex/sage')
sage: attach('sageSnip022.sage')

This should only print a list of 'True'.
"""

from sage.all import I
from sageSnip020 import matrix_M
from sageSnip020 import epsilon_matrices
from sageSnip020 import com


def do_work():
    """Do the verifications."""
    M = {1: matrix_M(3, 2),
         2: matrix_M(1, 3),
         3: matrix_M(2, 1)}
    N = {1: matrix_M(0, 1),
         2: matrix_M(0, 2),
         3: matrix_M(0, 3)}
    L = {k: (M[k] + I * N[k])/2 for k in [1, 2, 3]}
    S = {k: (M[k] - I * N[k])/2 for k in [1, 2, 3]}

    # Check [L_i, L_j] = epsilon_{ijk}L_k
    for kk in range(1, 4):
        for ll in range(1, 4):
            ans = epsilon_matrices(kk, ll, L)
            print(com(L[kk], L[ll]) == ans)

    # Check [L_i, S_j] = 0
    for kk in range(1, 4):
        for ll in range(1, 4):
            print(com(L[kk], S[ll]) == 0)

    # Check [S_i, S_j] = epsilon_{ijk}S_k
    for kk in range(1, 4):
        for ll in range(1, 4):
            ans = epsilon_matrices(kk, ll, S)
            print(com(S[kk], S[ll]) == ans)

do_work()
