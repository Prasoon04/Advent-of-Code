
f = open(r"C:\Users\pgaut\Desktop\Advent of Code 2021\Day 1\input.txt")
depths = []
for line in f:
    depths.append(int(line.strip('\n')))
count1 = 0
count2 = 0
prev = depths[0] + depths[1] + depths[2]
curr = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        count1 += 1

for i in range(0, len(depths)-2):
    curr = depths[i] + depths[i+1] + depths[i+2]
    if curr > prev:
        count2 += 1
    prev = curr


print(count1)
print(count2)
f.close()