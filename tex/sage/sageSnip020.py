"""Some definitions for the Lie algebra so(3,1)."""


from sage.all import matrix


def fun_delta(i, j):
    """The function under the matrix delta."""
    if i == j:
        return 1
    return 0


def matrix_delta():
    """Return the matrix delta."""
    return matrix(4, fun_delta)


def fun_eta(i, j):
    """The function under the matrix eta."""
    if i == j == 0:
        return 1
    if i == j:
        return -1
    return 0


def matrix_eta():
    """Return the matrix eta."""
    return matrix(4, fun_eta)


def matrix_M(lam, mu):
    """The matrix M_{lam, mu}"""

    def fun_M(alpha, beta):
        """The function for the matrix alpha, beta"""
        delta = matrix_delta()
        eta = matrix_eta()
        return delta[mu, alpha] * eta[lam, beta] \
            - delta[lam, alpha] * eta[mu, beta]

    return matrix(4, fun_M)


def epsilon(i, j, k):
    """Return epsilon_{ijk}."""
    if i == j:
        return 0
    if i == k:
        return 0
    if j == k:
        return 0
    if (i, j, k) == (1, 2, 3):
        return 1
    if (i, j, k) == (1, 3, 2):
        return -1
    if (i, j, k) == (2, 1, 3):
        return -1
    if (i, j, k) == (2, 3, 1):
        return 1
    if (i, j, k) == (3, 2, 1):
        return -1
    if (i, j, k) == (3, 1, 2):
        return 1


def epsilon_matrices(i, j, matrices):
    """return sum_k epsilon_{ijk}martices[k]."""
    return sum([epsilon(i, j, k) * matrices[k] for k in [1, 2, 3]])


def com(A, B):
    """Return the commutator of A and B"""
    return A * B - B * A
