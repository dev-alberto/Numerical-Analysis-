class Sparse:
    def __init__(self, matrix):
        self.n = matrix[0]
        self.NN = matrix[1]
        self.d = matrix[2]
        self.val = matrix[3]
        self.col = matrix[4]
        self.zipped = list(zip(self.val, self.col))
        #print(self.zipped)
        #self.zipped.sort(key=lambda x: x[1])

    def __add__(self, other):
        assert other.n == self.n
        new_d = []
        new_val = []
        new_col = []
        for k in range(len(self.d)):
            new_d.append(self.d[k] + other.d[k])

        i = 0
        j = 0
        while i < len(self.val) and j < len(self.val):
            if other.col[j] > self.col[i] >= 0:
                new_col.append(self.col[i])
                new_val.append(self.val[i])
                i += 1
            elif self.col[i] == other.col[j]:
                new_col.append(self.col[i])
                new_val.append(self.val[i] + other.val[j])
                i += 1
                j += 1
            elif self.col[i] > other.col[j] >= 0:
                new_col.append(other.col[j])
                new_val.append(other.val[j])
                j += 1
            elif self.col[i] > other.col[j] and other.col[j] < 0:
                new_col.append(self.col[i])
                new_val.append(self.val[i])
                i += 1
            elif other.col[j] > self.col[i] and self.col[i] < 0:
                new_col.append(other.col[j])
                new_val.append(other.val[j])
                j += 1
        return Sparse([self.n, len(new_val) - 1, new_d, new_val, new_col])

    def __mul__(self, other):
        assert other.n == self.n
        new_d = []
        new_val = []
        new_col = []
        # print("****")
        # print(self.prepare_matrix(other.val, other.col, self.n))
        # print("****")
        other.val, other.col = self.prepare_matrix(other.val, other.col, self.n)
        # l1 = self.prepare_line_or_column(self.val, self.col, 1, self.d)
        # c1 = self.prepare_line_or_column(other.val, other.col, 1, other.d)
        # print(l1)
        # print(c1)
        # print(self.interclasare(l1, c1))
        line = 0
        while line < self.n:
            print("****")
            print("Line Is : " + str(line))
            column = 0
            new_val.append(0)
            new_col.append(-line)
            #current_line = self.get_line_from_val(self.val, self.col, line)
            current_line = self.prepare_line_or_column(self.val, self.col, line, self.d)
            while column < self.n:
                #current_line = self.get_line_from_val(self.val, self.col, line)
               # print("Column is: " + str(column))
                #print(current_line)
                #current_column = self.get_line_from_val(other.val, other.col, column)
                current_column = self.prepare_line_or_column(other.val, other.col, column, other.d)
                value = self.interclasare(current_line, current_column)
                if value != 0:
                    new_val.append(value)
                    new_col.append(column)
                column += 1
            line += 1
        print(new_val)
        print(new_col)

    def vector_mul(self, vector):
        assert self.n == len(vector)
        line = 0
        i = 0
        result = []
        while i < len(self.col)-1:
            s = 0
            if (self.col[i] < 0 or i == 0) and self.col[i] != -self.n:
                s += vector[line] * self.d[line]
                line += 1
                i += 1
            while self.col[i] >= 0:
                s += self.val[i] * vector[self.col[i]]
                i += 1
            result.append(s)

        return result

    def __str__(self):
        return "n: " + str(self.n) + "\n NN: " + str(self.NN) + "\n d: " + str(self.d) + "\n val: " + str(self.val) + \
               "\n col: " + str(self.col) + '\n zipped: ' + str(self.zipped)

    def __eq__(self, other):
        if other.n != self.n:
            return False
        elif other.NN != self.NN:
            return False
        elif sorted(other.d) != sorted(self.d):
            return False
        elif sorted(other.val) != sorted(self.val):
            return False
        elif sorted(other.col) != sorted(self.col):
            return False
        return True

    @staticmethod
    def prepare_matrix(val, col, n):
        new_val = []
        new_line = []
        line = 0
       # a_line = [val[i] for i in range(len(val)) if col[i] == line and i != 0]
        while line < n:
            new_val.append(0)
            new_line.append(-line)
            for i in range(len(val)):
                if col[i] == line and i != 0:
                    new_val.append(val[i])
                    new_line.append(Sparse.get_line(val, i))
            line += 1
        new_val.append(0)
        new_line.append(-n)
        return new_val, new_line

    @staticmethod
    def get_line(val, stop):
        count = 0
        for i in range(stop):
            if val[i] == 0:
                count += 1
        return count - 1

    # @staticmethod
    # def get_line_from_val(val, col, line):
    #     slice1, slice2 = 0, 0
    #     #print(col)
    #     for i in range(len(col)):
    #         if col[i] == -line:
    #             slice1 = i
    #         if col[i] == -line - 1:
    #             slice2 = i
    #     if line == 0:
    #         slice1 = 0
    #     return list(zip(val[slice1:slice2+1], col[slice1:slice2+1]))

    @staticmethod
    def prepare_line_or_column(val, col, line, d):
        slice1, slice2 = 0, 0
        # print(col)
        for i in range(len(col)):
            if col[i] == -line:
                slice1 = i
            if col[i] == -line - 1:
                slice2 = i
        if line == 0:
            slice1 = 0
        preped = list(zip(val[slice1:slice2+1], col[slice1:slice2+1]))
        preped.insert(0, (d[-preped[0][1]], -preped[0][1]))
        preped.sort(key=lambda x: x[1])
        aux = preped[0]
        del preped[0]
        preped.append(aux)
        if preped[0][1] != 0:
            del preped[0]
        else:
            for i in range(len(preped)):
                if preped[i] == (0, 0):
                    del preped[i]
                    break
        del preped[-1]
        return preped

    @staticmethod
    def interclasare(line, col):
        i, j = 0, 0

        # line_aux = line[:]
        #
        # line_aux.insert(0, (dl[-line[0][1]], -line[0][1]))
        # col.insert(0, (dc[-col[0][1]], -col[0][1]))
        #
        # line_aux.sort(key=lambda x: x[1])
        # col.sort(key=lambda x: x[1])
        # aux1, aux2 = line_aux[0], col[0]
        # del line_aux[0]
        # del col[0]
        # line_aux.append(aux1)
        # col.append(aux2)
        # if line_aux[0][1] != 0:
        #     del line_aux[0]
        #     #del col[0]
        # else:
        #     for i in range(len(line_aux)):
        #         if line_aux[i] == (0, 0):
        #             del line_aux[i]
        #             break
        # if col[0][1] != 0:
        #     del col[0]
        # else:
        #     for i in range(len(col)):
        #         if col[i] == (0, 0):
        #             del col[i]
        #             break
        # del line_aux[-1]
        # del col[-1]
        #print(col)
        val = 0
        while i < len(line) and j < len(col):
            # print("**")
            # print(line[i][1])
            # print("\n")
            # print(col[j][1])
            # print("***")
            if line[i][1] < col[j][1]:
                i += 1
            elif line[i][1] > col[j][1]:
                j += 1
            elif line[i][1] == col[j][1]:
                val += line[i][0] * col[j][0]
                i += 1
                j += 1
        #print(val)
        return val
