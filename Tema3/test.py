import time
from datetime import timedelta
from Sparse import Sparse
from parser import Parser


# f = open("a.txt", 'r')
# lines = f.readlines()
# new_lines = [i for i in lines[int(lines[0])+3:]]
# intermediate = [i.split(', ') for i in new_lines]
# intermediate.sort(key=lambda x: int(x[1]))
#
# print(intermediate[1][0])
#
# for i in range(len(intermediate)):
#     for j in range(i+1, len(intermediate)):
#         if (int(intermediate[i][1]) == int(intermediate[j][1])) and (int(intermediate[i][2].strip('\n')) == int(intermediate[j][2].strip('\n'))):
#             print("nuuuu")


class Test:
    def __init__(self):
        self.parser_a = Parser("matrici_tema3/a.txt")
        self.parser_b = Parser("matrici_tema3/b.txt")
        self.parser_sum = Parser("matrici_tema3/aplusb.txt")
        self.parser_prod = Parser("matrici_tema3/aorib.txt")

        self.matrix_a = Sparse(self.parser_a.parse_matrix())
        self.matrix_b = Sparse(self.parser_b.parse_matrix())

        self.matrix_sum = Sparse(self.parser_sum.parse_matrix())
        self.matrix_prod = Sparse(self.parser_prod.parse_matrix())

    def test_matrix_sum(self):
        assert (self.matrix_a + self.matrix_b) == self.matrix_sum

    def test_vector_product(self):

        self.matrix_a.vector_mul(self.parser_a.parse_vector())
        self.matrix_b.vector_mul(self.parser_b.parse_vector())
        self.matrix_sum.vector_mul(self.parser_sum.parse_vector())
        self.matrix_prod.vector_mul(self.parser_prod.parse_vector())

    def test_matrix_product(self):
        assert self.matrix_a * self.matrix_b == self.matrix_prod

if __name__ == '__main__':
    start = time.time()
    print("Commencing tests: ")
    test = Test()
    print("Starting A + B test: ")
    test.test_matrix_sum()
    print("A+B success")
    print("Starting A*x, B*x, (A+B)*x, (A*B)*x tests")
    test.test_vector_product()
    print("Vector prods success")
    print("Starting A*B test")
    test.test_matrix_product()
    print("Matrix product was successful")
    print('ALL DONE, time elapsed: ')
    elapsed = time.time() - start
    print(str(timedelta(minutes=elapsed)))
