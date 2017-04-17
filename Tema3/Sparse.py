import itertools


class Sparse:
    def __init__(self, matrix, epsilon=10**(-10)):
        self.n = matrix[0]
        self.NN = matrix[1]
        self.d = matrix[2]
        self.struct = matrix[3]
        self.epsilon = epsilon

    def __str__(self):
        return "n: " + str(self.n) + "\n NN: " + str(self.NN) + "\n d: " + str(self.d) + "\n efficientStruct: " + str(self.struct)

    def __mul__(self, other):
        other.struct = self.prepare_for_multiplication(other.struct, other.n)
        # print(other.struct)
        # line0 = Sparse.extract_line_or_column(self.struct, 0)
        # print(line0)
        # print(self.mul_line_matrix(line0, 0, other.struct))
        line = 0
        new_struct = []
        d = []
        while line < self.n:
            #print("****")
            #print("Line Is : " + str(line))
            current_line = self.extract_line_or_column(self.struct, line)
            assert len(current_line) < 13
            res = self.mul_line_matrix(current_line, line, other.struct)
            new_struct.append(res[0])
            d.append(res[1])
            line += 1
        new_struct = list(itertools.chain.from_iterable(new_struct))
        new_struct.append((0, -self.n))
        return Sparse([other.n, len(new_struct) - len(d) - 1, d, new_struct])

    def __add__(self, other):
        new_struct = []
        i, j = 0, 0
        new_d = []

        for k in range(len(self.d)):
            new_d.append(self.d[k] + other.d[k])

        while i < len(self.struct) and j < len(other.struct):
            if other.struct[j][1] > self.struct[i][1] >= 0:
                new_struct.append((self.struct[i][0], self.struct[i][1]))
                i += 1
            elif self.struct[i][1] > other.struct[j][1] >= 0:
                new_struct.append((other.struct[j][0], other.struct[j][1]))
                j += 1
            elif self.struct[i][1] == other.struct[j][1]:
                new_struct.append((self.struct[i][0] + other.struct[j][0], self.struct[i][1]))
                i += 1
                j += 1
            elif self.struct[i][1] < 0 and other.struct[j][1] >= 0:
                new_struct.append((other.struct[j][0], other.struct[j][1]))
                j += 1
            elif other.struct[j][1] < 0 and self.struct[i][1] >= 0:
                new_struct.append((self.struct[i][0], self.struct[i][1]))
                i += 1
        return Sparse([self.n, len(new_struct) - len(new_d) - 1, new_d, new_struct])

    def vector_mul(self, expected_result):
        result = []
        line = 0
        while line < self.n:
            current_line = self.extract_line_or_column(self.struct, line)
            result.append(self.multiply_line_with_prod_vector(current_line, self.n))
            line += 1

        for i in range(len(result)):
            assert result[i] - expected_result[i] < self.epsilon

        #return result

    def __eq__(self, other):
        for i in range(len(self.struct)):
            if self.struct[i][0] - other.struct[i][0] > self.epsilon:
                return False
        return True

    @staticmethod
    def multiply_line_with_prod_vector(line, n):
        result = 0
        for i in line:
            result += i[0] * (n - i[1])
        return result


    @staticmethod
    def prepare_for_multiplication(struct, n):
        new_val = []
        new_line = []
        line = 0
        # a_line = [val[i] for i in range(len(val)) if col[i] == line and i != 0]
        while line < n:
            new_val.append(0)
            new_line.append(-line)
            for i in range(len(struct)):
                if struct[i][1] == line and i != 0:
                    new_val.append(struct[i][0])
                    new_line.append(Sparse.get_line(struct, i))
            line += 1
        new_val.append(0)
        new_line.append(-n)
        return list(zip(new_val, new_line))

    @staticmethod
    def get_line(val, stop):
        count = 0
        for i in range(stop):
            if val[i][0] == 0:
                count += 1
        return count - 1

    @staticmethod
    def extract_line_or_column(struct, line):
        slice1, slice2 = 0, 0
        for i in range(len(struct)):
            if struct[i][1] == -line:
                slice1 = i
            if struct[i][1] == -line - 1:
                slice2 = i
        if line == 0:
            slice1 = 0
        return struct[slice1:slice2+1]

    @staticmethod
    def mul_line_matrix(line, line_nr, struct_):
        result = []
        i, j = 0, 0
        val = 0
        col_nr = 0
        result.append((0, -line_nr))
        col_value = 0
        while i < len(line) and j < len(struct_):

            if line[i][0] == 0 == line[i][1]:
                #print("(0, 0)")
                i += 1

            if line[i][1] == -line_nr and line[i][1] != 0:
                i += 1

            if struct_[j][0] == struct_[j][1] == 0:
                #print("(0, 0)")
                j += 1

            if line[i][1] < 0 and struct_[j][1] < 0:
                #print("Pivotez")
                #print("i, j sunt ")
                #print(i, j)
                j += 1
                i = i - len(line) + 2
                #print("new i")
                #print(i)
                #print("valoarea e")
                #print(val)
                if val != 0:
                    result.append((val, col_nr))
                if col_nr == line_nr:
                    col_value = val
                col_nr += 1
                if j == len(struct_):
                    break
                val = 0

            if struct_[j][1] > line[i][1] >= 0:
                #print("shiftez linia")
                i += 1

            if line[i][1] > struct_[j][1] >= 0:
                #print("shiftez coloana")
                j += 1

            if struct_[j][1] < 0 <= line[i][1]:
                #print("astept sa se termine linia")
                i += 1

            if line[i][1] < 0 <= struct_[j][1]:
                #print("astept sa se termine coloana ")
                j += 1

            if struct_[j][1] == line[i][1] and struct_[j][0] != 0 and line[i][0] != 0:
                #print("in sfarsit inmultesc ceva")
                val += struct_[j][0] * line[i][0]
                i += 1
                j += 1

        return result, col_value

