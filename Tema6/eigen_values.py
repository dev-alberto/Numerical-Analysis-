from parser import Parser
from decimal import Decimal
import math
from random import random, randint, uniform
from mpmath import mp
from sympy import Matrix
import numpy as np


class Solver:
    def __init__(self, filename, epsilon=10**(-9), kmax=1000000):
        self.epsilon = epsilon
        self.parser = Parser(filename)
        self.n, self.struct = self.parser.parse_file_matrix()[0], self.parser.parse_file_matrix()[1]
        self.k = kmax

    def generate_random_sparse(self):
        size = randint(500, 1500)
        random_struct = self.parser.generate_random(size)
        self.randSize, self.randStruct = self.parser.make_sparse_structure(random_struct, size)

    def generate_svd_matrix(self):

        p = 3
        n = 2
        matrix = [[0 for i in range(n)] for j in range(p)]
        #print(matrix)
        for i in range(p):
            for j in range(n):
                matrix[i][j] = uniform(-10, 10)
        return mp.matrix(matrix)

    def find_svd_eigen_values(self, p, n):
        # A = self.generate_svd_matrix()
        # U, S, V = mp.svd_r(A)
        # print(U)
        # #print(S)
        # _U = Matrix(U)
        # _S = Matrix(S)
        # _V = Matrix(V)
        # print(_U.shape)
        # return S[0], len(S), float(max(S) / min(S))
        assert p > n
        a = np.random.randn(p, n)
        U, s, V = np.linalg.svd(a, full_matrices=True, compute_uv=True)
        rang = 0
        valori_sing = []
        for i in s:
            if i > 0:
                rang += 1
            valori_sing.append(i)

        S = np.zeros((p, n))
        S[:n, :n] = np.diag(s)
        print(S)
        print("Valori singulare")
        print(valori_sing)
        print("Rang " + str(rang))
        print("Numar de conditionare: ")
        print(max(valori_sing) / min(valori_sing))
        print("Norma: ")
        print(np.linalg.norm(np.dot(np.dot(U, S), np.transpose(V)), ord=np.inf))

    def generate_random_v0(self):
        v0 = [random() for i in range(self.n)]
        v0 = self.mul_vector_with_scalar(1 / self.v_norm(v0), v0)
        assert self.v_norm(v0) - 1 < self.epsilon
        return v0

    def find_largest_eigen_value(self, rand=False):
        v = self.generate_random_v0()

        if rand:
            self.generate_random_sparse()
            struct = self.randStruct
        else:
            struct = self.struct

        w = self.multiply_matrix_with_vector(v, struct)

        _lambda = self.scalar_vector_mul(w, v)
        k = 0
        while (k < self.k) and (self.norm(w, self.mul_vector_with_scalar(_lambda, v)) > self.n * self.epsilon):
            v = self.mul_vector_with_scalar(1/self.v_norm(w), w)
            w = self.multiply_matrix_with_vector(v, struct)
            _lambda = self.scalar_vector_mul(w, v)
            k += 1
        return _lambda, k

    @staticmethod
    def multiply_matrix_with_vector(vector, struct):
        i = 1
        val = 0
        result = []
        while i < len(struct):
            if struct[i][1] < 0:
                i += 1
                result.append(val)
                val = 0
            else:
                val += struct[i][0] * vector[struct[i][1]]
                i += 1
        return result

    @staticmethod
    def mul_vector_with_scalar(scalar, v):
        return [scalar*i for i in v]

    @staticmethod
    def scalar_vector_mul(x, y):
        s = 0
        for i, j in zip(x, y):
            s += i*j
        return s

    @staticmethod
    def v_norm(v):
        return math.sqrt(sum([i**2 for i in v]))

    @staticmethod
    def norm(x, y):
        dist = [Decimal((a - b)) ** 2 for a, b in zip(x, y)]
        dist = math.sqrt(sum(dist))
        return dist
