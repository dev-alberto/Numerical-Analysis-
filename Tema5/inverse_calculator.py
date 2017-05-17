from sympy import Matrix, eye


class Inverse:
    def __init__(self, n, A, epsilon=10**(-5), kmax=20):
        self.n = n
        self.A = Matrix(A)
        self.epsilon = epsilon
        self.k = kmax
        if self.A.shape[0] != n:
            raise ValueError("*** Matrix dimension and size don't match ***")

    @staticmethod
    def absSum(v):
        s = 0
        for i in v:
            s += abs(i)
        return s

    @staticmethod
    def norm1(matrix):
        v = []
        for i in range(matrix.shape[0]):
            v.append(Inverse.absSum(matrix.row(i)))
        return max(v)

    @staticmethod
    def normInf(matrix):
        v = []
        for i in range(matrix.shape[0]):
            v.append(Inverse.absSum(matrix.col(i)))
        return max(v)

    def computeInverse(self):
        const = 1 / (self.norm1(self.A) * self.normInf(self.A))
        V0 = const * self.A
        V1 = V0
        delta = 1
        k = 0
        while delta >= self.epsilon and k < self.k :
            V0 = V1
            V1 = V0 * (2 * eye(self.n) - self.A * V0)
            #print(V1)
            delta = self.norm1(V1 - V0)
            k += 1
        #print(k)
        return str(k) + '<br>' + str(V1) 


test = Inverse(3, [[1.0, 2.0, 3.0], [0, 4, 5], [1, 0, 6]])
print(test.computeInverse())

