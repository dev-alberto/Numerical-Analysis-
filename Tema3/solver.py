from parser import Parser
from Sparse import Sparse
import math


class Gauss:
    def __init__(self, filename, epsilon=10**(-10)):
        parser = Parser(filename)
        details = parser.parse_matrix()
        self.b = parser.parse_vector()
        self.size = details[0]
        self.d = details[2]
        self.struct = details[3]
        self.epsilon = epsilon

    def formula3(self, x_p):
        #print(Sparse.extract_line_or_column(self.struct, 3000))
        x = []
        line = 0
        while line < self.size:
            #print("Line is")
            print(line)
            current_line = Sparse.extract_line_or_column(self.struct, line)
            #_j = [j for j in range(len(current_line)) if (line > current_line[j][1] >= 0)]
            #print(_j)
            #j_ = [j for j in range(len(current_line)) if current_line[j][1] > line]
            #print(j_)
            x.append((self.b[line] - sum([current_line[j][0] * x[j] for j in range(len(current_line)) if (line > current_line[j][1] >= 0)]) - sum([current_line[j][0] * x_p[j] for j in range(len(current_line)) if current_line[j][1] > line])) / self.d[line])
            line += 1
        return x

    def revised_formula3(self, x_p):
        x = [0 for i in range(self.size)]
        line = 0
        i = 0
        s1, s2 = 0, 0
        while line < self.size:
           # print(line)
            if self.struct[i][1] < 0:
                x[line] = (self.b[line] - s1 - s2) / self.d[line]
                line += 1
                i += 1
                s1, s2 = 0, 0
            elif line > self.struct[i][1] >= 0:
                s1 += self.struct[i][0] * x[self.struct[i][1]]
                i += 1
            elif self.struct[i][1] > line:
                s2 += self.struct[i][0] * x_p[self.struct[i][1]]
                i += 1
            elif self.struct[i][1] == line:
                i += 1
        return x

    def seidel(self):
        x_p = [0 for i in range(self.size)]
        #x_c = [0 for i in range(self.size)]
        delta = 1
        k = 0
        while k < 10000:
            print("****")
            print("k is")
            print(k)
            print("delta is")
            print(delta)
            #x_c = self.formula3(x_p)
            x_c = self.revised_formula3(x_p)
            delta = self.norm(x_c, x_p)
            x_p = x_c
            k += 1
            if delta <= self.epsilon:
                print(x_c)
                break
        #return x_c

    @staticmethod
    def norm(x_c, x_p):
        dist = [(a - b) ** 2 for a, b in zip(x_c, x_p)]
        dist = math.sqrt(sum(dist))
        return dist

if __name__ == '__main__':
    gauss = Gauss("sisteme/m_rar_2017_1.txt")
    print(gauss.size)
   # gauss.formula3()
    gauss.seidel()