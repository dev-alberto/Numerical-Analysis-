class Parser:
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.lines = f.readlines()

    def parse_vector(self):
        return [float(self.lines[i].strip('\n')) for i in range(2, int(self.lines[0]) + 2)]

    def make_prod_vector(self):
        return [int(self.lines[0]) - i for i in range(0, int(self.lines[0]))]

    def parse_matrix(self):

        #non zero elements
        new_lines = [i for i in self.lines[int(self.lines[0])+3:]]

        #list of lists with elements from file
        intermediate = [i.split(', ') for i in new_lines]

        intermediate.sort(key=lambda x: (int(x[1]), int(x[2].strip('\n'))))

        a_ij = [float(i[0]) for i in intermediate]
        line_vector = [int(i[1]) for i in intermediate]
        d = [float(i[0]) for i in intermediate if int(i[1]) == int(i[2].strip('\n'))]

        val = []
        special_line_haha = []
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
                 #   special_line_haha.append(line_vector[j])
                    # print("count is")
                    # print(count)
            # val.append(a_ij[i])
            val.insert(len(val) - count, a_ij[i])
           # special_line_haha.insert(len(val) - count, line_vector[i])
            i += count + 1
            line += 1

        # print(val)
      #  print(special_line_haha)
        for i in val:
            if i in d:
                val.remove(i)

        val.append(0)

        # make col vector
        col = [int(k[2].strip('\n')) for k in intermediate if float(k[0]) in val]

        count1 = 0
        for i in range(len(val)):
            if val[i] == 0:
                col.insert(i, -count1)
                count1 += 1

        assert len(d) == int(self.lines[0])
        assert len(col) == len(val) and len(col) == len(new_lines) + 1

        return int(self.lines[0].strip('\n')), len(new_lines), d, val, col

