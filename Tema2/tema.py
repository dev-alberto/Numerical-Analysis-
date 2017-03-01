from gui import GUI
from sympy import Matrix

stuff = GUI(Matrix([[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]]), [2, 3, 1], 10**(-10))


### Exercitiul 1 ###
print(stuff.decompose_wrapper())


### Exercitiul 2 ###
print(stuff.compute_determinant_wrapper())


### Exercitiu 3 ###
print(stuff.solution_wrapper())


### Exercitiu 4 ###
print(stuff.library_solution_wrapper())


### Exercitiu 5 ###
print(stuff.check_precision())


