from operator import mul
import functools
import math


def check_matrix(A, epsilon):
    #check symmetry
    assert A.transpose() == A
    #check pozitive definite
    eigen = A.eigenvals()
    for i in eigen:
        assert eigen[i] > epsilon


def decompose(A):
    n = A.shape[0]
    D = [0 for i in range(n)]
    #no restriction yet
    #L = Matrix(n, n, L_lambda)
    for p in range(n):
        D[p] = A[p, p] - sum([D[k] * A[p, k] ** 2 for k in range(0, p)])
        for i in range(p+1, n):
            A[i, p] = (A[i, p] - sum([D[k] * A[i, k] * A[p, k] for k in range(0, p)])) / D[p]
    for i in range(n):
        A[i, i] = 1
        for j in range(i+1, n):
            A[i, j] = 0
    return A, D


def compute_determinant(D):
  #  L, D = decompose(A)
        return functools.reduce(mul, D)


def direct_substitution(L, b):
    n = L.shape[0]
    z = [0 for i in range(n)]
    for i in range(n):
        z[i] = (b[i] - sum([L[i, j] * z[j] for j in range(i)])) / L[i, i]
    return z


def solve_diag_matrix(D, z):
    return [z[i] / D[i] for i in range(len(D))]


def inverse_substitution(L, y):
    n = L.shape[0]
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum([L[i, j] * x[j] for j in range(i+1, n)])) / L[i, i]
    return x


def LU_decomposition(A):
    return A.LUdecomposition()


def solve_using_LU(A, b):
    L, U, _ = LU_decomposition(A)
    y = direct_substitution(L, b)
    x = inverse_substitution(U, y)
    return x


def euclidean_norm(vector):
    s = sum([vector[i]**2 for i in range(len(vector))])
    return math.sqrt(s)