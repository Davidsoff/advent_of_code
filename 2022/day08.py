import itertools
import math
raw = open('input/day08.txt', 'r')
# raw = open('input/test.txt', 'r')
f = [line[:-1] for line in raw]

def is_visible(grid, transposed ,x,y):
    if x == 0 or y == 0 or x == len(grid)-1 or y == len(grid[0])-1:
        return 1
    else:
        left = is_direction_visible(grid[x][y], grid[x][:y])
        right = is_direction_visible(grid[x][y], grid[x][y+1:])
        top = is_direction_visible(grid[x][y], transposed[y][:x])
        bottom = is_direction_visible(grid[x][y], transposed[y][x+1:])
        return max([top, bottom, left, right])

def is_direction_visible(tree, neighbours):
    if len([x for x in neighbours if x >= tree]) > 0:
        return 0
    else:
        return 1
    

grid = [[int(x) for x in line] for line in f]
transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

p1 = sum([ is_visible(grid, transposed, x,y) for x in range(len(grid)) for y in range(len(grid[0]))])


print("part 1: ", p1)


def get_scenic_score(grid, transposed, x, y):
    left = get_direction_score(grid[x][y], grid[x][:y][::-1])
    right = get_direction_score(grid[x][y], grid[x][y+1:])
    top = get_direction_score(grid[x][y], transposed[y][:x][::-1])
    bottom = get_direction_score(grid[x][y], transposed[y][x+1:])
    scores = [top, bottom, left, right]
    return math.prod(scores)

def get_direction_score(tree, neighbours):
    if len([x for x in neighbours if x >= tree]) <= 0:
        return len(neighbours)
    else:
        count = 0
        for n in neighbours:
            if n < tree:
                count += 1
            else:
                count += 1
                return count

p2 = max([get_scenic_score(grid, transposed, x,y) for x in range(len(grid)) for y in range(len(grid[0]))])

print("part 2: ", p2)