from random import uniform, randint


class Parser:
    def __init__(self, filename):
        self.filename = filename
        f = open(self.filename, 'r')
        self.lines = f.readlines()

    def parse_file_matrix(self):

        new_lines = [i for i in self.lines[3:]]

        intermediate = [i.split(', ') for i in new_lines]

        intermediate = list(map(lambda x: (float(x[0]), int(x[1]), int(x[2].strip('\n'))), intermediate))

        intermediate.sort(key=lambda x: (x[1], x[2]))

        #check simmetry
        swap_inter = list(map(lambda x: (x[0], x[2], x[1]), intermediate))

        swap_inter.sort(key=lambda x: (x[2], x[1]))

        for i, j in zip(swap_inter, intermediate):
            assert i[0] - j[0] < 10**(-8)

        return self.make_sparse_structure(intermediate, int(self.lines[0].strip('\n')))

    @staticmethod
    def make_sparse_structure(struct, size):
        count, i = 1, 1

        while i < len(struct):
            if struct[i - 1][1] != struct[i][1]:
                struct.insert(i, (0, -count))
                count += 1
                i += 1
            i += 1
        for i in range(len(struct)):
            if struct[i][0] != 0:
                struct[i] = struct[i][:1] + struct[i][2:]
                # print(i)

        struct.insert(0, (0, 0))
        struct.append((0, -size))
        return size, struct

    def generate_random(self, size):
        struct = []
        for i in range(size):
            struct.append((uniform(500, 1000), i, i))

        for i in range(size):
            a = randint(0, 5)
            for j in range(a):
                if i != j:
                    value = uniform(-10, 10)
                    struct.append((value, i, j))
                    struct.append((value, j, i))
        struct.sort(key=lambda x: (x[1], x[2]))
        return struct
