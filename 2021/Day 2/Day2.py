import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def part1(lines):
    x = 0
    y = 0

    for line in lines:
        dir, val = line.split()
        val = int(val)
        if dir == 'forward':
            x += val
        elif dir == 'up':
            y -= val
        else:
            y += val
    print (x*y)

def part2(lines):
    x = 0
    y = 0
    aim = 0

    for line in lines:
        dir, val = line.split()
        val = int(val)
        if dir == 'forward':
            x += val
            y += aim * val
        elif dir == 'up':
            aim -= val
        else:
            aim += val
    print(x*y)  
    


if __name__ == "__main__":
    lines = open(r"input.txt").read().splitlines()
    part1(lines)
    part2(lines)

