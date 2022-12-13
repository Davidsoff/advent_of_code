import itertools
raw = open('input/day10.txt', 'r')
# raw = open('input/test.txt', 'r')
f = [line[:-1].split(" ") for line in raw]

X = 1
total_cycles = 0
instructions = []

for line in f:
    if len(line) == 1:
        instructions.append(0)
    else:
        instructions.append(0)
        instructions.append(int(line[1]))

cycles = []
width = 40
pixels = []

for i in range(len(instructions)):
    y = i % width
    x = i - (y * width)
    # start
    # during
    lit = y >= X-1 and y <= X+1
    pixels.append("#" if lit else ".")
    # after
    X += instructions[i]
    cycles.append(X)


p1 = sum([cycles[poi-2]*poi for poi in range(20,221,40)])

print(f"part 1: {p1}")

print("part2:")
for i in range(0, len(pixels), width):
    x = i
    print("".join(pixels[x:x+width]))


# print(f"part 2: {p2}")