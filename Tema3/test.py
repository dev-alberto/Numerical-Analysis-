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

parser_a = Parser("small.txt")
parser_b = Parser("small2.txt")
sum = Parser("smallSum.txt")

matrix_a = Sparse(parser_a.parse_matrix())
matrix_b = Sparse(parser_b.parse_matrix())
good_sum = Sparse(sum.parse_matrix())
my_sum = matrix_a + matrix_b

print(my_sum)

print("****")

print(good_sum)

assert my_sum == good_sum