from math import prod
def is_lowest(x,y,height_map):
    width = len(height_map[0])
    height = len(height_map)
    point = height_map[y][x]
    lowest =  not(
            (x != 0 and point >= height_map[y][x-1]) or
            (y != 0 and point >= height_map[y-1][x]) or
            (x != width-1 and point >= height_map[y][x+1]) or
            (y != height-1 and point >= height_map[y+1][x])
            )
    return lowest

f = '''2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines()
f = open('input/day09.txt', 'r').read().splitlines()
input = [[int(y) for y in x] for x in f ]

width = len(input[0])
height = len(input)

low_points = [(x,y) for y in range(height) for x in range(width) if is_lowest(x,y,input)]
low_values = [1+input[y][x] for (x,y) in low_points]

print(sum(low_values))

basin_sizes = []
for point in low_points:
    next = set([point])
    searched = set()
    search = set([point])
    size=0
    while len(search) > 0:
        search = next.difference(searched)
        next = set()
        for (x,y) in search:
            searched.add((x,y))
            point = input[y][x]
            if point < 9:
                size += 1
            if x != 0 and point < input[y][x-1]:
                next.add((x-1,y))
            if y != 0 and point < input[y-1][x]:
                next.add((x,y-1))
            if x < width-1 and point < input[y][x+1]:
                next.add((x+1,y))
            if y < height-1 and point < input[y+1][x]:
                next.add((x,y+1))
    basin_sizes.append(size)

print(prod(sorted(basin_sizes)[-3:]))

