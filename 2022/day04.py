import itertools
f = [line[:-1] for line in open('input/day04.txt', 'r')]
# f = [line[:-1] for line in open('input/test.txt', 'r')]

def find_full_overlap(line):
    elves = line.split(",")
    elf1 = [int(x) for x in elves[0].split("-")]
    elf2 = [int(x) for x in elves[1].split("-")]
    return min([1, full_overlap(elf1, elf2) + full_overlap(elf2, elf1)])

def full_overlap(elf1, elf2):
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return 1
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return 1
    else:
        return 0

def find_some_overlap(line):
    elves = line.split(",")
    elf1 = [int(x) for x in elves[0].split("-")]
    elf2 = [int(x) for x in elves[1].split("-")]
    return some_overlap(elf1, elf2)

def some_overlap(elf1, elf2):
    if elf1[1] < elf2[0] or elf2[1] < elf1[0]:
        return 0
    else:
        return 1

p1 = sum([find_full_overlap(line) for line in f])

print("part 1: ", p1)

p2 = sum([find_some_overlap(line) for line in f])

print("part 2: ", p2)
