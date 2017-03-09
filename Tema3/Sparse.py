class Sparse:
    def __init__(self, matrix):
        self.n = matrix[0]
        self.NN = matrix[1]
        self.d = matrix[2]
        self.val = matrix[3]
        self.col = matrix[4]
        self.zipped = list(zip(self.val, self.col))

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
            if self.col[i] < other.col[j] and self.col[i] >= 0:
                new_col.append(self.col[i])
                new_val.append(self.val[i])
                i += 1
            elif self.col[i] == other.col[j]:
                new_col.append(self.col[i])
                new_val.append(self.val[i] + other.val[j])
                i += 1
                j += 1
            elif self.col[i] > other.col[j] and other.col[j] >= 0:
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
        pass

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

