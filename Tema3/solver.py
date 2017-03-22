from parser import Parser
from Sparse import Sparse
import math


class Gauss:
    def __init__(self, filename):
        parser = Parser(filename)
        details = parser.parse_matrix()
        self.b = parser.parse_vector()
        self.size = details[0]
        self.d = details[2]
        self.struct = details[3]

    def formula3(self, x_p):
        print(Sparse.extract_line_or_column(self.struct, 3000))
        x = []
        line = 0
        while line < self.size:
            current_line = Sparse.extract_line_or_column(self.struct, line)
            _j = [j for j in range(len(current_line)) if current_line[j][1] < line]
            j_ = [j for j in range(len(current_line)) if current_line[j][1] > line]
            x.append((self.b[line] - sum([current_line[j][0] * x[j] for j in _j]) - sum([current_line[j][0] * x_p[j] for j in j_])) / self.d[line])
            line += 1
        return x

    def seidel(self):
        pass

    @staticmethod
    def norm(x_c, x_p):
        dist = [(a - b) ** 2 for a, b in zip(x_c, x_p)]
        dist = math.sqrt(sum(dist))
        return dist

if __name__ == '__main__':
    gauss = Gauss("sisteme/m_rar_2017_1.txt")
    print(gauss.size)
   # gauss.formula3()