from cn_parser import Parser
import math
from decimal import Decimal


class Gauss:
    def __init__(self, filename, epsilon=10**(-9)):
        parser = Parser(filename)
        details = parser.parse_matrix()
        self.b = parser.parse_vector()
        self.size = details[0]
        self.d = details[2]
        self.struct = details[3]
        self.epsilon = epsilon

        for i in self.d:
            assert i != 0

    def formula3(self, x_p):
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
        delta = 1
        k = 0
        while k < 10000:
            # print("****")
            # print("k is")
            # print(k)
            # print("delta is")
            # print(delta)
            x_c = self.formula3(x_p)
            delta = self.norm(x_c, x_p)
            x_p = x_c
            k += 1
            if delta <= self.epsilon:
                break
        if k < 10000:
            print("Nr of iterations used until convergence:  ")
            print(k)
            return x_p, k
        else:
            return False, k

    def check_solution(self):
        x_GS = self.seidel()[0]
        if x_GS:
            A_times_x_GS = self.multiply_solution_with_matrix(x_GS)
            diff = []
            for i in range(len(x_GS)):
                diff.append(A_times_x_GS[i] - self.b[i])
            assert max(diff) < self.epsilon
            return "Solution OK " + "Nr of iterations\n " + str(self.seidel()[1])
        else:
            return "No solution was found" + "Nr of iterations\n " + str(self.seidel()[1])

    def multiply_solution_with_matrix(self, solution):
        i = 1
        val = 0
        result = []
        while i < len(self.struct):
            if self.struct[i][1] < 0:
                i += 1
                result.append(val)
                val = 0
            else:
                val += self.struct[i][0] * solution[self.struct[i][1]]
                i += 1
        return result

    @staticmethod
    def norm(x_c, x_p):
        dist = [Decimal((a - b)) ** 2 for a, b in zip(x_c, x_p)]
        dist = math.sqrt(sum(dist))
        return dist

if __name__ == '__main__':

    print("First system, checking solution")
    gauss1 = Gauss("sisteme/m_rar_2017_1.txt")
    gauss1.check_solution()

    print("Second system, checking solution")  
    gauss2 = Gauss("sisteme/m_rar_2017_2.txt")
    gauss2.check_solution()

    print("Third system, checking solution")
    gauss3 = Gauss("sisteme/m_rar_2017_3.txt")
    gauss3.check_solution()

    print("Fourth system, checking solution")
    gauss4 = Gauss("sisteme/m_rar_2017_4.txt")
    print(gauss4.check_solution())
