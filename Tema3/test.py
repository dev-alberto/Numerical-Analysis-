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
        self.parser_a = Parser("a.txt")
        self.parser_b = Parser("b.txt")

        self.matrix_a = Sparse(self.parser_a.parse_matrix())
        self.matrix_b = Sparse(self.parser_b.parse_matrix())

    def test_matrix_sum(self):
        parser_sum = Parser("aplusb.txt")
        assert (self.matrix_a + self.matrix_b) == Sparse(parser_sum.parse_matrix())

    def test_vector_product(self):
        #just print for now
        print(self.matrix_a.vector_mul(self.parser_a.make_prod_vector()))


test = Test()
test.test_matrix_sum()
test.test_vector_product()