class Parser():
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.lines = f.readlines()

    def parse_vector(self):
        v = []
        for i in range(2, int(self.lines[0]) + 2):
            v.append(float(self.lines[i].strip('\n')))
        return v

    def parse_matrix(self):

        new_lines = [i for i in self.lines[int(self.lines[0])+3:]]

        intermediate = []
        for i in new_lines:
            intermediate.append(i.split(', '))

        # print(intermediate)

        a_ij = []
        line_vector = []
        column_vector = []

        d = []

        intermediate.sort(key=lambda x: int(x[1]))

        # print(intermediate)

        for i in intermediate:
            a_ij.append(float(i[0]))
            line_vector.append(int(i[1]))
            if int(i[1]) == int(i[2].strip('\n')):
                # make d vector
                d.append(float(i[0]))

        val = []

        i = 0
        line = 0
        # make val vector
        while i < len(line_vector):
            # print("******")
            # print("Line is ")
            # print(line)
            val.append(0)
            # print("i is")
            # print(i)
            count = 0
            for j in range(i + 1, len(line_vector)):
                if line_vector[i] == line_vector[j]:
                    # print("J is")
                    # print(j)
                    count += 1
                    val.append(a_ij[j])
                    # print("count is")
                    # print(count)
            # val.append(a_ij[i])
            val.insert(len(val) - count, a_ij[i])
            i += count + 1
            line += 1

        # print(val)

        for i in val:
            if i in d:
                val.remove(i)

        val.append(0)
        print(len(val))

        # make col vector
        col = []
        for i in intermediate:
            if float(i[0]) in val:
                col.append(int(i[2].strip('\n')))

        count1 = 0
        for i in range(len(val)):
            if val[i] == 0:
                col.insert(i, -count1)
                count1 += 1

        assert len(d) == int(self.lines[0])
        assert len(col) == len(val) and len(col) == len(new_lines) + 1

        return self.lines[0], len(new_lines), d, val, col