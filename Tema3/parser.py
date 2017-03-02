def parse_vector(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    v = []
    for i in range(2, 2019):
        v.append(float(lines[i].strip('\n')))
    return v


def parse(filename, small=False):

    f = open(filename, 'r')
    lines = f.readlines()

    if small is True:
        new_lines = [i for i in lines[8:]]
    else:
        new_lines = [i for i in lines[2020:]]

    intermediate = []
    for i in new_lines:
        intermediate.append(i.split(', '))

    #print(intermediate)

    a_ij = []
    line_vector = []
    column_vector = []

    d = []

    intermediate.sort(key=lambda x: int(x[1]))

    #print(intermediate)

    for i in intermediate:
         a_ij.append(float(i[0]))
         line_vector.append(int(i[1]))
         column_vector.append(int(i[2].strip('\n')))
         if int(i[1]) == int(i[2].strip('\n')):
            #make d vector
            d.append(float(i[0]))

    val = []
    col = []


    i = 0
    line = 0
    #make val vector
    while i < len(line_vector):
        #print("******")
        #print("Line is ")
        #print(line)
        val.append(0)
        #print("i is")
        #print(i)
        count = 0
        for j in range(i + 1, len(line_vector)):
            if line_vector[i] == line_vector[j]:
                #print("J is")
               # print(j)
                count += 1
                val.append(a_ij[j])
               # val[i] = a_ij[i]
                #val[j] = a_ij[j]
       # print("count is")
       # print(count)
        val.append(a_ij[i])
        i += count + 1
        line += 1

    #print(val)

    for i in val:
        if i in d:
           val.remove(i)

    val.append(0)

    print(val)

    #for i in val:
        #for k in intermediate:
            #if float(k[0]) == i:
                #col.append(k[2].strip('\n'))

    #print(len(col))
    # count1 = 0
    # for i in range(len(val)):
    #     if val[i] == 0:
    #         col.insert(i, -count1)
    #         count1 += 1
    #
    # print(len(d))
    # print(len(col))
    # print(len(val))
    #
    # #assert len(col) == len(val)
    #
    # return d, val, col


parse("a.txt")
