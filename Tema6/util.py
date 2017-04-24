def multiply_with_vector(struct, solution):
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