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


if __name__ == "__main__":
    lines = open(r"input.txt").read().splitlines()
    part1(lines)
