from parser import Parser
from decimal import Decimal
import math
from random import randint, random


class Solver:
    def __init__(self, filename, p, epsilon=10**(-8), kmax=1000):
        self.epsilon = epsilon
        self.parser = Parser(filename)
        self.p = p
        self.n, self.struct = self.parser.parse_matrix()[0], self.parser.parse_matrix()[3]
        self.k = kmax

    def generate_random_sparse(self):
        pass

    def generate_random_v0(self):
        #change method for v0
        v0 = [random() for i in range(self.n)]
        #randCol = randint(0, self.n)
        v0 = self.mul_vector_with_scalar(1 / self.v_norm(v0), v0)
        print(self.v_norm(v0))
        assert self.v_norm(v0) - 1 < self.epsilon
        return v0

    def find_largest_eigen_value(self, rand=False):
        v = self.generate_random_v0()
        w = self.multiply_matrix_with_vector(v, self.struct)
        _lambda = self.scalar_vector_mul(w, v)
        k = 0
        while (k < self.k) and (self.norm(w, self.mul_vector_with_scalar(_lambda, v)) > self.n * self.epsilon):
            v = self.mul_vector_with_scalar(1/self.v_norm(w), w)
            w = self.multiply_matrix_with_vector(v, self.struct)
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


    # def transposition_mul(self, x, y):
    #     return self.multiply_normal_matrix_with_vector(self.multiply_column_vector_with_line_vector(y, x), y)

    @staticmethod
    def multiply_column_vector_with_line_vector(col, line):
        result = []
        for i in col:
            l = []
            for j in line:
                l.append(i*j)
            result.append(l)
        return result


    # @staticmethod
    # def multiply_normal_matrix_with_vector(A, line):
    #     result = []
    #     for i in range(len(A)):
    #         s = 0
    #         for j in range(len(A)):
    #             s += A[i][j] * line[i]
    #         result.append(s)
    #     return result

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
