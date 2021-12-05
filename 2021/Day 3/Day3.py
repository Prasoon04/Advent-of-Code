import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def part1(lines):
    epsilon = ''
    gamma = ''
    listsize = len(lines)

    out = {}
    size = len(lines[0])

    for i in range(size):  #Creating dictionary
        out[i] = 0
    
    for line in lines:     #updating dictionary with if found 1 for every bit in the binary number
        for j in range(size):
            if line[j] == '1':
                out[j] += 1

    for i in range(size):  #creating gamma and epsilon
        if out[i] > listsize/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    epsilon = int(epsilon,2)
    gamma = int(gamma,2)
    print (epsilon * gamma)
 
def o2filter(i , o2list):
    newlist = []
    pos_count = 0
    if len(o2list) == 1:
        return o2list

    size = len(o2list)

    for line in o2list:
        if line[i] == '1':
            pos_count += 1
    
    if pos_count >= size/2:
        for line in o2list:
            if line[i] == '1':
                newlist.append(line)
    else:
        for line in o2list:
            if line[i] == '0':
                newlist.append(line)
    
    print(size, len(newlist))
    return newlist
    
def co2filter(i , co2list):
    newlist = []
    pos_count = 0
    if len(co2list) == 1:
        return co2list

    size = len(co2list)

    for line in co2list:
        if line[i] == '1':
            pos_count += 1
    
    if pos_count < size/2:
        for line in co2list:
            if line[i] == '1':
                newlist.append(line)
    else:
        for line in co2list:
            if line[i] == '0':
                newlist.append(line)
    
    return newlist

def part2(lines):
    size = len(lines[0])
    zerolist = []
    onelist = []

    for line in lines:
        if line[0] == '1':
            onelist.append(line)
        else:
            zerolist.append(line)       

    if len(onelist) > len(zerolist):
        o2list = onelist
        co2list = zerolist
    else:
        co2list = onelist
        o2list = zerolist
    
    for i in range(1, size):
        o2list = o2filter(i, o2list)
        co2list = co2filter(i, co2list)

    o2 = int(o2list[0], 2)
    co2 = int(co2list[0], 2)
    print(o2*co2)

if __name__ == "__main__":
    lines = open(r"input.txt").read().splitlines()
    part1(lines)
    part2(lines)
