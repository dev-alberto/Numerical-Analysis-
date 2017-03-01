import util
from sympy import Matrix


class GUI:
    def __init__(self, A, b, epsilon):
        util.check_matrix(A, epsilon)
        # we need a copy for A, because our "efficient" way of decomposing the Matrix A actually modifies said matrix, and we still need it
        A_copy = A[:, :]
        self.A = A
        self.b = b
        self.epsilon = epsilon
        self.L, self.D = util.decompose(A_copy)

    def decompose_wrapper(self):
        """Exercise 1"""
        return "L matrix: " + str(self.L) + " D matrix: " + str(self.D)

    def compute_determinant_wrapper(self):
        """Exercise 2"""
        return "Matrix determinant " + str(util.compute_determinant(self.D))

    def solution_wrapper(self):
        """Exercise 3"""
        z = util.direct_substitution(self.L, self.b)
        y = util.solve_diag_matrix(self.D, z)
        x = util.inverse_substitution(self.L.transpose(), y)
        return "Solution to system of equations: " + str(x)

    def library_solution_wrapper(self):
        """Exercise 4"""
        return "Library solution to our system of equations: " + str(util.solve_using_LU(self.A, self.b))

    def check_precision(self):
        """Exercise 5"""
        x = util.solve_using_LU(self.A, self.b)
        x_ = Matrix(self.A.shape[0], 1, x)
        b_ = Matrix(self.A.shape[0], 1, self.b)
        if abs(util.euclidean_norm(self.A * x_ - b_)) < self.epsilon:
            return "Good Solution"
        else:
            return "Bad Solution"
