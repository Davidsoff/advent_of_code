import itertools
raw = open('input/day06.txt', 'r')
# raw = open('input/test.txt', 'r')
f = [line[:-1] for line in raw]

def process_line(line, length):
    for i in range(len(line)-(length-1)):
        group = line[i:i+length]
        if len(set(group)) == length:
            print(i+length, group)
            return i+length

for line in f:
    p1 = process_line(line, 4)
    p2 = process_line(line, 14)
    break

print("part 1: ", p1)

print("part 2: ", p2)