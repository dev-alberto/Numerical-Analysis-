def parse_vector(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    v = []
    for i in range(2, 2019):
        v.append(float(lines[i].strip('\n')))
    return v

#TODO: Finish parsing file


def parse(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    new_lines = [i for i in lines[8:]]
    intermediate = []
    for i in new_lines:
        intermediate.append(i.split(', '))

    a_ij = []
    line_vector = []
    column_vector = []

    for i in intermediate:
        a_ij.append(float(i[0]))
        line_vector.append(int(i[1]))
        column_vector.append(int(i[2].strip('\n')))

    val = [0 for i in range(len(a_ij))]

    i = 0
    count = 0
    while i < len(line_vector):
        for j in range(i, len(line_vector)):
            print(line_vector[i])
            print("**")
            print(column_vector[i])
            if line_vector[i] == line_vector[j]:
                count += 1
                val[i] = a_ij[i]
                val[j] = a_ij[j]
        i += count
        count = 0


    #assert len(a_ij) == len(column_vector)
    print(line_vector)
    print(val)


parse("small.txt")
