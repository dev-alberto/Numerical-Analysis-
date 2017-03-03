import util
from sympy import Matrix


class LDL_Decomposition:
    def __init__(self, A, b, epsilon):
        util.check_matrix(A, epsilon)
        # we need a copy for A, because our "efficient" way of decomposing the
        # Matrix A actually modifies said matrix, and we need the initial matrix for exercise 4
        A_copy = A[:, :]
        self.A = A
        self.b = b
        self.epsilon = epsilon
        self.L, self.D = util.decompose(A_copy)

    def decompose_wrapper(self):
        """Exercise 1"""
        return "L matrix: " + str(self.L) + " <br/>\nD matrix: " + str(self.D)

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

    def LU_Wrapper(self):
        return str(util.LU_decomposition(self.A))

if __name__ == "__main__":
    CH = LDL_Decomposition(Matrix([[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]]), [2, 3, 1], 10 ** (-10))

    #CH = LDL_Decomposition(Matrix([[3, 2, -2], [2, 3, 1], [-2, 1, 3]]), [-3, 2, 7], 10 ** (-10))

    ### Exercitiul 1 ###
    print(CH.decompose_wrapper())

    ### Exercitiul 2 ###
    print(CH.compute_determinant_wrapper())

    ### Exercitiu 3 ###
    print(CH.solution_wrapper())

    ### Exercitiu 4 ###
    print(CH.library_solution_wrapper())

    ### Exercitiu 5 ###
    print(CH.check_precision())
