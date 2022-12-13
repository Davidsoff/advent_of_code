import itertools
import sys
raw = open('input/day12.txt', 'r')
# raw = open('input/test.txt', 'r')
data = raw.read()

S = chr(ord("a")-1)
E = chr(ord("z")+1)

f = [line.replace("S", S).replace("E", E) for line in data.splitlines()]
a = ord("a")
z = ord("z")
heights = [[ord(x)-a for x in line] for line in f]

start_idx = "".join(f).find(S)
end_idx = "".join(f).find(E)

width = len(heights[0])
height = len(heights)
start_x = start_idx % width
start_y = start_idx // width
end_x = end_idx % width
end_y = end_idx // width

distances = [[-1 for x in range(width)] for y in range(height)]
distances[end_y][end_x] = 0

heights[start_y][start_x] = a-a
heights[end_y][end_x] = z-a

distance = 0
changes = True
while(changes):
    changes = False
    distance += 1
    for y in range(height):
        for x in range(width):
            if distances[y][x] == distance-1:
                h = heights[y][x]
                if y < height-1:
                    if distances[y+1][x] < 0 and heights[y+1][x] >= h-1:
                        distances[y+1][x] = distance
                        changes = True
                if x < width-1:
                    if distances[y][x+1] < 0 and heights[y][x+1] >= h-1:
                        distances[y][x+1] = distance
                        changes = True
                if y > 0:
                    if distances[y-1][x] < 0 and heights[y-1][x] >= h-1:
                        distances[y-1][x] = distance
                        changes = True
                if x > 0:
                    if distances[y][x-1] < 0 and heights[y][x-1] >= h-1:
                        distances[y][x-1] = distance
                        changes = True

p1 = distances[start_y][start_x]

print()
print(f"part 1: {p1}")

p2 = min([distances[y][x] for x in range(width) for y in range(height) if heights[y][x] == 0 and distances[y][x]>0])


print(f"part 2: {p2}")