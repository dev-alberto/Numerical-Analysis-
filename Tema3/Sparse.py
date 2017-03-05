class Sparse:
    def __init__(self, matrix):
        self.n = matrix[0]
        self.NN = matrix[1]
        self.d = matrix[2]
        self.val = matrix[3]
        self.col = matrix[4]

    def __add__(self, other):
        assert other.n == self.n
        new_d = []
        new_val = []
        new_col = []

        for k in range(len(self.d)):
            new_d.append(self.d[k] + other.d[k])

        i = 0
        j = 0
        line = 0
        while i < len(self.val) - 1 and j < len(self.val) - 1:
            if self.val[i] == 0 and other.val[j] == 0:
                new_col.append(-line)
                new_val.append(0)
                line += 1
                if i < len(self.val):
                    i += 1
                if j < len(other.val):
                    j += 1

            if self.col[i] == other.col[j] and self.val[i] != 0 and other.val[j] != 0:
                new_val.append(self.val[i] + other.val[j])
                new_col.append(self.col[i])
                i += 1
                j += 1

            if self.col[i] != other.col[j] and self.val[i] != 0:
                new_val.append(self.val[i])
                new_col.append(self.col[i])
                i += 1

            if other.col[j] != self.col[i] and other.val[j] != 0:
                new_val.append(other.val[j])
                new_col.append(other.col[j])
                j += 1

        new_val.append(0)
        new_col.append(-self.n)

        return Sparse([self.n, len(new_val) - 1, new_d, new_val, new_col])

    def __mul__(self, other):
        pass

    def __str__(self):
        return "n: " + str(self.n) + "\n NN: " + str(self.NN) + "\n d: " + str(self.d) + "\n val: " + str(self.val) + \
               "\n col: " + str(self.col)

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

    def vector_mul(self):
        pass
