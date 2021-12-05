
def part1(lines):
    x = 0
    y = 0

    for line in lines:
        dir, val = line.split()
        if dir == 'forward':
            x += int(val)
        elif dir == 'up':
            y -= int(val)
        else:
            y += int(val)
    print (x*y)


if __name__ == "__main__":
    lines = open(r"C:\Users\pgaut\Desktop\Advent of Code 2021\Day 2\input.txt").read().splitlines()
    part1(lines)

