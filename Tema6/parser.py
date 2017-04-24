class Parser:
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.lines = f.readlines()

    def parse_vector(self):
        return [float(self.lines[i].strip('\n')) for i in range(2, int(self.lines[0]) + 2)]

    def parse_matrix(self):

        new_lines = [i for i in self.lines[3:]]

        intermediate = [i.split(', ') for i in new_lines]

        intermediate = list(map(lambda x: (float(x[0]), int(x[1]), int(x[2].strip('\n'))), intermediate))

        intermediate.sort(key=lambda x: (x[1], x[2]))

        d = [i[0] for i in intermediate if i[1] == i[2]]

        count, i = 1, 1
        while i < len(intermediate):
            if intermediate[i-1][1] != intermediate[i][1]:
                intermediate.insert(i, (0, -count))
                count += 1
                i += 1
            i += 1
        for i in range(len(intermediate)):
            if intermediate[i][0] != 0:
                intermediate[i] = intermediate[i][:1] + intermediate[i][2:]
                #print(i)
        #print(intermediate)
        intermediate.insert(0, (0, 0))
        intermediate.append((0, -int(self.lines[0].strip('\n'))))

        return int(self.lines[0].strip('\n')), len(new_lines), d, intermediate
