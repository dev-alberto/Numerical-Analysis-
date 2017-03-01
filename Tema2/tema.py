from sympy import Matrix, pprint, ImmutableMatrix
from util import check_matrix, decompose, compute_determinant, direct_substitution, solve_diag_matrix, inverse_substitution, solve_using_LU, euclidean_norm, epsilon

#pprint(A.LDLdecomposition())
#pprint(A.LUdecomposition())

#check_matrix(A)


#print(solve_using_LU(A, [2, 3, 1]))


### Exercitiul 1 ###
def print_decomposition(A):
    pprint(decompose(A))


### Exercitiul 2 ###
def print_determinant(A):
    print(compute_determinant(A))


### Exercitiu 3 ###
def find_solution(A, b):
    L, D = decompose(A)
    z = direct_substitution(L, b)
    y = solve_diag_matrix(D, z)
    x = inverse_substitution(L.transpose(), y)
    print(x)


### Exercitiu 4 ###
def find_library_solution(A, b):
    x = solve_using_LU(A, b)
    print(x)
    return x


### Exercitiu 5 ###
def check_precision(A, b):
    x = find_library_solution(A, b)
    x_ = Matrix(A.shape[0], 1, x)
    b_ = Matrix(A.shape[0], 1, b)
    if abs(euclidean_norm(A * x_ - b_)) < epsilon:
        print("Good Solution")
    else:
        print("Bad Solution")


