def stage5():
    data = read_data()
    s1 = data[0].split()
    s2 = data[1].split()
    print(s1[0] + s2[0] + s1[1])
    print(s1[2] + s2[1] + s1[3])

def read_data():
    fn = input()
    # fn = 'example.txt'
    cnt = 0
    data = []
    with open(fn, 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip('\n')
            data.append(line)
            cnt += 1
            line = f.readline()
    if cnt == 1:
        data = data[0].split('\\n')
    return data

stage5()
